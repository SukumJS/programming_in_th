#include <stdio.h>
#include <math.h>

int main()
{
    int a = 11, b = 21, c = 30;

    // c = a * ((++b) / 7) / 30.0 + b % 10;

    // printf("%f", (float)c);

    c = ++b + b;
    printf("%d", c);

    return 0;
}
