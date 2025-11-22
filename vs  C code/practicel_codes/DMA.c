#include <stdio.h>
#include <stdlib.h>
 
      // int main(){
      //   int *arr,size,i;
      //   printf("Enter the size o array: ");
      //   scanf("%d",&size);
      //     arr=(int *)malloc(size*sizeof(int));
      //     if(arr==NULL){
      //       printf("Memory not allocated ");
      //     }else{
      //       printf("memory allocated successfully\n");
      //     }

      //     printf("Enter the %d elements:\n",size);
      //     for(i=0;i<size;i++){
      //       scanf("%d",&arr[i]);
      //     }

      //     printf("The elements are:\n");
      //     for(i=0;i<size;i++){
            
      //       printf("%d ",arr[i]);
      //     }
      //    printf("\nEnter the new size : ");
      //    scanf("%d",&size);
      //    arr=(int *)realloc(arr,size*sizeof (int));

      //    printf("array after reallocating memory:\n");
      //    for(i=0;i<size;i++){
      //       printf("%d ",arr[i]);
      //     }
      //     free(arr);
      //     printf("\nMemory freed successfully\n");

//2d array
int main()
{

      int **arr, rows, cols, i, j;
  
      printf("Enter rows and cols: ");
      scanf("%d %d", &rows, &cols);
  
      arr = (int **)malloc(rows * sizeof(int *));
      for (i = 0; i < rows; i++)
          arr[i] = (int *)malloc(cols * sizeof(int));
  
      printf("Enter elements:\n");
      for (i = 0; i < rows; i++)
          for (j = 0; j < cols; j++)
              scanf("%d", &arr[i][j]);
  
      int new_rows, new_cols;
      printf("Enter new rows and cols: ");
      scanf("%d %d", &new_rows, &new_cols);
  
      arr = (int **)realloc(arr, new_rows * sizeof(int *));
      for (i = 0; i < new_rows; i++)
          arr[i] = (int *)realloc(arr[i], new_cols * sizeof(int));
  
      printf("Resized array:\n");
      for (i = 0; i < new_rows; i++) {
          for (j = 0; j < new_cols; j++)
              printf("%d ", arr[i][j]);
          printf("\n");
      }
  
      for (i = 0; i < new_rows; i++) free(arr[i]);
      free(arr);
  
 
  

return 0;
}