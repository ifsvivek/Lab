# 5
```c
#include <stdio.h>
#include <mpi.h>

int main(int argc, char** argv) {
    int process_Rank, size_Of_Cluster, message_Item;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size_Of_Cluster);
    MPI_Comm_rank(MPI_COMM_WORLD, &process_Rank);

    if (size_Of_Cluster < 2) {
        if (process_Rank == 0) {
            printf("This program needs at least 2 processes.\n");
        }
        MPI_Finalize();
        return 0;
    }

    if (process_Rank == 0) {
        message_Item = 42;
        MPI_Send(&message_Item, 1, MPI_INT, 1, 1, MPI_COMM_WORLD);
        printf("%d is sent from process %d to process 1\n", message_Item, process_Rank);
    }
    else if (process_Rank == 1) {
        MPI_Recv(&message_Item, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("process 1 received %d from process 0\n", message_Item);
    }

    MPI_Finalize();
    return 0;
}

```

# 6A
```
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    int rank, size;
    MPI_Status status;
    long int data = 500;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (size != 2) {
        if (rank == 0)
            printf("This program requires exactly 2 processes.\n");
        MPI_Finalize();
        return 0;
    }

    if (rank == 0) {
        // Both do recv first -> deadlock
        MPI_Recv(&data, 1, MPI_LONG, 1, 10, MPI_COMM_WORLD, &status);
        printf("Process 0 received data from process 1\n");

        MPI_Send(&data, 1, MPI_LONG, 1, 10, MPI_COMM_WORLD);
        printf("Process 0 sent data to process 1\n");
    }
    else if (rank == 1) {
        MPI_Recv(&data, 1, MPI_LONG, 0, 10, MPI_COMM_WORLD, &status);
        printf("Process 1 received data from process 0\n");

        MPI_Send(&data, 1, MPI_LONG, 0, 10, MPI_COMM_WORLD);
        printf("Process 1 sent data to process 0\n");
    }

    printf("Process %d finished communication.\n", rank);

    MPI_Finalize();
    return 0;
}

```


# 6B

```
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    int rank, size;
    MPI_Status status;
    long int data = 500;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (size != 2) {
        if (rank == 0)
            printf("This program requires exactly 2 processes.\n");
        MPI_Finalize();
        return 0;
    }

    if (rank == 0) {
        MPI_Send(&data, 1, MPI_INT, 1, 10, MPI_COMM_WORLD);
        printf("\nSent data to process 1\n");
        MPI_Recv(&data, 1, MPI_INT, 1, 10, MPI_COMM_WORLD, &status);
        printf("Received data from process 1\n");
    } 
    else if (rank == 1) {
        MPI_Send(&data, 1, MPI_INT, 0, 10, MPI_COMM_WORLD);
        printf("\nSent data to process 0\n");
        MPI_Recv(&data, 1, MPI_INT, 0, 10, MPI_COMM_WORLD, &status);
        printf("Received data from process 0\n");
    }

    printf("Process %d finished communication.\n", rank);
    MPI_Finalize();
    return 0;
}
```

# 7

```c
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    int rank, size;
    int data;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0) {
        data = 42;
        printf("Process %d broadcasting data = %d\n", rank, data);
    }

    MPI_Bcast(&data, 1, MPI_INT, 0, MPI_COMM_WORLD);
    printf("Process %d received data = %d\n", rank, data);

    MPI_Finalize();
    return 0;
}

```

# 8
```c
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    int rank, size;
    int send_data[100], recv_data, gather_data[100];

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0) {
        for (int i = 0; i < size; i++)
            send_data[i] = (i + 1) * 10;
    }

    MPI_Scatter(send_data, 1, MPI_INT, &recv_data, 1, MPI_INT, 0, MPI_COMM_WORLD);
    recv_data *= 2;
    MPI_Gather(&recv_data, 1, MPI_INT, gather_data, 1, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        for (int i = 0; i < size; i++)
            printf("%d ", gather_data[i]);
        printf("\n");
    }

    MPI_Finalize();
    return 0;
}
```

# 9

```c
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    int rank, size;
    int value, max_val, min_val, sum_val, prod_val;
    int all_max_val, all_min_val, all_sum_val, all_prod_val;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    value = rank + 1;

    MPI_Reduce(&value, &max_val, 1, MPI_INT, MPI_MAX, 0, MPI_COMM_WORLD);
    MPI_Reduce(&value, &min_val, 1, MPI_INT, MPI_MIN, 0, MPI_COMM_WORLD);
    MPI_Reduce(&value, &sum_val, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    MPI_Reduce(&value, &prod_val, 1, MPI_INT, MPI_PROD, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        printf("\nMPI_Reduce on root:\n");
        printf("MAX = %d\n", max_val);
        printf("MIN = %d\n", min_val);
        printf("SUM = %d\n", sum_val);
        printf("PROD = %d\n", prod_val);
    }

    MPI_Allreduce(&value, &all_max_val, 1, MPI_INT, MPI_MAX, MPI_COMM_WORLD);
    MPI_Allreduce(&value, &all_min_val, 1, MPI_INT, MPI_MIN, MPI_COMM_WORLD);
    MPI_Allreduce(&value, &all_sum_val, 1, MPI_INT, MPI_SUM, MPI_COMM_WORLD);
    MPI_Allreduce(&value, &all_prod_val, 1, MPI_INT, MPI_PROD, MPI_COMM_WORLD);

    printf("\nRank %d - MPI_Allreduce:\n", rank);
    printf("MAX = %d\n", all_max_val);
    printf("MIN = %d\n", all_min_val);
    printf("SUM = %d\n", all_sum_val);
    printf("PROD = %d\n", all_prod_val);

    MPI_Finalize();
    return 0;
}

```
