import java.util.*;
import DSA.Advance_recursions;


class students {
    static{
        System.out.println("dfkdkoghdfjhgkdjfn");
    }
    students(){
        System.out.println("kaa be");
    }
    students(int a){
        this.rollno=a;
        System.out.println("kaa be " + a);
    }

    String name;
    int rollno;
    float marks;

    void display() {
        System.out.println("Name: " + name);
        System.out.println("Roll No: " + rollno);
        System.out.println("Marks: " + marks);
        System.out.println();
    }
    // static void sd(){
    //     System.out.println("djhfdgh" + name);
    // }
}


public class Studdents {
    public static void main(String[] args) {
        Integer a=16;   
        

        // students.sd();
        System.out.println();

        students s1 = new students();
        s1.name = "John";
        s1.rollno = 1;
        s1.marks= 85;

        students s2 = new students();   
        s2.name="dd";
        s2.rollno=2;
        s2.marks=34.5f;

        students s3 = new students(4);
        s3=s1;

        System.out.println();

        Advance_recursions.printperm("abc", "");
    }
}
