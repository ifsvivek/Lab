// mpi program to demonstrate MPI_Send and MPI_Recv

#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv){

    int process_rank, size_of_cluster,message_item;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &process_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size_of_cluster);

    if(process_rank == 0){
        message_item = 42;
        MPI_Send(&message_item, 1, MPI_INT, 1, 1, MPI_COMM_WORLD);
        printf("%d is sent from %d process\n",message_item,process_rank);
    } else if(process_rank == 1){
        MPI_Recv(&message_item, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("%d is received at %d process\n",message_item,process_rank);
    }
    MPI_Finalize();
    return 0;
    
}