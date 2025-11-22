import java.util.*;


    class Animal{
        public void makesound(){
            System.out.println("woof");
        }}

    class pig extends Animal{
        @Override
        public void makesound(){
            System.out.println("kyu re madhar chod");
        }
    }
    public class dfain{
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        Animal a= new Animal();
        a.makesound();;
        sc.close();
    }
}