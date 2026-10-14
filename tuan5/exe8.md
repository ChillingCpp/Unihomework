# Đáp án bài tập exe8.pdf - Chapter 8 Arrays

## Exercises - Section 8.1 - Bài 1

**Đề bài:**
We discussed using the expression `sizeof(a) / sizeof(a[0])` to calculate the number of elements in an array. The expression `sizeof(a) / sizeof(t)`, where `t` is the type of a's elements, would also work, but it's considered an inferior technique. Why?

**Đáp án:**
Vì `sizeof(a) / sizeof(t)` yêu cầu phải biết và ghi rõ kiểu phần tử. Nếu kiểu phần tử của mảng bị thay đổi sau này mà không cập nhật `t`, biểu thức sẽ cho kết quả sai. Còn `sizeof(a) / sizeof(a[0])` tự động lấy đúng kích thước phần tử hiện tại, không bị trùng lặp thông tin về kiểu, nên an toàn và dễ bảo trì hơn.

## Exercises - Section 8.1 - Bài 2

**Đề bài:**
The Q&A section shows how to use a *letter* as an array subscript. Describe how to use a *digit* (in character form) as a subscript.

**Đáp án:**
Dùng hiệu `ch - '0'` làm chỉ số, với `ch` là ký tự chữ số từ `'0'` đến `'9'`. Ví dụ: `count[ch - '0']`. Vì các mã ký tự `'0'` đến `'9'` liên tiếp nhau, hiệu này cho giá trị 0 đến 9 tương ứng với chữ số.

## Exercises - Section 8.1 - Bài 3

**Đề bài:**
Write a declaration of an array named `weekend` containing seven `bool` values. Include an initializer that makes the first and last values `true`; all other values should be `false`.

**Đáp án:**
```c
#include <stdbool.h>
bool weekend[7] = {true, false, false, false, false, false, true};
```

## Exercises - Section 8.1 - Bài 4

**Đề bài:**
(C99) Repeat Exercise 3, but this time use a designated initializer. Make the initializer as short as possible.

**Đáp án:**
```c
#include <stdbool.h>
bool weekend[7] = {[0] = true, [6] = true};
```

## Exercises - Section 8.1 - Bài 5

**Đề bài:**
The Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, ..., where each number is the sum of the two preceding numbers. Write a program fragment that declares an array named `fib_numbers` of length 40 and fills the array with the first 40 Fibonacci numbers. *Hint:* Fill in the first two numbers individually, then use a loop to compute the remaining numbers.

**Đáp án:**
```c
int fib_numbers[40];
fib_numbers[0] = 0;
fib_numbers[1] = 1;
for (int i = 2; i < 40; i++)
    fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2];
```

## Exercises - Section 8.2 - Bài 6

**Đề bài:**
Calculators, watches, and other electronic devices often rely on seven-segment displays for numerical output. To form a digit, such devices "turn on" some of the seven segments while leaving others "off". Suppose that we want to set up an array that remembers which segments should be "on" for each digit. Let's number the segments as follows:
```
  0
5| |1
  6
4| |2
  3
```
Here's what the array might look like, with each row representing one digit:
```c
const int segments[10][7] = {{1, 1, 1, 1, 1, 1, 0}, ...};
```
I've given you the first row of the initializer; fill in the rest.

**Đáp án:**
```c
const int segments[10][7] = {
    {1, 1, 1, 1, 1, 1, 0},
    {0, 1, 1, 0, 0, 0, 0},
    {1, 1, 0, 1, 1, 0, 1},
    {1, 1, 1, 1, 0, 0, 1},
    {0, 1, 1, 0, 0, 1, 1},
    {1, 0, 1, 1, 0, 1, 1},
    {1, 0, 1, 1, 1, 1, 1},
    {1, 1, 1, 0, 0, 0, 0},
    {1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 0, 1, 1}
};
```

## Exercises - Section 8.2 - Bài 7

**Đề bài:**
Using the shortcuts described in Section 8.2, shrink the initializer for the `segments` array (Exercise 6) as much as you can.

**Đáp án:**
```c
const int segments[10][7] = {
    {1, 1, 1, 1, 1, 1},
    {0, 1, 1},
    {1, 1, 0, 1, 1, 0, 1},
    {1, 1, 1, 1, 0, 0, 1},
    {0, 1, 1, 0, 0, 1, 1},
    {1, 0, 1, 1, 0, 1, 1},
    {1, 0, 1, 1, 1, 1, 1},
    {1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 0, 1, 1}
};
```

## Exercises - Section 8.2 - Bài 8

**Đề bài:**
Write a declaration for a two-dimensional array named `temperature_readings` that stores one month of hourly temperature readings. (For simplicity, assume that a month has 30 days.) The rows of the array should represent days of the month; the columns should represent hours of the day.

**Đáp án:**
```c
int temperature_readings[30][24];
```

## Exercises - Section 8.2 - Bài 9

**Đề bài:**
Using the array of Exercise 8, write a program fragment that computes the average temperature for a month (averaged over all days of the month and all hours of the day).

**Đáp án:**
```c
int sum = 0;
for (int i = 0; i < 30; i++)
    for (int j = 0; j < 24; j++)
        sum += temperature_readings[i][j];
double average = sum / (30.0 * 24.0);
```

## Exercises - Section 8.2 - Bài 10

**Đề bài:**
Write a declaration for an 8 x 8 `char` array named `chess_board`. Include an initializer that puts the following data into the array (one character per array element):
```
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
```

**Đáp án:**
```c
char chess_board[8][8] = {
    {'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'},
    {'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'},
    {'.', '.', '.', '.', '.', '.', '.', '.'},
    {'.', '.', '.', '.', '.', '.', '.', '.'},
    {'.', '.', '.', '.', '.', '.', '.', '.'},
    {'.', '.', '.', '.', '.', '.', '.', '.'},
    {'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'},
    {'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'}
};
```

## Exercises - Section 8.2 - Bài 11

**Đề bài:**
Write a program fragment that declares an 8 x 8 `char` array named `checker_board` and then uses a loop to store the following data into the array (one character per array element):
```
B R B R B R B R
R B R B R B R B
B R B R B R B R
R B R B R B R B
B R B R B R B R
R B R B R B R B
B R B R B R B R
R B R B R B R B
Hint: The element in row i, column j, should be the letter B if i + j is an even number.
```

**Đáp án:**
```c
char checker_board[8][8];
for (int i = 0; i < 8; i++)
    for (int j = 0; j < 8; j++)
        if ((i + j) % 2 == 0)
            checker_board[i][j] = 'B';
        else
            checker_board[i][j] = 'R';
```

## Programming Projects - Bài 1

**Đề bài:**
Modify the `repdigit.c` program of Section 8.1 so that it shows which digits (if any) were repeated:
```
Enter a number: 939577
Repeated digit(s): 7 9
```

**Đáp án:**
```c
#include <stdio.h>

int main(void)
{
    long n;
    int digit_seen[10] = {0};

    printf("Enter a number: ");
    scanf("%ld", &n);

    if (n < 0)
        n = -n;
    if (n == 0)
        digit_seen[0] = 1;

    while (n > 0) {
        digit_seen[n % 10]++;
        n /= 10;
    }

    printf("Repeated digit(s):");
    for (int i = 0; i < 10; i++)
        if (digit_seen[i] > 1)
            printf(" %d", i);
    printf("\n");

    return 0;
}
```

## Programming Projects - Bài 2

**Đề bài:**
Modify the `repdigit.c` program of Section 8.1 so that it prints a table showing how many times each digit appears in the number:
```
Enter a number: 41271092
Digit:         0  1  2  3  4  5  6  7  8  9
Occurrences:   1  2  2  0  1  0  0  1  0  1
```

**Đáp án:**
```c
#include <stdio.h>

int main(void)
{
    long n;
    int occurrences[10] = {0};

    printf("Enter a number: ");
    scanf("%ld", &n);

    if (n < 0)
        n = -n;
    if (n == 0)
        occurrences[0] = 1;

    while (n > 0) {
        occurrences[n % 10]++;
        n /= 10;
    }

    printf("Digit:        ");
    for (int i = 0; i < 10; i++)
        printf("%3d", i);
    printf("\nOccurrences:  ");
    for (int i = 0; i < 10; i++)
        printf("%3d", occurrences[i]);
    printf("\n");

    return 0;
}
```

## Programming Projects - Bài 3

**Đề bài:**
Modify the `repdigit.c` program of Section 8.1 so that the user can enter more than one number to be tested for repeated digits. The program should terminate when the user enters a number that's less than or equal to 0.

**Đáp án:**
```c
#include <stdbool.h>
#include <stdio.h>

int main(void)
{
    long n;

    for (;;) {
        int digit_seen[10] = {0};
        bool repeated = false;

        printf("Enter a number: ");
        scanf("%ld", &n);
        if (n <= 0)
            break;

        while (n > 0) {
            int d = n % 10;
            if (digit_seen[d]) {
                repeated = true;
                break;
            }
            digit_seen[d] = 1;
            n /= 10;
        }

        if (repeated)
            printf("Repeated digit\n");
        else
            printf("No repeated digit\n");
    }

    return 0;
}
```

## Programming Projects - Bài 4

**Đề bài:**
Modify the `reverse.c` program of Section 8.1 to use the expression `(int)(sizeof(a) / sizeof(a[0]))` (or a macro with this value) for the array length.

**Đáp án:**
```c
#include <stdio.h>

int main(void)
{
    int a[10];

    int len = (int)(sizeof(a) / sizeof(a[0]));

    printf("Enter %d numbers: ", len);
    for (int i = 0; i < len; i++)
        scanf("%d", &a[i]);

    printf("In reverse order:");
    for (int i = len - 1; i >= 0; i--)
        printf(" %d", a[i]);
    printf("\n");

    return 0;
}
```

## Programming Projects - Bài 5

**Đề bài:**
Modify the `interest.c` program of Section 8.1 so that it compounds interest *monthly* instead of *annually*. The form of the output shouldn't change; the balance should still be shown at annual intervals.

**Đáp án:**
```c
#include <stdio.h>

#define NUM_RATES 5
#define INITIAL_BALANCE 100.00

int main(void)
{
    int low_rate, num_years;
    double value[NUM_RATES];

    printf("Enter interest rate: ");
    scanf("%d", &low_rate);
    printf("Enter number of years: ");
    scanf("%d", &num_years);

    printf("\nYears");
    for (int i = 0; i < NUM_RATES; i++) {
        printf("%6d%%", low_rate + i);
        value[i] = INITIAL_BALANCE;
    }
    printf("\n");

    for (int year = 1; year <= num_years; year++) {
        printf("%3d    ", year);
        for (int i = 0; i < NUM_RATES; i++) {
            for (int month = 0; month < 12; month++)
                value[i] += value[i] * (low_rate + i) / 100.0 / 12.0;
            printf(" %7.2f", value[i]);
        }
        printf("\n");
    }

    return 0;
}
```

## Programming Projects - Bài 6

**Đề bài:**
The prototypical Internet newbie is a fellow named B1FF, who has a unique way of writing messages. Here's a typical B1FF communique:
```
H3Y DUD3, C 15 R1LLY C00L!!!!!!!!!!
```
Write a "B1FF filter" that reads a message entered by the user and translates it into B1FF-speak:
```
Enter message: Hey dude, C is rilly cool
In B1FF-speak: H3Y DUD3, C 15 R1LLY C00L!!!!!!!!!!
```
Your program should convert the message to upper-case letters, substitute digits for certain letters (A->4, B->8, E->3, I->1, O->0, S->5), and then append 10 or so exclamation marks. *Hint:* Store the original message in an array of characters, then go back through the array, translating and printing characters one by one.

**Đáp án:**
```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char msg[1000];
    int n = 0;
    int ch;

    printf("Enter message: ");
    while ((ch = getchar()) != '\n' && ch != EOF && n < 1000)
        msg[n++] = (char) ch;

    printf("In B1FF-speak: ");
    for (int i = 0; i < n; i++) {
        char c = toupper((unsigned char)msg[i]);
        switch (c) {
            case 'A': putchar('4'); break;
            case 'B': putchar('8'); break;
            case 'E': putchar('3'); break;
            case 'I': putchar('1'); break;
            case 'O': putchar('0'); break;
            case 'S': putchar('5'); break;
            default: putchar(c); break;
        }
    }
    for (int i = 0; i < 10; i++)
        putchar('!');
    printf("\n");

    return 0;
}
```

## Programming Projects - Bài 7

**Đề bài:**
Write a program that reads a 5 x 5 array of integers and then prints the row sums and the column sums:
```
Enter row 1: 8 3 9 0 10
Enter row 2: 3 5 17 1 1
Enter row 3: 2 8 6 23 1
Enter row 4: 15 7 3 2 9
Enter row 5: 6 14 2 6 0
Row totals: 30 27 40 36 28
Column totals: 34 37 37 32 21
```

**Đáp án:**
```c
#include <stdio.h>

int main(void)
{
    int a[5][5];
    int row_sum[5] = {0};
    int col_sum[5] = {0};

    for (int i = 0; i < 5; i++) {
        printf("Enter row %d: ", i + 1);
        for (int j = 0; j < 5; j++) {
            scanf("%d", &a[i][j]);
            row_sum[i] += a[i][j];
            col_sum[j] += a[i][j];
        }
    }

    printf("Row totals:");
    for (int i = 0; i < 5; i++)
        printf(" %d", row_sum[i]);
    printf("\nColumn totals:");
    for (int j = 0; j < 5; j++)
        printf(" %d", col_sum[j]);
    printf("\n");

    return 0;
}
```

## Programming Projects - Bài 8

**Đề bài:**
Modify Programming Project 7 so that it prompts for five quiz grades for each of five students, then computes the total score and average score for each *student*, and the average score, high score, and low score for each *quiz*.

**Đáp án:**
```c
#include <stdio.h>

int main(void)
{
    int grades[5][5];

    for (int i = 0; i < 5; i++) {
        printf("Enter grades for student %d: ", i + 1);
        for (int j = 0; j < 5; j++)
            scanf("%d", &grades[i][j]);
    }

    for (int i = 0; i < 5; i++) {
        int total = 0;
        for (int j = 0; j < 5; j++)
            total += grades[i][j];
        printf("Student %d: total %d, average %.1f\n",
               i + 1, total, total / 5.0);
    }

    for (int j = 0; j < 5; j++) {
        int sum = 0, high = grades[0][j], low = grades[0][j];
        for (int i = 0; i < 5; i++) {
            sum += grades[i][j];
            if (grades[i][j] > high)
                high = grades[i][j];
            if (grades[i][j] < low)
                low = grades[i][j];
        }
        printf("Quiz %d: average %.1f, high %d, low %d\n",
               j + 1, sum / 5.0, high, low);
    }

    return 0;
}
```

## Programming Projects - Bài 9

**Đề bài:**
Write a program that generates a "random walk" across a 10 x 10 array. The array will contain characters (all '.' initially). The program must randomly "walk" from element to element, always going up, down, left, or right by one element. The elements visited by the program will be labeled with the letters A through Z, in the order visited. Here's an example of the desired output:
```
A . . . . . . . . .
B C D . . . . . . .
. F E . . . . . . .
H G . . . . . . . .
I . . . . . . . . .
J . . . . . . Z . .
K . . R S T U V Y .
L M P Q . . . W X .
. N O . . . . . . .
. . . . . . . . . .
```
*Hint:* Use the `srand` and `rand` functions (see `deal.c`) to generate random numbers. After generating a number, look at its remainder when divided by 4. There are four possible values for the remainder-0, 1, 2, and 3-indicating the direction of the next move. Before performing a move, check that (a) it won't go outside the array, and (b) it doesn't take us to an element that already has a letter assigned. If either condition is violated, try moving in another direction. If all four directions are blocked, the program must terminate. Here's an example of premature termination:
```
A B G H I . . . . .
. C F . J K . . . .
. D E . M L . . . .
. . . . N O . . . .
. . W X Y P Q . . .
. . V U T S R . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
Y is blocked on all four sides, so there's no place to put Z.
```

**Đáp án:**
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    char board[10][10];
    for (int i = 0; i < 10; i++)
        for (int j = 0; j < 10; j++)
            board[i][j] = '.';

    srand((unsigned) time(NULL));

    int r = 0, c = 0;
    board[r][c] = 'A';

    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, 1, -1};

    for (char step = 'B'; step <= 'Z'; step++) {
        int tried[4] = {0, 0, 0, 0};
        int tried_count = 0;
        int moved = 0;

        while (tried_count < 4) {
            int dir = rand() % 4;
            if (tried[dir])
                continue;
            tried[dir] = 1;
            tried_count++;

            int nr = r + dr[dir];
            int nc = c + dc[dir];
            if (nr < 0 || nr > 9 || nc < 0 || nc > 9)
                continue;
            if (board[nr][nc] != '.')
                continue;
            r = nr;
            c = nc;
            board[r][c] = step;
            moved = 1;
            break;
        }
        if (!moved)
            break;
    }

    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++)
            printf("%c ", board[i][j]);
        printf("\n");
    }

    return 0;
}
```

## Programming Projects - Bài 10

**Đề bài:**
Modify Programming Project 8 from Chapter 5 so that the departure times are stored in an array and the arrival times are stored in a second array. (The times are integers, representing the number of minutes since midnight.) The program will use a loop to search the array of departure times for the one closest to the time entered by the user.

**Đáp án:**
```c
#include <stdio.h>

int main(void)
{
    int departures[8] = {480, 583, 679, 767, 840, 945, 1140, 1305};
    int arrivals[8] = {616, 712, 811, 900, 968, 1075, 1280, 1438};

    int h, m;
    printf("Enter a 24-hour time: ");
    scanf("%d:%d", &h, &m);
    int t = h * 60 + m;

    int best = 0;
    int best_diff = 1440;
    for (int i = 0; i < 8; i++) {
        int diff = departures[i] - t;
        if (diff < 0)
            diff = -diff;
        if (diff < best_diff) {
            best_diff = diff;
            best = i;
        }
    }

    int d = departures[best];
    int a = arrivals[best];
    int dh = (((d / 60) + 11) % 12) + 1;
    int ah = (((a / 60) + 11) % 12) + 1;
    const char *ds = d < 720 ? "a.m." : "p.m.";
    const char *as = a < 720 ? "a.m." : "p.m.";
    int dm = d % 60;
    int am = a % 60;

    printf("Closest departure time is %d:%.2d %s, arriving at %d:%.2d %s\n",
           dh, dm, ds, ah, am, as);

    return 0;
}
```

## Programming Projects - Bài 11

**Đề bài:**
Modify Programming Project 4 from Chapter 7 so that the program labels its output:
```
Enter phone number: 1-800-COL-LECT
In numeric form: 1-800-265-5328
```
The program will need to store the phone number (either in its original form or in its numeric form) in an array of characters until it can be printed. You may assume that the phone number is no more than 15 characters long.

**Đáp án:**
```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char phone[16];
    int n = 0;
    int ch;

    printf("Enter phone number: ");
    while ((ch = getchar()) != '\n' && ch != EOF && n < 15)
        phone[n++] = (char) ch;
    phone[n] = '\0';

    printf("In numeric form: ");
    for (int i = 0; i < n; i++) {
        char c = toupper((unsigned char)phone[i]);
        switch (c) {
            case 'A': case 'B': case 'C': putchar('2'); break;
            case 'D': case 'E': case 'F': putchar('3'); break;
            case 'G': case 'H': case 'I': putchar('4'); break;
            case 'J': case 'K': case 'L': putchar('5'); break;
            case 'M': case 'N': case 'O': putchar('6'); break;
            case 'P': case 'R': case 'S': putchar('7'); break;
            case 'T': case 'U': case 'V': putchar('8'); break;
            case 'W': case 'X': case 'Y': putchar('9'); break;
            default: putchar(phone[i]); break;
        }
    }
    printf("\n");

    return 0;
}
```

## Programming Projects - Bài 12

**Đề bài:**
Modify Programming Project 5 from Chapter 7 so that the SCRABBLE values of the letters are stored in an array. The array will have 26 elements, corresponding to the 26 letters of the alphabet. For example, element 0 of the array will store 1 (because the SCRABBLE value of the letter A is 1), element 1 of the array will store 3 (because the SCRABBLE value of the letter B is 3), and so forth. As each character of the input word is read, the program will use the array to determine the SCRABBLE value of that character. Use an array initializer to set up the array.

**Đáp án:**
```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    int values[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
                      1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
    int sum = 0;
    int ch;

    printf("Enter a word: ");
    while ((ch = getchar()) != '\n' && ch != EOF) {
        if (isalpha(ch))
            sum += values[toupper(ch) - 'A'];
    }

    printf("Scrabble value: %d\n", sum);

    return 0;
}
```

## Programming Projects - Bài 13

**Đề bài:**
Modify Programming Project 11 from Chapter 7 so that the program labels its output:
```
Enter a first and last name: Lloyd Fosdick
You entered the name: Fosdick, L.
```
The program will need to store the last name (but not the first name) in an array of characters until it can be printed. You may assume that the last name is no more than 20 characters long.

**Đáp án:**
```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char last[21];
    int n = 0;
    int ch;
    char first_initial;

    printf("Enter a first and last name: ");
    scanf(" %c", &first_initial);
    while ((ch = getchar()) == ' ')
        ;
    while (ch != '\n' && ch != EOF && ch != ' ') {
        ch = getchar();
    }
    if (ch == ' ') {
        while ((ch = getchar()) == ' ')
            ;
    }
    while (ch != '\n' && ch != EOF && n < 20) {
        if (ch != ' ')
            last[n++] = (char) ch;
        ch = getchar();
    }
    last[n] = '\0';

    printf("You entered the name: %s, %c.\n", last, first_initial);

    return 0;
}
```

## Programming Projects - Bài 14

**Đề bài:**
Write a program that reverses the words in a sentence:
```
Enter a sentence: you can cage a swallow can't you?
Reversal of sentence: you can't swallow a cage can you?
```
*Hint:* Use a loop to read the characters one by one and store them in a one-dimensional `char` array. Have the loop stop at a period, question mark, or exclamation point (the "terminating character"), which is saved in a separate `char` variable. Then use a second loop to search backward through the array for the beginning of the last word. Print the last word, then search backward for the next-to-last word. Repeat until the beginning of the array is reached. Finally, print the terminating character.

**Đáp án:**
```c
#include <stdio.h>

int main(void)
{
    char sentence[1000];
    int n = 0;
    char term;
    int ch;

    printf("Enter a sentence: ");
    while ((ch = getchar()) != '.' && ch != '?' && ch != '!' && ch != EOF && n < 1000)
        sentence[n++] = (char) ch;
    term = (char) ch;

    printf("Reversal of sentence:");
    int end = n;
    while (end > 0) {
        while (end > 0 && sentence[end - 1] == ' ')
            end--;
        if (end == 0)
            break;
        int start = end;
        while (start > 0 && sentence[start - 1] != ' ')
            start--;
        printf(" ");
        for (int i = start; i < end; i++)
            putchar(sentence[i]);
        end = start;
    }
    printf("%c\n", term);

    return 0;
}
```

## Programming Projects - Bài 15

**Đề bài:**
One of the oldest known encryption techniques is the Caesar cipher, attributed to Julius Caesar. It involves replacing each letter in a message with another letter that is a fixed number of positions later in the alphabet. (If the replacement would go past the letter Z, the cipher "wraps around" to the beginning of the alphabet. For example, if each letter is replaced by the letter two positions after it, then Y would be replaced by A, and Z would be replaced by B.) Write a program that encrypts a message using a Caesar cipher. The user will enter the message to be encrypted and the shift amount (the number of positions by which letters should be shifted):
```
Enter message to be encrypted: Go ahead, make my day.
Enter shift amount (1-25): 3
Encrypted message: Jr dkhdg, pdnh pb gdb.
```
Notice that the program can decrypt a message if the user enters 26 minus the original key:
```
Enter message to be encrypted: Jr dkhdg, pdnh pb gdb.
Enter shift amount (1-25): 23
Encrypted message: Go ahead, make my day.
```
You may assume that the message does not exceed 80 characters. Characters other than letters should be left unchanged. Lower-case letters remain lower-case when encrypted, and upper-case letters remain upper-case. *Hint:* To handle the wrap-around problem, use the expression `((ch - 'A') + n) % 26 + 'A'` to calculate the encrypted version of an upper-case letter, where `ch` stores the letter and `n` stores the shift amount. (You'll need a similar expression for lower-case letters.)

**Đáp án:**
```c
#include <stdio.h>

int main(void)
{
    char msg[81];
    int n = 0;
    int shift;
    int ch;

    printf("Enter message to be encrypted: ");
    while ((ch = getchar()) != '\n' && ch != EOF && n < 80)
        msg[n++] = (char) ch;

    printf("Enter shift amount (1-25): ");
    scanf("%d", &shift);

    printf("Encrypted message: ");
    for (int i = 0; i < n; i++) {
        char c = msg[i];
        if (c >= 'A' && c <= 'Z')
            putchar((char)(((c - 'A') + shift) % 26 + 'A'));
        else if (c >= 'a' && c <= 'z')
            putchar((char)(((c - 'a') + shift) % 26 + 'a'));
        else
            putchar(c);
    }
    printf("\n");

    return 0;
}
```

## Programming Projects - Bài 16

**Đề bài:**
Write a program that tests whether two words are anagrams (permutations of the same letters):
```
Enter first word: smartest
Enter second word: mattress
The words are anagrams.
Enter first word: dumbest
Enter second word: stumble
The words are not anagrams.
```
Write a loop that reads the first word, character by character, using an array of 26 integers to keep track of how many times each letter has been seen. (For example, after the word *smartest* has been read, the array should contain the values 1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 1 2 2 0 0 0 0 0 0 0, reflecting the fact that *smartest* contains one *a*, one *e*, one *m*, one *r*, two *s*'s and two *t*'s.) Use another loop to read the second word, except this time decrementing the corresponding array element as each letter is read. Both loops should ignore any characters that aren't letters, and both should treat upper-case letters in the same way as lower-case letters. After the second word has been read, use a third loop to check whether all the elements in the array are zero. If so, the words are anagrams. *Hint:* You may wish to use functions from `<ctype.h>`, such as `isalpha` and `tolower`.

**Đáp án:**
```c
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>

int main(void)
{
    int counts[26] = {0};
    int ch;

    printf("Enter first word: ");
    while ((ch = getchar()) != '\n' && ch != EOF) {
        if (isalpha(ch))
            counts[tolower(ch) - 'a']++;
    }

    printf("Enter second word: ");
    while ((ch = getchar()) != '\n' && ch != EOF) {
        if (isalpha(ch))
            counts[tolower(ch) - 'a']--;
    }

    bool anagram = true;
    for (int i = 0; i < 26; i++) {
        if (counts[i] != 0) {
            anagram = false;
            break;
        }
    }

    if (anagram)
        printf("The words are anagrams.\n");
    else
        printf("The words are not anagrams.\n");

    return 0;
}
```

## Programming Projects - Bài 17

**Đề bài:**
Write a program that prints an *n* x *n* magic square (a square arrangement of the numbers 1, 2, ..., *n*² in which the sums of the rows, columns, and diagonals are all the same). The user will specify the value of *n*:
```
This program creates a magic square of a specified size.
The size must be an odd number between 1 and 99.
Enter size of magic square: 5
    17    24     1     8    15
    23     5     7    14    16
     4     6    13    20    22
    10    12    19    21     3
    11    18    25     2     9
```
Store the magic square in a two-dimensional array. Start by placing the number 1 in the middle of row 0. Place each of the remaining numbers 2, 3, ..., *n*² by moving up one row and over one column. Any attempt to go outside the bounds of the array should "wrap around" to the opposite side of the array. For example, instead of storing the next number in row -1, we would store it in row *n* - 1 (the last row). Instead of storing the next number in column *n*, we would store it in column 0. If a particular array element is already occupied, put the number directly below the previously stored number. If your compiler supports variable-length arrays, declare the array to have *n* rows and *n* columns. If not, declare the array to have 99 rows and 99 columns.

**Đáp án:**
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("This program creates a magic square of a specified size.\n");
    printf("The size must be an odd number between 1 and 99.\n");
    printf("Enter size of magic square: ");
    scanf("%d", &n);

    int square[99][99] = {{0}};

    int r = 0, c = n / 2;
    square[r][c] = 1;

    for (int k = 2; k <= n * n; k++) {
        int nr = (r - 1 + n) % n;
        int nc = (c + 1) % n;
        if (square[nr][nc] != 0) {
            r = (r + 1) % n;
        } else {
            r = nr;
            c = nc;
        }
        square[r][c] = k;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            printf("%5d", square[i][j]);
        printf("\n");
    }

    return 0;
}
```
