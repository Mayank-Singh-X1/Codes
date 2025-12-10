public class practice{

    public static void tower(int n,String src, String sux, String dest ){
        if(n==1){
            System.out.println("move disk "+n+" from "+src+" to "+ dest);
            return;
        }
        tower(n-1, src, dest , sux);
        System.out.println("move disk "+n+" from "+src+" to "+ dest);
        tower(n-1, sux, src, dest);

    }
    public static void main (String []args){
     tower(1, "A", "B", "C");

        }
    }
    

