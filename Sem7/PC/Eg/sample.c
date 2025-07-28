#include <stdio.h>
#include <omp.h>

// #pragma omp parallel
// int main() {
//     #pragma omp parallel
    
//     {
//         printf("Thread count: %d\n", omp_get_thread_num());
//         printf("Total threads: %d\n", omp_get_num_threads());
//     }
//     return 0;
// }

// #pragma omp parallel and #pragma omp for
// int main() {
//     #pragma omp parallel
//     {
//         int i;
//         #pragma omp for
       
//          for (i = 0; i < 10; i++) {
//             printf("Thread %d: i = %d\n", omp_get_thread_num(), i);
//         }
//     }
//     return 0;
// }


// #pragma omp parallel for
// int main() {
//     int i;
//     #pragma omp parallel for
//     for (i = 0; i < 100000; i++) {
//         printf("Thread %d: i = %d\n", omp_get_thread_num(), i);
//     }
//     return 0;
// }


// #pragma omp parallel section
// int main() {
//     #pragma omp parallel sections
//     {
//         #pragma omp section
//         {
//             printf("Section 1 executed by thread %d\n", omp_get_thread_num());
//         }
//         #pragma omp section
//         {
//             printf("Section 2 executed by thread %d\n", omp_get_thread_num());
//         }
//     }
//     return 0;
// }


// #pragma omp single
// int main() {
//     #pragma omp parallel
//     {
//         printf("Thread %d is executing the parallel region\n", omp_get_thread_num());
//         #pragma omp single
//         {
//             printf("Thread %d is the only one executing this single region\n", omp_get_thread_num());
//         }
//     }
//     return 0;
// }
// int main(){
//     int count = 0;
//     #pragma omp parallel
//     {
//         #pragma omp critical
//         {
//             count++;
//             printf("Thread %d incremented count to %d\n", omp_get_thread_num(), count);
//         }
//     }
// }
// int main(){
//     #pragma omp parallel
//     {
//         #pragma omp single
//         {
//             printf("This is printed only once by thread %d\n", omp_get_thread_num());
//         }
//     }
// }
int main(){
    #pragma omp parallel sections
    {
        #pragma omp section
        {
            printf("This is section 1 executed by thread %d\n", omp_get_thread_num());
        }
        #pragma omp section
        {
            printf("This is section 2 executed by thread %d\n", omp_get_thread_num());
        }
    }
}