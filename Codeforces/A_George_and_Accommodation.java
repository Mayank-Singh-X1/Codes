import java.util.*;
public class A_George_and_Accommodation {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count=0;
        int n=sc.nextInt();
        for(int i=0; i<n; i++){
            int p=sc.nextInt();
            int q= sc.nextInt();
            if(q-p >=2){
                count++;
            }
        }
        System.out.println(count);
    }

}