#include <stdio.h>// 
int  main()
{
  int n,original,reverse=0;
  printf("Enter the number: ");
  scanf("%d",&n);
  original=n;
  while(n!=0)
    {
      int remainder=n%10;
      reverse=reverse*10+remainder;
      n/=10;
    }

  if(original==reverse)
  {
    printf("%d is a palinndrome number",original);
  }
  else{
    printf("%d is not a palindrome number",original);
  }


  return 0;
}