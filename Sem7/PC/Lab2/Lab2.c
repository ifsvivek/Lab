#include<stdio.h>
#include<omp.h>

int main(){
    int n,i;
    printf("Enter the number of iterations: ");
    scanf("%d",&n);
    omp_set_num_threads(4);
    #pragma omp parallel for schedule(static,2)
    for(i=0;i<n;i++){
        printf("Iteration %d by thread %d\n",i,omp_get_thread_num());
    }
}