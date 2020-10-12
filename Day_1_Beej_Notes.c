#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // int d = 100;    //value is 100 decimal (decimal)
    // int h = 0x100;  //value is 256 decimal (hex)
    // int b = 0b100;  //value is 4 decimal (binary)

    // //if we want to write 47F in hex:
    // int y = 0x47F;

    // //
    // if (b == 4) {
    //     //TRUE! because value of b is equal to 4
    // }

    // take a binary number and print it out in hexadecimal
    // int x = 0b11000101;
    // printf("%d decimal\n", x);

    // printf("%x hex\n", x);

    // printf("%X hex\n", x);

    // int y = 255;
    // char s[20];

    // sprintf(s, "%X", y);

    // printf("%s\n", s);

    char *s = "110011"; //binary
    long v = strtol(s, NULL, 2);
    printf("%ld\n", v);

    return 0;
}