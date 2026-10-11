# Exercises — Chapter 16 Structures, Unions, and Enumerations (exe16.pdf)

*(Programming Projects skipped as requested.)*

## Exercise 1

Đề: In the following declarations, the x and y structures have members named x and y:

```c
struct { int x, y; } x;
struct { int x, y; } y;
```

Are these declarations legal on an individual basis? Could both declarations appear as shown in a program? Justify your answer.

Đáp án:

Cả hai khai báo đều hợp lệ riêng lẻ và có thể cùng xuất hiện, vì tên member nằm trong namespace riêng của từng struct còn x, y ngoài là hai biến khác nhau.

## Exercise 2 (W)

Đề:

```text
(a) Declare structure variables named c1, c2, and c3, each having members real and imaginary of type double.
(b) Modify the declaration in part (a) so that c1's members initially have the values 0.0 and 1.0, while c2's members are 1.0 and 0.0 initially. (c3 is not initialized.)
(c) Write statements that copy the members of c2 into c1. Can this be done in one statement, or does it require two?
(d) Write statements that add the corresponding members of c1 and c2, storing the result in c3.
```

Đáp án:

```c
(a) struct { double real, imaginary; } c1, c2, c3;

(b) struct { double real, imaginary; } c1 = {0.0, 1.0}, c2 = {1.0, 0.0}, c3;

(c) c1 = c2;

(d) c3.real = c1.real + c2.real;
    c3.imaginary = c1.imaginary + c2.imaginary;
```

## Exercise 3

Đề:

```text
(a) Show how to declare a tag named complex for a structure with two members, real and imaginary, of type double.
(b) Use the complex tag to declare variables named c1, c2, and c3.
(c) Write a function named make_complex that stores its two arguments (both of type double) in a complex structure, then returns the structure.
(d) Write a function named add_complex that adds the corresponding members of its arguments (both complex structures), then returns the result (another complex structure).
```

Đáp án:

```c
(a) struct complex { double real, imaginary; };

(b) struct complex c1, c2, c3;

(c) struct complex make_complex(double real, double imaginary)
    {
      struct complex c;
      c.real = real;
      c.imaginary = imaginary;
      return c;
    }

(d) struct complex add_complex(struct complex c1, struct complex c2)
    {
      struct complex c;
      c.real = c1.real + c2.real;
      c.imaginary = c1.imaginary + c2.imaginary;
      return c;
    }
```

## Exercise 4 (W)

Đề: Repeat Exercise 3, but this time using a type named Complex.

Đáp án:

```c
typedef struct { double real, imaginary; } Complex;

Complex c1, c2, c3;

Complex make_complex(double real, double imaginary)
{
  Complex c;
  c.real = real;
  c.imaginary = imaginary;
  return c;
}

Complex add_complex(Complex c1, Complex c2)
{
  Complex c;
  c.real = c1.real + c2.real;
  c.imaginary = c1.imaginary + c2.imaginary;
  return c;
}
```

## Exercise 5

Đề: Write the following functions, assuming that the date structure contains three members: month, day, and year (all of type int).

```text
(a) int day_of_year(struct date d);
Returns the day of the year (an integer between 1 and 366) that corresponds to the date d.
(b) int compare_dates(struct date d1, struct date d2);
Returns -1 if d1 is an earlier date than d2, +1 if d1 is a later date than d2, and 0 if d1 and d2 are the same.
```

Đáp án:

```c
int day_of_year(struct date d)
{
  int t[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  int i, s = 0;
  if ((d.year % 4 == 0 && d.year % 100 != 0) || d.year % 400 == 0)
    t[1] = 29;
  for (i = 0; i < d.month - 1; i++)
    s += t[i];
  return s + d.day;
}

int compare_dates(struct date d1, struct date d2)
{
  if (d1.year != d2.year)
    return d1.year < d2.year ? -1 : 1;
  if (d1.month != d2.month)
    return d1.month < d2.month ? -1 : 1;
  if (d1.day != d2.day)
    return d1.day < d2.day ? -1 : 1;
  return 0;
}
```

## Exercise 6

Đề: Write the following function, assuming that the time structure contains three members: hours, minutes, and seconds (all of type int).

```c
struct time split_time(long total_seconds);
```

total_seconds is a time represented as the number of seconds since midnight. The function returns a structure containing the equivalent time in hours (0-23), minutes (0-59), and seconds (0-59).

Đáp án:

```c
struct time split_time(long total_seconds)
{
  struct time t;
  t.hours = (total_seconds / 3600) % 24;
  t.minutes = (total_seconds / 60) % 60;
  t.seconds = total_seconds % 60;
  return t;
}
```

## Exercise 7

Đề: Assume that the fraction structure contains two members: numerator and denominator (both of type int). Write functions that perform the following operations on fractions:

```text
(a) Reduce the fraction f to lowest terms. Hint: To reduce a fraction to lowest terms, first compute the greatest common divisor (GCD) of the numerator and denominator. Then divide both the numerator and denominator by the GCD.
(b) Add the fractions f1 and f2.
(c) Subtract the fraction f2 from the fraction f1.
(d) Multiply the fractions f1 and f2.
(e) Divide the fraction f1 by the fraction f2.
```

The fractions f, f1, and f2 will be arguments of type struct fraction; each function will return a value of type struct fraction. The fractions returned by the functions in parts (b)-(e) should be reduced to lowest terms. Hint: You may use the function from part (a) to help write the functions in parts (b)-(e).

Đáp án:

```c
static int gcd(int m, int n)
{
  int r;
  while (n != 0) {
    r = m % n;
    m = n;
    n = r;
  }
  return m;
}

(a) struct fraction reduce(struct fraction f)
    {
      int g = gcd(f.numerator, f.denominator);
      f.numerator /= g;
      f.denominator /= g;
      return f;
    }

(b) struct fraction add_frac(struct fraction f1, struct fraction f2)
    {
      struct fraction r;
      r.numerator = f1.numerator * f2.denominator + f2.numerator * f1.denominator;
      r.denominator = f1.denominator * f2.denominator;
      return reduce(r);
    }

(c) struct fraction sub_frac(struct fraction f1, struct fraction f2)
    {
      struct fraction r;
      r.numerator = f1.numerator * f2.denominator - f2.numerator * f1.denominator;
      r.denominator = f1.denominator * f2.denominator;
      return reduce(r);
    }

(d) struct fraction mul_frac(struct fraction f1, struct fraction f2)
    {
      struct fraction r;
      r.numerator = f1.numerator * f2.numerator;
      r.denominator = f1.denominator * f2.denominator;
      return reduce(r);
    }

(e) struct fraction div_frac(struct fraction f1, struct fraction f2)
    {
      struct fraction r;
      r.numerator = f1.numerator * f2.denominator;
      r.denominator = f1.denominator * f2.numerator;
      return reduce(r);
    }
```

## Exercise 8

Đề: Let color be the following structure:

```c
struct color {
    int red;
    int green;
    int blue;
};
```

```text
(a) Write a declaration for a const variable named MAGENTA of type struct color whose members have the values 255, 0, and 255, respectively.
(b) (C99) Repeat part (a), but use a designated initializer that doesn't specify the value of green, allowing it to default to 0.
```

Đáp án:

```c
(a) const struct color MAGENTA = {255, 0, 255};

(b) const struct color MAGENTA = {.red = 255, .blue = 255};
```

## Exercise 9

Đề: Write the following functions. (The color structure is defined in Exercise 8.)

```text
(a) struct color make_color(int red, int green, int blue);
Returns a color structure containing the specified red, green, and blue values. If any argument is less than zero, the corresponding member of the structure will contain zero instead. If any argument is greater than 255, the corresponding member of the structure will contain 255.
(b) int getRed(struct color c);
Returns the value of c's red member.
(c) bool equal_color(struct color color1, struct color color2);
Returns true if the corresponding members of color1 and color2 are equal.
(d) struct color brighter(struct color c);
Returns a color structure that represents a brighter version of the color c. The structure is identical to c, except that each member has been divided by 0.7 (with the result truncated to an integer). However, there are three special cases: (1) If all members of c are zero, the function returns a color whose members all have the value 3. (2) If any member of c is greater than 0 but less than 3, it is replaced by 3 before the division by 0.7. (3) If dividing by 0.7 causes a member to exceed 255, it is reduced to 255.
(e) struct color darker(struct color c);
Returns a color structure that represents a darker version of the color c. The structure is identical to c, except that each member has been multiplied by 0.7 (with the result truncated to an integer).
```

Đáp án:

```c
(a) struct color make_color(int red, int green, int blue)
    {
      struct color c;
      c.red = red < 0 ? 0 : red > 255 ? 255 : red;
      c.green = green < 0 ? 0 : green > 255 ? 255 : green;
      c.blue = blue < 0 ? 0 : blue > 255 ? 255 : blue;
      return c;
    }

(b) int getRed(struct color c)
    {
      return c.red;
    }

(c) bool equal_color(struct color color1, struct color color2)
    {
      return color1.red == color2.red &&
             color1.green == color2.green &&
             color1.blue == color2.blue;
    }

(d) struct color brighter(struct color c)
    {
      if (c.red == 0 && c.green == 0 && c.blue == 0) {
        c.red = c.green = c.blue = 3;
        return c;
      }
      if (c.red > 0 && c.red < 3) c.red = 3;
      if (c.green > 0 && c.green < 3) c.green = 3;
      if (c.blue > 0 && c.blue < 3) c.blue = 3;
      c.red = (int) (c.red / 0.7);
      c.green = (int) (c.green / 0.7);
      c.blue = (int) (c.blue / 0.7);
      if (c.red > 255) c.red = 255;
      if (c.green > 255) c.green = 255;
      if (c.blue > 255) c.blue = 255;
      return c;
    }

(e) struct color darker(struct color c)
    {
      c.red = (int) (c.red * 0.7);
      c.green = (int) (c.green * 0.7);
      c.blue = (int) (c.blue * 0.7);
      return c;
    }
```

## Exercise 10

Đề: The following structures are designed to store information about objects on a graphics screen:

```c
struct point { int x, y; };
struct rectangle { struct point upper_left, lower_right; };
```

A point structure stores the x and y coordinates of a point on the screen. A rectangle structure stores the coordinates of the upper left and lower right corners of a rectangle. Write functions that perform the following operations on a rectangle structure r passed as an argument:

```text
(a) Compute the area of r.
(b) Compute the center of r, returning it as a point value. If either the x or y coordinate of the center isn't an integer, store its truncated value in the point structure.
(c) Move r by x units in the x direction and y units in the y direction, returning the modified version of r. (x and y are additional arguments to the function.)
(d) Determine whether a point p lies within r, returning true or false. (p is an additional argument of type struct point.)
```

Đáp án:

```c
(a) int area(struct rectangle r)
    {
      int w = r.lower_right.x - r.upper_left.x;
      int h = r.lower_right.y - r.upper_left.y;
      return w * h;
    }

(b) struct point center(struct rectangle r)
    {
      struct point p;
      p.x = (r.upper_left.x + r.lower_right.x) / 2;
      p.y = (r.upper_left.y + r.lower_right.y) / 2;
      return p;
    }

(c) struct rectangle move(struct rectangle r, int x, int y)
    {
      r.upper_left.x += x;
      r.lower_right.x += x;
      r.upper_left.y += y;
      r.lower_right.y += y;
      return r;
    }

(d) bool inside(struct rectangle r, struct point p)
    {
      return p.x >= r.upper_left.x && p.x <= r.lower_right.x &&
             p.y >= r.upper_left.y && p.y <= r.lower_right.y;
    }
```

## Exercise 11 (W)

Đề: Suppose that s is the following structure:

```c
struct {
    double a;
    union {
        char b[4];
        double c;
        int d;
    } e;
    char f[4];
} s;
```

If char values occupy one byte, int values occupy four bytes, and double values occupy eight bytes, how much space will a C compiler allocate for s? (Assume that the compiler leaves no "holes" between members.)

Đáp án:

```text
20 bytes
```

## Exercise 12

Đề: Suppose that u is the following union:

```c
union {
    double a;
    struct {
        char b[4];
        double c;
        int d;
    } e;
    char f[4];
} u;
```

If char values occupy one byte, int values occupy four bytes, and double values occupy eight bytes, how much space will a C compiler allocate for u? (Assume that the compiler leaves no "holes" between members.)

Đáp án:

```text
16 bytes
```

## Exercise 13

Đề: Suppose that s is the following structure (point is a structure tag declared in Exercise 10):

```c
struct shape {
    int shape_kind;             /* RECTANGLE or CIRCLE */
    struct point center;        /* coordinates of center */
    union {
        struct {
            int height, width;
        } rectangle;
        struct {
            int radius;
        } circle;
    } u;
} s;
```

If the value of shape_kind is RECTANGLE, the height and width members store the dimensions of a rectangle. If the value of shape_kind is CIRCLE, the radius member stores the radius of a circle. Indicate which of the following statements are legal, and show how to repair the ones that aren't:

```c
(a) s.shape_kind = RECTANGLE;
(b) s.center.x = 10;
(c) s.height = 25;
(d) s.u.rectangle.width = 8;
(e) s.u.circle = 5;
(f) s.u.radius = 5;
```

Đáp án:

```text
(a) legal
(b) legal
(c) illegal: s.u.rectangle.height = 25;
(d) legal
(e) illegal: s.u.circle.radius = 5;
(f) illegal: s.u.circle.radius = 5;
```

## Exercise 14 (W)

Đề: Let shape be the structure tag declared in Exercise 13. Write functions that perform the following operations on a shape structure s passed as an argument:

```text
(a) Compute the area of s.
(b) Move s by x units in the x direction and y units in the y direction, returning the modified version of s. (x and y are additional arguments to the function.)
(c) Scale s by a factor of c (a double value), returning the modified version of s. (c is an additional argument to the function.)
```

Đáp án:

```c
#define PI 3.14159

(a) double area(struct shape s)
    {
      if (s.shape_kind == RECTANGLE)
        return s.u.rectangle.height * s.u.rectangle.width;
      return PI * s.u.circle.radius * s.u.circle.radius;
    }

(b) struct shape move(struct shape s, int x, int y)
    {
      s.center.x += x;
      s.center.y += y;
      return s;
    }

(c) struct shape scale(struct shape s, double c)
    {
      if (s.shape_kind == RECTANGLE) {
        s.u.rectangle.height *= c;
        s.u.rectangle.width *= c;
      } else {
        s.u.circle.radius *= c;
      }
      return s;
    }
```

## Exercise 15 (W)

Đề:

```text
(a) Declare a tag for an enumeration whose values represent the seven days of the week.
(b) Use typedef to define a name for the enumeration of part (a).
```

Đáp án:

```c
(a) enum days {MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY};

(b) typedef enum {MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY} Day;
```

## Exercise 16

Đề: Which of the following statements about enumeration constants are true?

```text
(a) An enumeration constant may represent any integer specified by the programmer.
(b) Enumeration constants have exactly the same properties as constants created using #define.
(c) Enumeration constants have the values 0, 1, 2, ... by default.
(d) All constants in an enumeration must have different values.
(e) Enumeration constants may be used as integers in expressions.
```

Đáp án:

```text
(a), (c), (e)
```

## Exercise 17 (W)

Đề: Suppose that b and i are declared as follows:

```c
enum {FALSE, TRUE} b;
int i;
```

Which of the following statements are legal? Which ones are "safe" (always yield a meaningful result)?

```c
(a) b = FALSE;
(b) b = i;
(c) b++;
(d) i = b;
(e) i = 2 * b + 1;
```

Đáp án:

```text
Legal: (a), (b), (c), (d), (e)
Safe: (a), (d), (e)
```

## Exercise 18

Đề:

```text
(a) Each square of a chessboard can hold one piece—a pawn, knight, bishop, rook, queen, or king—or it may be empty. Each piece is either black or white. Define two enumerated types: Piece, which has seven possible values (one of which is "empty"), and Color, which has two.
(b) Using the types from part (a), define a structure type named Square that can store both the type of a piece and its color.
(c) Using the Square type from part (b), declare an 8 x 8 array named board that can store the entire contents of a chessboard.
(d) Add an initializer to the declaration in part (c) so that board's initial value corresponds to the usual arrangement of pieces at the start of a chess game. A square that's not occupied by a piece should have an "empty" piece value and the color black.
```

Đáp án:

```c
(a) typedef enum {EMPTY, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING} Piece;
    typedef enum {BLACK, WHITE} Color;

(b) typedef struct { Piece piece; Color color; } Square;

(c)(d) Square board[8][8] = {
      {{ROOK,BLACK},{KNIGHT,BLACK},{BISHOP,BLACK},{QUEEN,BLACK},
       {KING,BLACK},{BISHOP,BLACK},{KNIGHT,BLACK},{ROOK,BLACK}},
      {{PAWN,BLACK},{PAWN,BLACK},{PAWN,BLACK},{PAWN,BLACK},
       {PAWN,BLACK},{PAWN,BLACK},{PAWN,BLACK},{PAWN,BLACK}},
      {{EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK},
       {EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK}},
      {{EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK},
       {EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK}},
      {{EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK},
       {EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK}},
      {{EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK},
       {EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK},{EMPTY,BLACK}},
      {{PAWN,WHITE},{PAWN,WHITE},{PAWN,WHITE},{PAWN,WHITE},
       {PAWN,WHITE},{PAWN,WHITE},{PAWN,WHITE},{PAWN,WHITE}},
      {{ROOK,WHITE},{KNIGHT,WHITE},{BISHOP,WHITE},{QUEEN,WHITE},
       {KING,WHITE},{BISHOP,WHITE},{KNIGHT,WHITE},{ROOK,WHITE}}
    };
```

## Exercise 19

Đề: Declare a structure with the following members whose tag is pinball_machine:

```text
name – a string of up to 40 characters
year – an integer (representing the year of manufacture)
type – an enumeration with the values EM (electromechanical) and SS (solid state)
players – an integer (representing the maximum number of players)
```

Đáp án:

```c
struct pinball_machine {
  char name[41];
  int year;
  enum {EM, SS} type;
  int players;
};
```

## Exercise 20

Đề: Suppose that the direction variable is declared in the following way:

```c
enum {NORTH, SOUTH, EAST, WEST} direction;
```

Let x and y be int variables. Write a switch statement that tests the value of direction, incrementing x if direction is EAST, decrementing x if direction is WEST, incrementing y if direction is SOUTH, and decrementing y if direction is NORTH.

Đáp án:

```c
switch (direction) {
  case EAST: x++; break;
  case WEST: x--; break;
  case SOUTH: y++; break;
  case NORTH: y--; break;
}
```

## Exercise 21

Đề: What are the integer values of the enumeration constants in each of the following declarations?

```c
(a) enum {NUL, SOH, STX, ETX};
(b) enum {VT = 11, FF, CR};
(c) enum {SO = 14, SI, DLE, CAN = 24, EM};
(d) enum {ENQ = 45, ACK, BEL, LF = 37, ETB, ESC};
```

Đáp án:

```text
(a) NUL = 0, SOH = 1, STX = 2, ETX = 3
(b) VT = 11, FF = 12, CR = 13
(c) SO = 14, SI = 15, DLE = 16, CAN = 24, EM = 25
(d) ENQ = 45, ACK = 46, BEL = 47, LF = 37, ETB = 38, ESC = 39
```

## Exercise 22

Đề: Let chess_pieces be the following enumeration:

```c
enum chess_pieces {KING, QUEEN, ROOK, BISHOP, KNIGHT, PAWN};
```

```text
(a) Write a declaration (including an initializer) for a constant array of integers named piece_value that stores the numbers 200, 9, 5, 3, 3, and 1, representing the value of each chess piece, from king to pawn. (The king's value is actually infinite, since "capturing" the king (checkmate) ends the game, but some chess-playing software assigns the king a large value such as 200.)
(b) (C99) Repeat part (a), but use a designated initializer to initialize the array. Use the enumeration constants in chess_pieces as subscripts in the designators. (Hint: See the last question in Q&A for an example.)
```

Đáp án:

```c
(a) const int piece_value[] = {200, 9, 5, 3, 3, 1};

(b) const int piece_value[] = {[KING] = 200, [QUEEN] = 9, [ROOK] = 5,
                               [BISHOP] = 3, [KNIGHT] = 3, [PAWN] = 1};
```
