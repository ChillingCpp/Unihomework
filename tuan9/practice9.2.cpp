// Practice 9.2 - cut a BMP file into equal parts.
// Build: g++ -std=c++17 -O2 practice9.2.cpp -o cutbmp
// Syntax:
//   cutbmp <bitmap> [-h <parts in height>] [-w <parts in width>]
// Examples:
//   cutbmp img1.bmp -h 3
//   cutbmp img1.bmp -h 2 -w 4
//
// Output files are named <name>_part1.bmp, <name>_part2.bmp, ...
// Supported input: uncompressed Windows BMP, 1/4/8/16/24/32 bpp.

#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

struct BMP {
    unsigned char *data;
    uint32_t sz;       // real file size
    uint32_t off;      // offset to pixel data
    uint32_t w;        // width in pixels
    uint32_t h;        // absolute height in pixels
    uint32_t stride;   // bytes per stored row, including padding
    uint16_t bpp;      // bits per pixel
    bool top;          // true if height is negative (top-down)
};

uint16_t g16(const unsigned char *p) {
    return (uint16_t)((uint16_t)p[0] | ((uint16_t)p[1] << 8));
}

uint32_t g32(const unsigned char *p) {
    return (uint32_t)p[0]
         | ((uint32_t)p[1] << 8)
         | ((uint32_t)p[2] << 16)
         | ((uint32_t)p[3] << 24);
}

void p16(unsigned char *p, uint16_t v) {
    p[0] = (unsigned char)(v & 0xFF);
    p[1] = (unsigned char)((v >> 8) & 0xFF);
}

void p32(unsigned char *p, uint32_t v) {
    p[0] = (unsigned char)(v & 0xFF);
    p[1] = (unsigned char)((v >> 8) & 0xFF);
    p[2] = (unsigned char)((v >> 16) & 0xFF);
    p[3] = (unsigned char)((v >> 24) & 0xFF);
}

// Read bits MSB-first from a row. Used for 1/4-bit BMPs.
uint32_t getbits(const unsigned char *p, uint64_t bit, int n) {
    uint32_t v = 0;
    for (int i = 0; i < n; i++) {
        uint64_t b = bit + i;
        v = (v << 1) | ((p[b >> 3] >> (7 - (b & 7))) & 1u);
    }
    return v;
}

void putbits(unsigned char *p, uint64_t bit, int n, uint32_t v) {
    for (int i = 0; i < n; i++) {
        uint64_t b = bit + i;
        unsigned char mask = (unsigned char)(1u << (7 - (b & 7)));
        if ((v >> (n - 1 - i)) & 1u)
            p[b >> 3] |= mask;
        else
            p[b >> 3] &= (unsigned char)~mask;
    }
}

void show() {
    cout << "cutbmp <bitmap> [-h <parts in height>] [-w <parts in width>]\n";
    cout << "  cutbmp img1.bmp -h 3\n";
    cout << "  cutbmp img1.bmp -h 2 -w 4\n";
    cout << "Output: <name>_part1.bmp, <name>_part2.bmp, ...\n";
}

bool getnum(const char *s, int &v) {
    char *e;
    long x = strtol(s, &e, 10);
    if (e == s || *e != '\0' || x <= 0 || x > 100000) return false;
    v = (int)x;
    return true;
}

bool readfile(const string &path, unsigned char *&data, uint32_t &sz) {
    ifstream f(path, ios::binary);
    if (!f) return false;

    f.seekg(0, ios::end);
    streamoff n = (streamoff)f.tellg();
    if (n <= 0 || (uint64_t)n > 0xFFFFFFFFu) return false;
    f.seekg(0, ios::beg);

    sz = (uint32_t)n;
    data = new unsigned char[sz];
    f.read((char *)data, (streamsize)sz);
    if (f.gcount() != (streamsize)sz) {
        delete[] data;
        data = 0;
        return false;
    }
    return true;
}

bool writefile(const string &path, const unsigned char *data, uint32_t sz) {
    ofstream f(path, ios::binary | ios::trunc);
    if (!f) return false;
    f.write((const char *)data, (streamsize)sz);
    f.close();
    return (bool)f;
}

bool parse(BMP &b) {
    if (b.sz < 54) return false;
    if (b.data[0] != 'B' || b.data[1] != 'M') return false;

    b.off = g32(b.data + 10);
    uint32_t hs = g32(b.data + 14);
    if (hs < 40 || (uint64_t)14 + hs > b.off || b.off > b.sz) return false; /// kích thước, thông tin trong các header không hợp lệ

    int32_t sw = (int32_t)g32(b.data + 18);
    int32_t sh = (int32_t)g32(b.data + 22);
    uint16_t planes = g16(b.data + 26);
    b.bpp = g16(b.data + 28);
    uint32_t comp = g32(b.data + 30);

    if (sw <= 0 || sh == 0 || sh == INT32_MIN) return false; // sai kích thước
    if (planes != 1) return false;
    if (comp != 0 && comp != 3) return false;
    if (b.bpp != 1 && b.bpp != 4 && b.bpp != 8 &&
        b.bpp != 16 && b.bpp != 24 && b.bpp != 32) return false; /// 1/4/8/16/24/32

    b.w = (uint32_t)sw;
    b.top = sh < 0;
    b.h = (uint32_t)(b.top ? -sh : sh);

    uint64_t row = ((uint64_t)b.w * b.bpp + 7) / 8;
    b.stride = (uint32_t)((row + 3) / 4 * 4);
    if ((uint64_t)b.off + (uint64_t)b.stride * b.h > b.sz) return false; /// file này có bit dư thừa so với kích thước thật
    return true;
}

string basename(const string &p) {
    size_t slash = p.find_last_of("/\\");
    size_t dot = p.find_last_of('.');
    if (dot == string::npos || (slash != string::npos && dot < slash))
        dot = p.size();
    return p.substr(0, dot);
}

bool split(const BMP &b, int nh, int nw, const string &base) {
    if ((uint32_t)nh > b.h || (uint32_t)nw > b.w) {
        cerr << "Number of parts is larger than the image dimension\n";
        return false;
    }
    if ((long long)nh * nw > 1000000) {
        cerr << "Too many parts\n"; 
        return false;
    }

    int cnt = 0;
    for (int i = 0; i < nh; i++) {
        uint32_t y0 = (uint32_t)((uint64_t)i * b.h / nh);
        uint32_t y1 = (uint32_t)((uint64_t)(i + 1) * b.h / nh);
        uint32_t th = y1 - y0;

        for (int j = 0; j < nw; j++) {
            uint32_t x0 = (uint32_t)((uint64_t)j * b.w / nw);
            uint32_t x1 = (uint32_t)((uint64_t)(j + 1) * b.w / nw);
            uint32_t tw = x1 - x0;

            uint64_t row = ((uint64_t)tw * b.bpp + 7) / 8;
            uint64_t outStride = (row + 3) / 4 * 4;
            uint64_t pix = outStride * th;
            uint64_t outSz = (uint64_t)b.off + pix;
            if (outSz > 0xFFFFFFFFu) {
                cerr << "Output file is too large\n";
                return false;
            }

            unsigned char *out = new unsigned char[(size_t)outSz]();
            memcpy(out, b.data, (size_t)b.off);

            p32(out + 2, (uint32_t)outSz);    // bfSize
            p32(out + 18, tw);                // biWidth
            p32(out + 22, th);                // biHeight, bottom-up
            p32(out + 34, (uint32_t)pix);     // biSizeImage

            for (uint32_t k = 0; k < th; k++) {
                uint32_t y = y0 + (th - 1 - k);   // output is bottom-up
                uint32_t sr = b.top ? y : (b.h - 1 - y);
                const unsigned char *src =
                    b.data + (size_t)b.off + (uint64_t)sr * b.stride;
                unsigned char *dst =
                    out + (size_t)b.off + (uint64_t)k * outStride;

                if (b.bpp >= 8 && b.bpp % 8 == 0) {
                    uint32_t bytes = b.bpp / 8;
                    memcpy(dst, src + (uint64_t)x0 * bytes,
                           (size_t)tw * bytes);
                } else {
                    for (uint32_t x = 0; x < tw; x++) {
                        uint32_t v = getbits(src,
                            (uint64_t)(x0 + x) * b.bpp, b.bpp);
                        putbits(dst, (uint64_t)x * b.bpp, b.bpp, v);
                    }
                }
            }

            string name = base + "_part" + to_string(++cnt) + ".bmp";
            if (!writefile(name, out, (uint32_t)outSz)) {
                cerr << "Cannot write " << name << '\n';
                delete[] out;
                return false;
            }
            delete[] out;
            cout << name << '\n';
        }
    }
    return true;
}

int main(int argc, char **argv) {
    if (argc == 2 &&
        (strcmp(argv[1], "-?") == 0 || strcmp(argv[1], "/?") == 0)) {
        show();
        return 0;
    }
    if (argc < 2) {
        show();
        return 1;
    }

    string path = argv[1];
    int nh = 1, nw = 1;
    bool hasH = false, hasW = false;

    for (int i = 2; i < argc; i++) {
        if (strcmp(argv[i], "-h") == 0) {
            if (i + 1 >= argc || !getnum(argv[i + 1], nh)) {
                cerr << "Invalid -h value\n";
                return 1;
            }
            hasH = true;
            i++;
        } else if (strcmp(argv[i], "-w") == 0) {
            if (i + 1 >= argc || !getnum(argv[i + 1], nw)) {
                cerr << "Invalid -w value\n";
                return 1;
            }
            hasW = true;
            i++;
        } else {
            cerr << "Unknown option: " << argv[i] << '\n';
            show();
            return 1;
        }
    }

    if (!hasH && !hasW) {
        cerr << "Please specify -h and/or -w\n";
        show();
        return 1;
    }

    BMP b;
    if (!readfile(path, b.data, b.sz)) {
        cerr << "Cannot read file: " << path << '\n';
        return 1;
    }
    if (!parse(b)) {
        cerr << "Unsupported or invalid BMP file\n";
        delete[] b.data;
        return 1;
    }

    bool ok = split(b, nh, nw, basename(path));
    delete[] b.data;
    return ok ? 0 : 1;
}
