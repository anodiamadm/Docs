public class StringExample {
    public static void main(String[] args) {
        /*
        // create strings
        String first = "Java";
        String second = "Python";
        String third = "JavaScript";

        // print strings
        System.out.println(first);   // print Java
        System.out.println(second);  // print Python
        System.out.println(third);   // print JavaScript
*/
        /* Wrapper class
        Examples
         */

        // create primitive types
        int a = 5;
        double b = 5.65;

        //converts into wrapper objects
        Integer aObj = Integer.valueOf(a);
        Double bObj = Double.valueOf(b);

        if(aObj instanceof Integer) {
            System.out.println("An object of Integer is created.");
        }

        if(bObj instanceof Double) {
            System.out.println("An object of Double is created.");
        }
    }
}
