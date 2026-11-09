#include <iostream>
#include <string>

#include "replace_words.h"

static void strip_cr(std::string& s)
{
    if (!s.empty() && s.back() == '\r')
        s.pop_back();
}

int main()
{
    std::string sentence;
    std::string find_word;
    std::string replace_word;

    std::cout << "Enter a sentence = ";
    if (!std::getline(std::cin, sentence))
    {
        std::cerr << "Input error.\n";
        return 1;
    }

    std::cout << "Enter find word = ";
    if (!std::getline(std::cin, find_word))
    {
        std::cerr << "Input error.\n";
        return 1;
    }

    std::cout << "Enter replacing word = ";
    if (!std::getline(std::cin, replace_word))
    {
        std::cerr << "Input error.\n";
        return 1;
    }

    strip_cr(sentence);
    strip_cr(find_word);
    strip_cr(replace_word);

    if (find_word.empty())
    {
        std::cerr << "Find word must not be empty.\n";
        return 1;
    }

    std::cout << replace_all(sentence, find_word, replace_word) << '\n';
    return 0;
}
