#include<stdio.h>

void bottomupheap(int h[], int n){
    int k, v;
    for(int i = n/2; i >= 1; i--){
        k = i;
        v = h[k];
        int heap = 0;
        while(!heap && 2*k <= n){
            int j = 2*k;
            if(j < n && h[j] < h[j+1])
                j++;
            if(v >= h[j])
                heap = 1;
            else{
                h[k] = h[j];
                k = j;
            }
        }
        h[k] = v;
    }
}

void heapsort(int h[], int n){
    int i, t;
    bottomupheap(h, n);
    for(i = n; i > 1; i--){
        t = h[1];
        h[1] = h[i];
        h[i] = t;
        bottomupheap(h, i-1);
    }
}

void main(){
    int h[20], n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    printf("Enter the elements\n");
    for(int i = 1; i <= n; i++)
        scanf("%d", &h[i]);
    heapsort(h, n);
    printf("The sorted elements are\n");
    for(int i = 1; i <= n; i++)
        printf("%d ", h[i]);
    printf("\n");
}