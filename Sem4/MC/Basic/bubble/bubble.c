#include<stdio.h>
#include<lpc214x.h>
int main() {
    unsigned long a[] = { 0x555555,0x444444,0x333333,0x222222 };
    unsigned long temp, i, j;
    for (i = 0;i < 3;i++) {
        for (j = 0;j < 3;j++) {
            if (a[j] > a[j + 1]) {
                temp = a[j + 1];
                a[j + 1] = a[j];
                a[j] = temp;
            }
        }
    }while (1);
    return 0;
}