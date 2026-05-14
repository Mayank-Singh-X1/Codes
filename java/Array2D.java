import java.util.*;

public class Array2D {
    public static void main(String[] args) {
        int[][] matrix = {
                { 1, 2, 3 },
                { 4, 5, 6 },
                { 7, 8, 9 }
        };

        for (int i = 0; i < matrix.length; i++) {   
                if (i % 2 == 0) {
                    for (int j = 0; j < matrix[i].length; j++) {
                    System.out.print(matrix[i][j] + " ");
                    }
                } else {
                    for (int k = matrix[0].length-1; k >=0; k--) {
                        System.out.print(matrix[i][k]+" ");

                    }
                }
        }
    }
}
