import java.util.*;
public class TAraining {
    public static void main(String[] args) {
        Scanner sc=new Scanner (System.in);
      //longest subsequence in given array using two pointer approach
      //input n=8  arr=1,2,3,1,2,3,4,2 output=4
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++){
            if(sc.hasNextInt()){
                arr[i]=sc.nextInt();              
            }
        }
        HashMap<Integer, Integer> map=new HashMap<>();
        int left=0;
        int max_len=0;
        for(int right=0;right<n;right++){
            int val = arr[right];
            map.put(val, map.getOrDefault(val, 0) + 1);

            while(map.get(val) > 1) {
                int leftVal = arr[left];
                map.put(leftVal, map.get(leftVal) - 1);
                left++;
            }

            max_len = Math.max(max_len, right - left + 1);
        }
        sc.close();
        System.out.println(max_len);
    }
}
