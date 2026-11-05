#include <iostream>
#include <string>

static bool ends_with_period(const std::string &line)
{
    for (int i = static_cast<int>(line.size()) - 1; i >= 0; --i) {
        const char c = line[i];

        if (c == ' ' || c == '\t' || c == '\r')
            continue;

        return c == '.';
    }

    return false;
}

static bool read_paragraph(std::istream &input, std::string &paragraph)
{
    paragraph.clear();
    std::string line;
    bool first_line = true;

    while (std::getline(input, line)) {
        if (!line.empty() && line[line.size() - 1] == '\r')
            line.erase(line.size() - 1);

        if (!first_line)
            paragraph.push_back('\n');

        paragraph += line;
        first_line = false;

        if (ends_with_period(line))
            return true;
    }

    return false;
}

int main()
{
    std::string paragraph;

    std::cout << "Enter a paragraph (end with '.'):\n";
    const bool terminated = read_paragraph(std::cin, paragraph);

    std::cout << paragraph << '\n';

    if (!terminated) {
        std::cerr << "Input ended before a line ending with '.'.\n";
        return 1;
    }

    return 0;
}
