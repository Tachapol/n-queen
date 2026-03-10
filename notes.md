
<!-- Sequential -->
    gcc nqueens_sequential.c -o nqueens

    ./nqueens 8


 <!-- Parallel -->
    mpicc nqueens_parallel.c \
    -O3 \
    -Xpreprocessor -fopenmp \
    -I/opt/homebrew/opt/libomp/include \
    -L/opt/homebrew/opt/libomp/lib \
    -lomp \
    -o nqueens_parallel
    
    ./nqueens 8
    mpirun -np 4 ./nqueens_parallel 13


<!-- Plot -->
# ใส่ค่า runtime จาก results.txt ใน plot_performance.py แล้วรัน:
python3 plot_performance.py

