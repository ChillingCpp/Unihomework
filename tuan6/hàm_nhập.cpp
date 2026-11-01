void clr()
{
    int c;
    while ((c = getchar()) != '\n' && c != EOF)
        ;
}
void nhap(NGAY& a)
{
    while (1)
    {
        printf("nhap ngay : ");
        if (scanf("%hu", &a.d) == 1 && a.d >= 1 && a.d <= 31)
            break;
        clr();
    }
    clr();
    while (1)
    {
        printf("nhap thang : ");
        if (scanf("%hu", &a.m) == 1 && a.m >= 1 && a.m <= 12)
        {
            if ((a.d != 31 || (a.m != 4 && a.m != 6 && a.m != 9 && a.m != 11))
                && !(a.m == 2 && a.d > 29))
                break;
        }
        clr();
    }
    clr();
    while (1)
    {
        printf("nhap nam : ");
        if (scanf("%hu", &a.y) == 1 && a.y >= 1 && a.y <= 60000)
        {
            if (!(a.m == 2 && a.d == 29) || lp(a.y))
                return;
        }
        clr();
    }
    clr();
}