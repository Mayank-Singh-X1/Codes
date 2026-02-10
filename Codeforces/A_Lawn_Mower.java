import java.util.*;
public class A_Lawn_Mower{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        for(int i=0; i<n; i++){
            long a=sc.nextInt();
            long b=sc.nextInt();
             if(b==1){
                System.out.println(0);
                continue;
            }
            long keep= a/b;
            long ans = a-keep;
           
            System.out.println(ans);
        }
    }
}