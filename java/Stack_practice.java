import java.util.*;
public class Stack_practice {
    public static void main(String[] args) {
        Deque <String> stack=new ArrayDeque<>();
        System.out.println(stack.isEmpty());

        stack.push("kela");
        stack.push("papaiya");
        stack.push("anannaas");

        System.out.println(stack.isEmpty());
        stack.pop();
        System.out.println(stack);



    }
    
}
