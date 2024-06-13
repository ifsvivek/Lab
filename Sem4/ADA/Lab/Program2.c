#include<stdio.h>

void prims(int n, int s, int cost[][10]) {
    int i, j, a, b, min, totalcost = 0, ecount = 0;
    int tvertex[10] = { 0 };
    tvertex[s] = 1;

    while (ecount < n - 1) {
        min = 999;
        for (int i = 0;i < n;i++) {
            if (tvertex[i] == 1) {
                for (int j = 0;j < n;j++) {
                    if (tvertex[j] == 0 && cost[i][j] < min) {
                        min = cost[i][j];
                        a = i;
                        b = j;
                    }
                }
            }
        }
        printf("Edge from vertices %d to %d in %d\n", a, b, min);
        tvertex[b] = 1;
        totalcost += min;
        ecount++;
    }
    printf("Min cost= %d\n", totalcost);
}

void main() {
    int n, s;
    printf("Enter the no.of vertices: ");
    scanf("%d", &n);

    int a[n][n];

    printf("Enter the cost matrix: \n");
    for (int i = 0;i < n;i++) {
        for (int j = 0;j < n;j++)
            scanf("%d", &a[i][j]);
    }
    printf("Enter the source vertex: ");
    scanf("%d", &s);

    prims(n, s, a);
}