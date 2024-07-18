#include<stdio.h>

int x[10], w[10], count = 0, n;

void sumofsubsets(int s, int k, int r) {
    x[k] = 1;
    if (s + w[k] == n) {
        printf("\nSubset %d:\n", ++count);
        for (int i = 1; i <= k; i++) {
            if (x[i] == 1)
                printf("%d\t", w[i]);
        }
    } else if (s + w[k] + w[k + 1] <= n)
        sumofsubsets(s + w[k], k + 1, r - w[k]);
    if ((s + r - w[k] >= n) && (s + w[k + 1] <= n)) {
        x[k] = 0;
        sumofsubsets(s, k + 1, r - w[k]);
    }
}

int main() {
    int sum = 0;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    printf("Enter the elements in ascending order:\n");
    for (int i = 1; i <= n; i++) {
        scanf("%d", &w[i]);
        sum += w[i];
    }
    if (sum < n) {
        printf("No solution exists\n");
        return 0;
    }
    printf("Enter the sum: ");
    scanf("%d", &n);
    sumofsubsets(0, 1, sum);
    if (count == 0)
        printf("No solution exists\n");
    return 0;
}