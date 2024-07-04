#include <stdio.h>

int max(int a, int b) {
    return a > b ? a : b;
}

void DPknapsack(int n, int m, int w[], int p[]) {
    int i, j, V[n + 1][m + 1];
    for (i = 0; i <= n; i++) {
        for (j = 0; j <= m; j++) {
            if (i == 0 || j == 0)
                V[i][j] = 0;
            else if (j < w[i - 1])
                V[i][j] = V[i - 1][j];
            else
                V[i][j] = max(V[i - 1][j], V[i - 1][j - w[i - 1]] + p[i - 1]);
            printf("%d\t", V[i][j]);
        }
        printf("\n");
    }
    printf("Optimal profit: %d\n", V[n][m]);
    printf("Items selected: ");
    int res = V[n][m];
    j = m;
    for (i = n; i > 0 && res > 0; i--) {
        if (res == V[i - 1][j])
            continue;
        else {
            printf("%d ", i);
            res -= p[i - 1];
            j -= w[i - 1];
        }
    }
    printf("\n");
}

int main() {
    int n, m, i;
    printf("Enter the number of items: ");
    scanf("%d", &n);
    int w[n], p[n]; // Adjusted the size to n, as we will use 0-based indexing
    printf("Enter the weights of the items: ");
    for (i = 0; i < n; i++) // Start loop from 0 for 0-based indexing
        scanf("%d", &w[i]);
    printf("Enter the profits of the items: ");
    for (i = 0; i < n; i++) // Start loop from 0 for 0-based indexing
        scanf("%d", &p[i]);
    printf("Enter the capacity of the knapsack: ");
    scanf("%d", &m);
    DPknapsack(n, m, w, p);
    return 0;
}