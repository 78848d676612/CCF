#include<stdio.h>

typedef struct tmptype {
    int x;
    int y;
} coordinate;

int main() {
    int i, j, n, m, k, d;
    scanf("%d", &n);
    scanf("%d", &m);
    scanf("%d", &k);
    scanf("%d", &d);
    coordinate map[n][n];
    coordinate shop[m];
    coordinate customer[k];
    coordinate unavalaible[d];
    for (i = 0; i < m; i++) {
        scanf("%d %d", &shop[i].x, &shop[i].y);
    }
    for (i = 0; i < k; i++) {
        scanf("%d %d", &customer[i].x, &customer[i].y);
    }
    for (i = 0; i < d; i++) {
        scanf("%d %d", &unavalaible[i].x, &unavalaible[i].y);
    }

    return 0;
}
/*
思路：
1.直达：如果没有障碍，直接计算 
2.唯一障碍：步数不变
3. 

*/
