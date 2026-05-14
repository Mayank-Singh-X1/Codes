package JAVA_TRAININNG;

import java.util.*;

public class Array_sub{
  static int[] calSum(int a[], int b[]) {
      String as="";
      String bs="";
    for(int i:a){
        as+=i;
    }
      for(int i: b){
          bs+=i;
      }
      int n1=Integer.parseInt(as);
      int n2 =Integer.parseInt(bs);
      int res= n1+n2;
      int []qwe={res};
      return qwe;
  }

  /* Driver program to test above function */
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
   int [] arr1= {1,2,3,4};
   int arr2[] = {2,3};

    int[] res = calSum(arr1, arr2);
    for (int i : res) System.out.println(i);
  }
}
