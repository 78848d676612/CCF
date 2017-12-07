#include<stdio.h>

int abs(int x) {
    return x < 0 ? -x : x;
}

int main() {
    int i, j, n, count;
    scanf("%d", &n);
    int numbers[n];
    count = 0;
    for (i = 0; i < n; i++) {
        scanf("%d", &numbers[i]);
    }
    for (i = 0; i < n; i++) {
        for (j = i; j < n; j++) {
            if (i != j && abs(numbers[i] - numbers[j]) == 1) {
                printf("%d:%d-%d:%d\n", i, numbers[i], j, numbers[j]);
                count++;
            }
        }
    }
    printf("count:%d\n", count);
}
