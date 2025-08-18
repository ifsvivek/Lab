// OMP parallel for fibonacci series using tasks

#include <omp.h>
#include <stdio.h>
#include <stdint.h>

int fib_recursive_omp(int n) {
    int x,y;
    if (n < 2) return n;
    #pragma omp task shared(x) firstprivate(n)
    x = fib_recursive_omp(n - 1);
    #pragma omp task shared(y) firstprivate(n)
    y = fib_recursive_omp(n - 2);
    #pragma omp taskwait
    return x + y;
}

int main(){
    int n = 41;
    int result;
    double start_time, end_time;
    start_time = omp_get_wtime();
    
    #pragma omp parallel
    {
        #pragma omp single
        result = fib_recursive_omp(n);
    }
    
    printf("Fibonacci of %d is %d\n", n, result);
    end_time = omp_get_wtime();
    printf("Time taken: %f seconds\n", end_time - start_time);
    return 0;
}