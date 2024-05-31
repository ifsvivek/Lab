#include<stdio.h>
#include<stdlib.h>

typedef struct bt {
    int data;
    struct bt* left;
    struct bt* right;

}node;

int max(int a, int b) {
    return (a > b) ? a : b;
}

int height(node* root) {
    if (root == NULL)
        return -1;
    else
        return(max(height(root->left), height(root->right)) + 1);
}

node* insert(node* root, int key) {
    if (root == NULL) {
        root = (node*)malloc(sizeof(node));
        root->data = key;
        root->left = NULL;
        root->right = NULL;
        return root;
    }
    if (key < root->data)
        root->left = insert(root->left, key);
    else if (key > root->data)
        root->right = insert(root->right, key);
    return root;
}


int main() {
    int n, i, key, h;
    node* root = NULL, * temp;
    printf("Enter the number of nodes\n");
    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        printf("Enter the element\n");
        scanf("%d", &key);
        root = insert(root, key);
    }
    h = height(root);
    printf("height: %d", h);
}