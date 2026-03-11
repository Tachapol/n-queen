# Parallel N-Queen Solver (MPI + OpenMP)

## Overview
This project implements a parallel solver for the N-Queen problem using a hybrid MPI + OpenMP model. The goal is to explore the performance and scalability of parallel backtracking algorithms in HPC environments.

**Compares:**
- Sequential implementation
- Hybrid parallel implementation (MPI + OpenMP)

**Performance Analysis:**
- Speedup
- Parallel efficiency
- Amdahl's Law
- Analytical performance model


## File Description
| File | Description |
|------|-------------|
| `nqueens_sequential.c` | Sequential backtracking implementation |
| `nqueens_parallel.c` | Hybrid MPI + OpenMP implementation |
| `run_experiments.sh` | Script for running experiments |
| `Parallel_NQueen_Report.pdf` | Final project report |
| `README.md` | Project documentation |

## Compilation
### Sequential Version
```bash
gcc -O3 nqueens_sequential.c -o nqueens_seq
```

### Parallel Version (MPI + OpenMP)
```bash
mpicc -O3 -fopenmp nqueens_parallel.c -o nqueens_parallel
```

## Running the Program
### Sequential
```bash
./nqueens_seq 14
```

### Parallel Examples
- **1 Process, 1 Thread:** `OMP_NUM_THREADS=1 mpirun -np 1 ./nqueens_parallel 14`
- **1 Process, 2 Threads:** `OMP_NUM_THREADS=2 mpirun -np 1 ./nqueens_parallel 14`
- **2 Processes, 2 Threads (4 Workers):** `OMP_NUM_THREADS=2 mpirun -np 2 ./nqueens_parallel 14`
- **4 Processes, 2 Threads (8 Workers):** `OMP_NUM_THREADS=2 mpirun -np 4 ./nqueens_parallel 14`

## Experimental Configuration
**Configurations:**
| MPI Processes | OpenMP Threads | Total Workers |
|---------------|----------------|---------------|
| 1 | 1 | 1 |
| 1 | 2 | 2 |
| 2 | 2 | 4 |
| 4 | 2 | 8 |

**Problem Size:** N = 14  
**Expected Solutions:** 365,596

## Parallelization Strategy
- Search space partitioned by first-row queen placement
- Each first-row column forms an independent subtree
- MPI distributes tasks across processes:
  - Rank 0 → columns 0,4,8,12
  - Rank 1 → columns 1,5,9,13
  - Rank 2 → columns 2,6,10
  - Rank 3 → columns 3,7,11
- OpenMP threads explore subtrees in parallel with dynamic scheduling

## Performance Analysis
**Metrics Analyzed:**
- Execution time
- Speedup
- Parallel efficiency
- Amdahl's Law prediction
- Analytical performance model

**Experiments:** P = 1, 2, 4, 8 workers  
Results show decreasing runtime with more workers, but efficiency declines due to communication overhead and load imbalance.