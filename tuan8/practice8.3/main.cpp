#include <iostream>
#include <string>

#include "paragraph.h"

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
