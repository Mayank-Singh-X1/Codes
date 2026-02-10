import java.util.*;
public class A_Halloumi_Boxes{
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int a=sc.nextInt();
        for(int i=0; i<a; i++){
            int n=sc.nextInt();
            int k=sc.nextInt();
            if(k>1){
                System.out.println("YES");
            }else{
                System.out.println("NO");
            }
        }
    }
}