#include <cctype>
#include <iostream>
#include <string>
#include <algorithm>
#include <utility>

static void reverse_string(std::string& s)
{
    for (std::string::size_type i = 0; i < s.size() / 2; ++i)
        std::swap(s[i], s[s.size() - i - 1]);
}

std::string add_strings(const std::string& t)
{
    std::string res;
    int         c = 1;
    for (int i = t.size() - 1; i >= 0; --i)
    {
        if (t[i] - '0' + c == 10)
            res.push_back('0'), c = 1;
        else
            res.push_back((char) t[i] + c), c = 0;
    }
    if (c)
        res.push_back('1');
    std::reverse(res.begin(), res.end());
    return res;
}

std::string increase_numbers(const std::string& sentence)
{
    std::string result;
    result.reserve(sentence.size());

    std::string::size_type i = 0;
    for (int i = 0; i < sentence.size(); ++i)
    {
        if (std::isdigit(static_cast<unsigned char>(sentence[i])))
        {
            const std::string::size_type start = i;

            while (i < sentence.size() && std::isdigit(static_cast<unsigned char>(sentence[i])))
                i++;
            const std::string number      = sentence.substr(start, i - start);
            const std::string incremented = add_strings(number);
            result += incremented;
            i--;
        }
        else
            result.push_back(sentence[i]);
    }

    return result;
}

int main()
{
    std::string sentence;

    std::cout << "Enter a sentence = ";
    if (!std::getline(std::cin, sentence))
    {
        std::cerr << "Input error.\n";
        return 1;
    }

    if (!sentence.empty() && sentence[sentence.size() - 1] == '\r')
        sentence.erase(sentence.size() - 1);

    std::cout << increase_numbers(sentence) << '\n';
    return 0;
}
