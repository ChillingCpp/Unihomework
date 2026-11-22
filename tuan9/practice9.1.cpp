#include <cstring>
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>


bool same(const std::string &a, const std::string &b) {
    return a == b;
}

void trim(std::string& a){
    while (a.size() && a.back() == ' ') a.pop_back();
    std::reverse(a.begin(), a.end());
    while (a.size() && a.back() == ' ') a.pop_back();
    std::reverse(a.begin(), a.end());
}
void show() {
    std::cout << "COPY - copy files in binary mode\n\n";
    std::cout << "COPY <source> <destination>\n";
    std::cout << "COPY <source> <destination-path>/\n";
    std::cout << "COPY <file1> + <file2> <destination>\n";
    std::cout << "COPY -?\n";
}

// Copy s to d. If app is true, append to d instead of truncating it.
bool cp(const std::string &s, const std::string &d, bool app) {
    if (same(s, d)) {
        std::cerr << "Source and destination are the same file\n";
        return false;
    }

    std::ifstream f(s, std::ios::binary);
    if (!f) {
        std::cerr << "Cannot open source: " << s << '\n';
        return false;
    }

    std::ios::openmode mode = std::ios::binary | (app ? std::ios::app : std::ios::trunc);
    std::ofstream g(d, mode);
    if (!g) {
        std::cerr << "Cannot open destination: " << d << '\n';
        return false;
    }

    char buf[64 * 1024];
    bool ok = true;
    int BUF = 1 << 16;
    while (f) {
        f.read(buf, BUF);
        std::streamsize n = f.gcount();
        if (n > 0) {
            g.write(buf, n);
            if (!g) {
                ok = false;
                break;
            }
        }
    }

    if (f.bad()) ok = false;
    g.close();
    if (!g) ok = false;

    if (!ok) std::cerr << "Copy failed: " << s << " -> " << d << '\n';
    return ok;
}

bool join(std::string a, std::string b, std::string d) {
    trim(a);
    trim(b);
    trim(d);
    if (same(a, d) || same(b, d)) {
        std::cerr << "Destination must differ from both sources\n";
        return false;
    }

    if (!cp(a, d, false)){ 
        remove(d.c_str());
        return false;
    }
    if (!cp(b, d, true)) {
        remove(d.c_str());
        return false;
    }
    return true;
}

int main(int argc, char *argv[]) {
    if (argc == 2 &&
        (strcmp(argv[1], "-?") == 0 || strcmp(argv[1], "/?") == 0)) {
        show();
        return 0;
    }

    // Syntax 3: COPY <file1> + <file2> <destination>
    if (argc == 5 && strcmp(argv[2], "+") == 0) {
        return !join(argv[1], argv[3], argv[4]);
    }

    // Syntax 1 and 2: COPY <source> <destination>
    if (argc == 3) {
        std::string s = argv[1];
        std::string d = argv[2];

        trim(s);
        trim(d);
        bool slash = !d.empty() && (d.back() == '/' || d.back() == '\\');
        if (slash) {
            // Keep the source filename when copying into a directory.
            int p = s.find_last_of("/\\") + 1;
            if (p == std::string::npos) p = 0;
            d.append(s, p, s.size()-p);    
        }
        return !cp(s, d, false);
    }

    show();
    return 1;
}
