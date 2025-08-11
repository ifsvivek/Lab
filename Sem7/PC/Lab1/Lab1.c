#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
#include <time.h>

#define MAX 1000
void merge(int arr[], int l, int m, int r) {
    int i=l;
    int j=m+1;
    int k=l;
    int *temp=(int*)malloc(sizeof(int)*(r+1));
    while(i<=m && j<=r) {
        if(arr[i]<arr[j]) {
            temp[k++]=arr[i++];
        } else {
            temp[k++]=arr[j++];
        }
    }
    while(i<=m) {
        temp[k++]=arr[i++];
    }
    while(j<=r) {
        temp[k++]=arr[j++];
    }
    for(i=l; i<=r; i++) {
        arr[i]=temp[i];
    }
}

void sequential_merge_sort(int arr[], int l, int r) {
    if(l<r) {
        int m=(l+r)/2;
        sequential_merge_sort(arr, l, m);
        sequential_merge_sort(arr, m+1, r);
        merge(arr, l, m, r);
    }
}
void parallel_merge_sort(int arr_copy[], int l, int r) {
    if(l<r) {
        int m=(l+r)/2;
        #pragma omp parallel sections
        {
            #pragma omp section
            parallel_merge_sort(arr_copy, l, m);
            #pragma omp section
            parallel_merge_sort(arr_copy, m+1, r);
        }
        merge(arr_copy, l, m, r);
    }
}

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int *arr = (int*)malloc(n * sizeof(int));
    int *arr_copy = (int*)malloc(n * sizeof(int));

    srand(time(NULL));
    printf("The array is: ");
    for(int i = 0; i < n; i++) {
        arr[i] = rand() % MAX;
        printf("%d",arr[i]);
    }

    for(int i = 0; i < n; i++) {
        arr_copy[i] = arr[i];
    }
    double start_time, end_time;
    start_time = omp_get_wtime();
    sequential_merge_sort(arr, 0, n - 1);
    end_time = omp_get_wtime();
    printf("\nSequential Merge Sort Time: %f seconds\n", end_time - start_time);
    printf("Sorted array (sequential): ");

    // for(int i = 0; i < n; i++) {
    //     printf("%d ", arr[i]);
    // }

    start_time = omp_get_wtime();
    parallel_merge_sort(arr_copy, 0, n - 1);
    end_time = omp_get_wtime();
    printf("\nParallel Merge Sort Time: %f seconds\n", end_time - start_time);
    printf("Sorted array (parallel): ");

    // for(int i = 0; i < n; i++) {
    //     printf("%d ", arr_copy[i]);
    // }

    free(arr);
    free(arr_copy);
    return 0;
}
