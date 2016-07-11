#include<stdio.h>

typedef struct tmptype {
    int x1;
    int y1;
    int x2;
    int y2;
} block;

int main() {
    int count = 0, map[100][100] = {0};//地图炮大法好
    int i, j, k, n;
    scanf("%d", &n);
    block blocks[n];
    for (i = 0; i < n; i++) {
        scanf("%d %d %d %d", &blocks[i].x1, &blocks[i].y1, &blocks[i].x2, &blocks[i].y2);
    }
    for (i = 0; i < n; i++) {
        for (j = blocks[i].x1; j < blocks[i].x2; j++) {
            for (k = blocks[i].y1; k < blocks[i].y2; k++) {
                map[j][k] = 1;
            }
        }
    }
    for (j = 0; j < 100; j++) {
        for (k = 0; k < 100; k++) {
            if (map[j][k]) {
                count++;
            }
        }
    }
    printf("count:%d\n", count);
    return 0;
}
