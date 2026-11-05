#include "matrix_access.h"

int matrix_value(int (*matrix)[6], int row, int column)
{
    return *(*(matrix + row) + column);
}
