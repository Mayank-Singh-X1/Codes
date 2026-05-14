import java.util.*;
public class GEo_tripets {
    public static void main(String[] args) {
        //find geometric triplets in an array
        //output: {3,9,27}, {9,18, 36}
        int []arr={9,3,18,64, 2, 8, 32, 27, 36};
        int n=arr.length;
        Arrays.sort(arr);
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                for(int k=j+1; k<n; k++){
                    if(arr[j]*arr[j]==arr[i]*arr[k]){
                        System.out.println("{"+arr[i]+","+arr[j]+","+arr[k]+"}");
                    }
                }
            }
        }
    }
}

