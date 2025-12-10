import java.util.*;
public class DSA_4 {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
        String a="lhello";
        StringBuilder sb= new StringBuilder(a);

        for(int i=0;i<sb.length()-1;i++){
            int front=i;
            int back=sb.length()-1-i;

            char frontchar=sb.charAt(front);
            char backchar=sb.charAt(back);

            sb.setCharAt(front, backchar);
            sb.setCharAt(back, frontchar);
        }
        System.out.println(sb);
    

       sc.close(); 
    }
    
}
