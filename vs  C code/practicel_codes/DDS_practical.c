// #include <stdio.h>
// #define size 100

// int stack[size];
// int top=-1;

// void push(int value){
//     if (top==size-1){
//         printf("stack overflow");
//     }else{
//         top++;
//         stack[top]=value;
//         printf("pushed %d \n",value);
//     }
// }

// void pop(){
//     if (top==-1){
//         printf("stack overflow");
// }else{
//     printf("popped %d",stack[top]);
//     top--;
// }
// }

// void peek(){
//      if (top==-1){
//         printf("stack overflow");
// }else{
//     printf("top %d",stack[top]);
  
// }
// }

// void traverse(){
//      if (top==-1){
//         printf("stack overflow");
// }else{
//     printf("\nstack elements are :");
//     for(int i=0;i<=top;i++){
//         printf("%d ",stack[i]);
//     }
//   printf("\n");
// }
// }

// void search(int value){
//      if (top==-1){
//         printf("stack overflow");
// }else{
//    int found=0;
//     for(int i=0;i<=top;i++){
//         if(stack[i]==value){
//             printf("value found at index %d",i+1);
//             found=1;
//             break;
//         }
//     }
//   if(!found){
//     printf("value not found");
//   }
// }
// }

// int main(){
//     push(10);
//     push(20);
//     push(30);
//     search(10);
//     traverse();
    
// }

#include <stdio.h>

void hanoi(int n, char from, char to ,char aux ){
    if (n==1){
        printf("Move disk 1 from %c to %c",from,to);
        return;
    }
hanoi(n-1,from,aux,to);
printf("\nMove disk%d from %c to %c \n",n,from,to);
hanoi(n-1,aux,to,from);

}

int main(){
    int n;
    printf("enter the number of disks: ");
    scanf("%d",&n);

    hanoi(n,'A','B','C');
    return 0;
}