import java.util.*;

public class A_Word {
    public static boolean issmall(char c) {
        if (c >= 'a' && c <= 'z') {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        int scount = 0;
        for (int i = 0; i < s.length(); i++) {
            if (issmall(s.charAt(i))) {
                scount++;
            }
        }
        String ans="";
        int ccount=s.length()-scount;
        if(scount >= ccount){
        //    StringBuilder answer =//
           ans=s.toLowerCase();
        }else{
            ans=s.toUpperCase();
        }
        System.out.println(ans);

    }
}