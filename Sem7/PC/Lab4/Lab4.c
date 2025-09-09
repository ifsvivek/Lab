#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int is_prime(int n) {
    if (n <= 1) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main(int argc, char *argv[]) {
    int n = 99999;
    if (argc > 1) n = atoi(argv[1]);

    clock_t start = clock();
    for (int i = 1; i <= n; i++) {
        if (is_prime(i)) {
        }
    }
    clock_t end = clock();
    double serial_time = (double)(end - start) / CLOCKS_PER_SEC;

    start = clock();
    #pragma omp parallel for default(none) 
    for (int i = 1; i <= n; i++) {
        if (is_prime(i)) {
            printf("%d, ", i);
        }
    }
    end = clock();
    double parallel_time = (double)(end - start) / CLOCKS_PER_SEC;
    printf("\n");
    printf("Serial time: %f seconds\n", serial_time);
    printf("Parallel time: %f seconds\n", parallel_time);

    return 0;
}
