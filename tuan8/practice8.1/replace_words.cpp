#include "replace_words.h"

std::string replace_all(const std::string& source,
                        const std::string& find,
                        const std::string& replace)
{
    std::string result;

    for (int p = source.find(find, 0), prev = 0; p != -1;
         prev = p + find.size(), p = source.find(find, p + 1))
    {
        if (p != prev)
            result.append(source, prev, p - prev);
        result += replace;
    }
    return result;
}
