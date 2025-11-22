import java.util.*;
public class Sorting {

    public static void printarr(int x[]){
        for(int i=0;i<x.length;i++){
            System.out.print(x[i]+" ");
        }}


    public static void main(String[] args) {
        Scanner sc= new Scanner (System.in);

        //Bubble sort
        
        // int arr[]={21,54,8,67,100,10,2,6};
        // for(int i=0; i<arr.length-1;i++){
        //     for(int j=0;j<arr.length-1-i;j++){
        //         if(arr[j]>arr[j+1]){
        //             int temp=arr[j];
        //             arr[j]=arr[j+1];
        //             arr[j+1]=temp;
        //         }}}


        //Selection sort

        int arr[]={8,4,9,2,1,7};
    
        for (int i = 0; i < arr.length - 1; i++) {
        int smallest = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[smallest]) {
                    smallest = j;
                }
            }
            // Swap the found minimum element with the first element
        int temp = arr[smallest];
        arr[smallest] = arr[i];
        arr[i] = temp;
        }


    printarr(arr);
       sc.close();
    }
    
}
