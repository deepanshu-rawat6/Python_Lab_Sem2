#include<stdio.h>
#include<stdlib.h>
struct Node{
    int data;
    struct Node* next;
}
struct Node* head=NULL;
void insert(int x){
    struct Node* temp=(struct Node*)malloc(sizeof(struct Node));
    temp->data=x;
    temp->next=head;
    head=temp;
}
void print(){
    
}