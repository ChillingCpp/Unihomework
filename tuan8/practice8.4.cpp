#include <iostream>

static int matrix_value(int (*matrix)[6], int row, int column)
{
    return *(*(matrix + row) + column);
}

int main()
{
    int m[4][6];

    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 6; ++j)
            m[i][j] = 10 * i + j;
    }

    std::cout << "m[2][4] = " << matrix_value(m, 2, 4) << '\n';
    return 0;
}
