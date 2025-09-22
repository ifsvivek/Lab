#include<mpi.h>
#include<stdio.h>

int main(int argc, char** argv){
    int rank, size;
    MPI_Status status;
    long int data=500;

    MPI_Init(NULL, NULL);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if(size<2){
        printf("This program requires at least two processes.\n");
        MPI_Abort(MPI_COMM_WORLD, 1);
    }
    if(rank==0){
        MPI_Send(&data, 1, MPI_INT, 1, 1, MPI_COMM_WORLD);
        MPI_Recv(&data, 1, MPI_INT, 1, 0, MPI_COMM_WORLD, &status);
        printf("Process 0 received data %d from process 1\n", data);
    }else if(rank==1){
        MPI_Send(&data, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
        MPI_Recv(&data, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);
        printf("Process 1 received data %d from process 0\n", data);
    }
    MPI_Finalize();
    return 0;

}