

class shape{
    public void display() {
        System.out.println("shape");
    }
}

class circle extends shape{
    @Override
    public void display() {
        System.out.println("circle");
    }
}

//Method overridding

public class poly {
    public static void main(String[] args) {
        shape c = new circle();
        c.display();
    }
}


//DYnamic method dispatcher  (java)
// virtual table / virtual pointer (c++)
//judge which decides which method will be called either of child or parent during runtime poly (method overridding)


//when class is final all its methods are final i.e they cannot be inherited and overridden

//static var does not depend on objects but overrridingn depends on objects