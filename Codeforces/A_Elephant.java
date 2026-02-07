import java.util.*;

public class A_Elephant{
  static int[] calSub(int a[], int b[]) {
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
      int res= n1-n2;
      int[] digits = String.valueOf(Math.abs(res))
                    .chars()
                    .map(Character::getNumericValue)
                    .toArray();
      // int digits 
      
      if (res < 0){ digits[0] *= -1;} 
      return digits;
  }

  public static void main(String[] args) {
    int[] arr1 ={1,2,3,4};
    int[] arr2 = {1};
    int[] res = calSub(arr1, arr2);
    System.out.print("[");
    for (int i : res) System.out.print(i+" ");
    System.out.println("]");   
  }
}