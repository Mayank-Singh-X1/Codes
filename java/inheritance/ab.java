

//multilevel inheritance

class A{
    void jsdsj(){
        System.out.println("shhds");
    }
    void display(){
        System.out.println("I am in class A");
    }
}
class B extends A{
    void display(){
        System.out.println("I am in class B");
    }
}

class C extends B{
    void display(){
        System.out.println("I am in class C");
    }
}
public class ab {
    public static void main(String[] args) {
        B b = new B();

        b.jsdsj();
    }
}
