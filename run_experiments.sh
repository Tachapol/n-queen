#!/bin/bash
N=14   
RUNS=5

echo "=== Sequential ==="
for i in $(seq 1 $RUNS); do
    ./nqueens $N
done

echo ""
echo "=== Parallel: 1 rank, 1 thread ==="
for i in $(seq 1 $RUNS); do
    OMP_NUM_THREADS=1 mpirun -np 1 ./nqueens_parallel $N
done

echo ""
echo "=== Parallel: 1 rank, 2 threads ==="
for i in $(seq 1 $RUNS); do
    OMP_NUM_THREADS=2 mpirun -np 1 ./nqueens_parallel $N
done

echo ""
echo "=== Parallel: 2 ranks, 2 threads (4 total) ==="
for i in $(seq 1 $RUNS); do
    OMP_NUM_THREADS=2 mpirun -np 2 ./nqueens_parallel $N
done

echo ""
echo "=== Parallel: 4 ranks, 2 threads (8 total) ==="
for i in $(seq 1 $RUNS); do
    OMP_NUM_THREADS=2 mpirun -np 4 ./nqueens_parallel $N
done