import java.util.*;

public class DSA_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of rows");
        int row = sc.nextInt();
        System.out.println("Enter the number of columns");
        int col = sc.nextInt();

        int arr[][] = new int[row][col];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                System.out.println("Enetr the value of " + (i + 1) + (j + 1));
                arr[i][j] = sc.nextInt();
            }
        }

        // for(int i=0; i<row; i++){
        // for(int j=0; j<col; j++){
        // System.out.print(arr[i][j]+" ");
        // }
        // System.out.println();
        // }

        System.out.print("Enter the value you want to search: ");
        int key = sc.nextInt();
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (key == arr[i][j]) {
                    System.out.print("found at index " + (i + 1) + (j + 1));
                }
            }

        }

        sc.close();
    }
}
