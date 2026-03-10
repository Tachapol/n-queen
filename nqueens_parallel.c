#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mpi.h>
#include <omp.h>
#include <time.h>

#define MAX_N 20

int N;
long long total_solutions = 0;

// Check if placing queen at (row, col) is safe
int is_safe(int *board, int row, int col) {
    for (int i = 0; i < row; i++) {
        if (board[i] == col) return 0;
        if (abs(board[i] - col) == abs(i - row)) return 0;
    }
    return 1;
}

// Recursive backtracking from given row
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
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <N>\n", argv[0]);
        return 1;
    }
    N = atoi(argv[1]);

    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    double start_time = MPI_Wtime();

    // Distribute first-row columns across MPI ranks
    long long local_count = 0;

    #pragma omp parallel reduction(+:local_count)
    {
        int *board = (int *)malloc(N * sizeof(int));
        memset(board, -1, N * sizeof(int));

        #pragma omp for schedule(dynamic, 1)
        for (int col = rank; col < N; col += size) {
            board[0] = col;
            local_count += solve(board, 1);
        }

        free(board);
    }

    // Reduce all counts to rank 0
    long long global_count = 0;
    MPI_Reduce(&local_count, &global_count, 1, MPI_LONG_LONG_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    double end_time = MPI_Wtime();
    double elapsed = end_time - start_time;

    if (rank == 0) {
        printf("N = %d\n", N);
        printf("Total solutions: %lld\n", global_count);
        printf("Time: %.6f seconds\n", elapsed);
        printf("MPI ranks: %d, OMP threads: %d\n", size, omp_get_max_threads());
    }

    MPI_Finalize();
    return 0;
}