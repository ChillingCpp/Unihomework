#include <iostream>
#include <string>

#include "big_number.h"

int main()
{
    std::string sentence;

    std::cout << "Enter a sentence = ";
    if (!std::getline(std::cin, sentence))
    {
        std::cerr << "Input error.\n";
        return 1;
    }

    if (!sentence.empty() && sentence.back() == '\r')
        sentence.pop_back();

    std::cout << increase_numbers(sentence) << '\n';
    return 0;
}
