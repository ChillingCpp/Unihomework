#include <iostream>
#include <string>

static void strip_cr(std::string &s)
{
    if (!s.empty() && s[s.size() - 1] == '\r')
        s.erase(s.size() - 1);
}

static std::string replace_all(const std::string &source,
                               const std::string &find,
                               const std::string &replace)
{
    if (find.empty())
        return source;

    std::string result;
    std::string::size_type start = 0;

    while (true) {
        const std::string::size_type pos = source.find(find, start);
        if (pos == std::string::npos) {
            result.append(source, start, std::string::npos);
            break;
        }

        result.append(source, start, pos - start);
        result += replace;
        start = pos + find.size();
    }

    return result;
}

int main()
{
    std::string sentence;
    std::string find_word;
    std::string replace_word;

    std::cout << "Enter a sentence = ";
    if (!std::getline(std::cin, sentence)) {
        std::cerr << "Input error.\n";
        return 1;
    }

    std::cout << "Enter find word = ";
    if (!std::getline(std::cin, find_word)) {
        std::cerr << "Input error.\n";
        return 1;
    }

    std::cout << "Enter replacing word = ";
    if (!std::getline(std::cin, replace_word)) {
        std::cerr << "Input error.\n";
        return 1;
    }

    strip_cr(sentence);
    strip_cr(find_word);
    strip_cr(replace_word);

    if (find_word.empty()) {
        std::cerr << "Find word must not be empty.\n";
        return 1;
    }

    std::cout << replace_all(sentence, find_word, replace_word) << '\n';
    return 0;
}
