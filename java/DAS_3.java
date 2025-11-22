import java.util.*;
public class DAS_3 {
    public static void main(String[] args) {
       //Bit manipulation
        Scanner sc= new Scanner(System.in);
        
        //Get bit
        int a=5; //0101
        int pos =2;
        int bitmask=a<<pos;
        System.out.println(bitmask);
        // if((bitmask & a)==0){
        //     System.out.println("Bit was zero");
        // }else{
        //     System.out.println("Bit was one");
        // }

        sc.close();
    }
}
