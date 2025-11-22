import java.util.*;
public class DSA {
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        System.out.print("enter the number of values: ");
        int n=sc.nextInt();
        System.out.print("enter the number of columns: ");
        // int m=sc.nextInt();

        //Hollow rectangle
        // for(int i=0;i<=n;i++){
        //     for(int j=0;j<=m;j++){
        //         if( i==0 || i==n || j==0 || j==m){
        //             System.out.print("*");
        //         }else{
        //             System.out.print(" ");
        //         }
        //     }
        //     System.out.println();
        // }

        //star
        // for(int i=0;i<n;i++){
        //     for(int j=0;j<i;j++){
        //         System.out.print("*");
        //     }
        //     System.out.println();
        // }

        //180 pyramid
            // for(int i=0;i<n;i++){
            //     for(int j=0;j<n-i;j++){
            //         System.out.print(" ");
            //     }
            //     for(int j=0;j<=i;j++){
            //         System.out.print("*");
            //     }
            //     System.out.println();
            // }


        // for(int i=1;i<=n;i++){
        //     for(int j=1;j<=i;j++){
        //         System.out.print(j);
        //     }
        //     System.out.println();
        // }

        //floyds triangle
        // int num=1;
        // for(int i=0;i<n;i++){
        //     for(int j=0;j<i;j++){
        //         System.out.print(num + " ");
        //         num++;
        //     }
        //   System.out.println();
        // }


        //1 0 triangle
        for(int i=0;i<n;i++){
            for(int j=0;j<i;j++){
                int sum =i+j;
                if (sum%2==0){
                    System.out.print("1 ");
                }
                if (sum%2!=0){
                    System.out.print("0 ");
                }
            }
            System.out.println();
        }
        sc.close();
    }
}
