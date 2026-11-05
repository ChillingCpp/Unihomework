#include "replace_words.h"

std::string replace_all(const std::string &source,
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
