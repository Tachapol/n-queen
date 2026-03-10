#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int N;

int is_safe(int *board, int row, int col) {
    for (int i = 0; i < row; i++) {
        if (board[i] == col) return 0;
        if (abs(board[i] - col) == abs(i - row)) return 0;
    }
    return 1;
}

long long solve(int *board, int row) {
    if (row == N) return 1;
    long long count = 0;
    for (int col = 0; col < N; col++) {
        if (is_safe(board, row, col)) {
            board[row] = col;
            count += solve(board, row + 1);
            board[row] = -1;
        }
    }
    return count;
}

int main(int argc, char *argv[]) {
    if (argc < 2) { fprintf(stderr, "Usage: %s <N>\n", argv[0]); return 1; }
    N = atoi(argv[1]);

    int *board = (int *)malloc(N * sizeof(int));
    memset(board, -1, N * sizeof(int));

    struct timespec ts, te;
    clock_gettime(CLOCK_MONOTONIC, &ts);

    long long result = solve(board, 0);

    clock_gettime(CLOCK_MONOTONIC, &te);
    double elapsed = (te.tv_sec - ts.tv_sec) + (te.tv_nsec - ts.tv_nsec) / 1e9;

    printf("N = %d\n", N);
    printf("Total solutions: %lld\n", result);
    printf("Time: %.6f seconds\n", elapsed);

    free(board);
    return 0;
}