#include<stdio.h>
#include<lpc214x.h>

int main() {
    unsigned int n=5, i;
    unsigned long fact = 1;
    for (i = 1; i <= n; i++) {
        fact *= i;
    }
    PINSEL0=fact;
    return 0;
}