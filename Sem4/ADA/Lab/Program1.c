#include<stdio.h>   

void kruskal(int cost[][10], int n) {
    int par[n + 1], a, b, u, v, i, j, min, mincost = 0, ec = 0;

    for (i = 1; i <= n; i++)
        par[i] = -1;

    while (ec < n - 1) {
        min = 999;
        for (i = 1; i <= n; i++)
            for (j = 1; j <= n; j++)
                if (cost[i][j] < min && cost[i][j] != 0) {
                    min = cost[i][j];
                    a = u = i;
                    b = v = j;
                }
        while (par[u] > 0)
            u = par[u];
        while (par[v] > 0)
            v = par[v];

        if (u != v) {
            printf("%d -> %d = %d\n", a, b, min);
            mincost += min;
            par[v] = u;
            ec++;
        }
        cost[a][b] = cost[b][a] = 999;
    }
    printf("Minimum cost = %d\n", mincost);
}

int main() {
    int n, cost[10][10], i, j;
    printf("Enter the number of vertices: ");
    scanf("%d", &n);

    printf("Enter the cost matrix:\n");
    for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++)
            scanf("%d", &cost[i][j]);

    kruskal(cost, n);
    return 0;
}