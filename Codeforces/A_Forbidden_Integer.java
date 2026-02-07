import java.util.*;

public class A_Forbidden_Integer {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i = sc.nextInt(); //5

        for(int a=0; a<i; a++){
        int n = sc.nextInt(); //10
        int k = sc.nextInt(); //3
        int x = sc.nextInt(); //2

        if (x != 1 ) {
            System.out.println("YES");
            System.out.println(n);
            for (int j = 0; j < n; j++) {
                System.out.print("1" + " ");
            }
            System.out.println();

        }else if(n%2==0 && k>=2 && x!=2){
            System.out.println("YES");
            System.out.println(n/2);
             for (int j = 0; j <= n/2-1; j++) {
                System.out.print("2" + " ");
            }
            System.out.println();

        }else {
             System.out.println("NO");
        }
    }
    }

}
