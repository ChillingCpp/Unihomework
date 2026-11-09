#include "replace_words.h"

std::string replace_all(const std::string& source,
                        const std::string& find,
                        const std::string& replace)
{
    if (find.empty())
        return source;
    std::string result;

    std::string::size_type prev = 0;
    for (std::string::size_type p = source.find(find, 0); p != std::string::npos;
         prev = p + find.size(), p = source.find(find, prev))
    {
        if (p != prev)
            result.append(source, prev, p - prev);
        result += replace;
    }
    result.append(source, prev, source.size() - prev);
    return result;
}
