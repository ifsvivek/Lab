//  MPI 
// mpi init, mpi finalize, mpi rank, mpi size

#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    printf("Hello from process %d of %d\n", rank, size);

    MPI_Finalize();
    return 0;
}
// mpicc Lab5.c -o lab5
// mpirun -np 4 ./lab5


// mpi send, mpi recv

// int main(int argc, char** argv) {
//     MPI_Init(&argc, &argv);

//     int rank, size;
//     MPI_Comm_rank(MPI_COMM_WORLD, &rank);
//     MPI_Comm_size(MPI_COMM_WORLD, &size);

//     int n = 10; // Number of elements per process
//     int* send_data = NULL;
//     if (rank == 0) {
//         send_data = (int*)malloc(n * size * sizeof(int));
//         for (int i = 0; i < n * size; i++) {
//             send_data[i] = i + 1;
//         }
//     }

//     int* recv_data = (int*)malloc(n * sizeof(int));
//     MPI_Scatter(send_data, n, MPI_INT, recv_data, n, MPI_INT, 0, MPI_COMM_WORLD);

//     printf("Process %d received: ", rank);
//     for (int i = 0; i < n; i++) {
//         printf("%d ", recv_data[i]);
//     }
//     printf("\n");

//     if (rank == 0) {
//         free(send_data);
//     }
//     free(recv_data);

//     MPI_Finalize();
//     return 0;
// }