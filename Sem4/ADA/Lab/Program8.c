#include<stdio.h>

int x[10], w[10], count = 0, n;

void findSubsetsWithSum(int currentSum, int currentIndex, int remainingSum) {
    x[currentIndex] = 1;
    if (currentSum + w[currentIndex] == n) {
        printf("\nSubset %d:\n", ++count);
        for (int i = 1; i <= currentIndex; i++) {
            if (x[i] == 1)
                printf("%d\t", w[i]);
        }
    } else if (currentSum + w[currentIndex] + w[currentIndex + 1] <= n) {
        findSubsetsWithSum(currentSum + w[currentIndex], currentIndex + 1, remainingSum - w[currentIndex]);
    }
    if ((currentSum + remainingSum - w[currentIndex] >= n) && (currentSum + w[currentIndex + 1] <= n)) {
        x[currentIndex] = 0;
        findSubsetsWithSum(currentSum, currentIndex + 1, remainingSum - w[currentIndex]);
    }
}

void main() {
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
    findSubsetsWithSum(0, 1, sum);
    if (count == 0)
        printf("No solution exists\n");
}
