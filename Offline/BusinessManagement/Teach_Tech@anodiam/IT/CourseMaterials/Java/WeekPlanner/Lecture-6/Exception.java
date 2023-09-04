public class Main {
    public static void main(String[] args) {
        try{
            int data = 100/0;
        }catch (ArithmeticException e) {System.out.println(e);}
        //rest of code of the program
        System.out.println("rest of the code.....");
    }
}