#include "paragraph.h"

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

bool read_paragraph(std::istream &input, std::string &paragraph)
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
