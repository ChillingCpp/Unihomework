#include "big_number.h"

#include <cctype>

std::string add_strings(const std::string& t)
{
    std::string res;
    int         c = 1;
    for (int i = t.size() - 1; i >= 0; --i)
    {
        if (t[i] - '0' + c == 10)
            res.push_back('0'), c = 1;
        else
            res.push_back(static_cast<char>(t[i] + c)), c = 0;
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

    for (int i = 0; i < sentence.size(); ++i)
    {
        if (std::isdigit(static_cast<char>(sentence[i])))
        {
            const std::string::size_type start = i;

            while (i < sentence.size() && std::isdigit(static_cast<char>(sentence[i])))
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
