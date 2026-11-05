#include <cctype>
#include <iostream>
#include <string>

static bool is_digits(const std::string &s)
{
    if (s.empty())
        return false;

    for (std::string::size_type i = 0; i < s.size(); ++i) {
        if (!std::isdigit(static_cast<unsigned char>(s[i])))
            return false;
    }
    return true;
}

static void reverse_string(std::string &s)
{
    for (std::string::size_type i = 0; i < s.size() / 2; ++i) {
        const char tmp = s[i];
        s[i] = s[s.size() - 1 - i];
        s[s.size() - 1 - i] = tmp;
    }
}

std::string add_strings(const std::string &a, const std::string &b)
{
    if (!is_digits(a) || !is_digits(b))
        return "";

    std::string result;
    int i = static_cast<int>(a.size()) - 1;
    int j = static_cast<int>(b.size()) - 1;
    int carry = 0;

    while (i >= 0 || j >= 0 || carry != 0) {
        int sum = carry;

        if (i >= 0)
            sum += a[i--] - '0';
        if (j >= 0)
            sum += b[j--] - '0';

        result.push_back(static_cast<char>('0' + sum % 10));
        carry = sum / 10;
    }

    reverse_string(result);

    std::string::size_type first = 0;
    while (first + 1 < result.size() && result[first] == '0')
        ++first;

    return result.substr(first);
}

std::string increase_numbers(const std::string &sentence)
{
    std::string result;
    result.reserve(sentence.size());

    std::string::size_type i = 0;
    while (i < sentence.size()) {
        if (std::isdigit(static_cast<unsigned char>(sentence[i]))) {
            const std::string::size_type start = i;

            while (i < sentence.size() &&
                   std::isdigit(static_cast<unsigned char>(sentence[i]))) {
                ++i;
            }

            const std::string number = sentence.substr(start, i - start);
            const std::string incremented = add_strings(number, "1");
            result += incremented.empty() ? number : incremented;
        } else {
            result.push_back(sentence[i]);
            ++i;
        }
    }

    return result;
}

int main()
{
    std::string sentence;

    std::cout << "Enter a sentence = ";
    if (!std::getline(std::cin, sentence)) {
        std::cerr << "Input error.\n";
        return 1;
    }

    if (!sentence.empty() && sentence[sentence.size() - 1] == '\r')
        sentence.erase(sentence.size() - 1);

    std::cout << increase_numbers(sentence) << '\n';
    return 0;
}
