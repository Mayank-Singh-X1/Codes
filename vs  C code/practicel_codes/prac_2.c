#include <stdio.h>
#include <stdlib.h>
  #include <string.h>

// int main(){
//   int i,n=5;
//   int *arr_malloc,*arr_calloc;

//   arr_malloc= (int*)malloc(n*sizeof(int));
//   arr_calloc= (int*)calloc(n,sizeof(int));

//   printf("Elements of malloc array :\n");
//   for(i=0;i<n;i++){
//     printf(" %d\n",arr_malloc[i]);
//   }

  
//   printf("Elements of calloc array :\n");
//   for(i=0;i<n;i++){
//     printf(" %d\n",arr_calloc[i]);
//   }






 
  
  int main() {
      char *str;
      int size;
  
      printf("Enter the maximum length of the string: ");
      scanf("%d", &size);
  
      // Allocate memory (+1 for null terminator)
      str = (char *)malloc((size + 1) * sizeof(char));
  
      if (str == NULL) {
          printf("Memory allocation failed.\n");
          return 1;
      }
  
      // Clear input buffer before using fgets
      getchar();
  
      printf("Enter the string: ");
      fgets(str, size + 1, stdin);
  
      printf("You entered: %s", str);
  
      free(str);
   
  

  return 0;
}