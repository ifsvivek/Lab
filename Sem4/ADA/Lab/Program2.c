#include<stdio.h>

void prims(int n, int s, int cost[][10]) {
    int i, j, a = -1, b = -1, min, total_cost = 0, edge_count = 0;
    int tree_vertex[10] = { 0 };
    tree_vertex[s] = 1;

    while (edge_count < n - 1) {
        min = 999;
        for (i = 0; i < n; i++) {
            if (tree_vertex[i] == 1) {
                for (j = 0; j < n; j++) {
                    if (tree_vertex[j] == 0 && cost[i][j] < min) {
                        min = cost[i][j];
                        a = i;
                        b = j;
                    }
                }
            }
        }
        if (a != -1 && b != -1) {
            printf("Edge from vertices %d to %d with cost %d\n", a, b, min);
            tree_vertex[b] = 1;
            total_cost += min;
            edge_count++;
        }
    }
    printf("Min cost= %d\n", total_cost);
}

void main() {
    int n, s, cost[10][10];
    printf("Enter the no.of vertices: ");
    scanf("%d", &n);
    printf("Enter the cost matrix: \n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &cost[i][j]);

    printf("Enter the source vertex: ");
    scanf("%d", &s);
    prims(n, s, cost);
}