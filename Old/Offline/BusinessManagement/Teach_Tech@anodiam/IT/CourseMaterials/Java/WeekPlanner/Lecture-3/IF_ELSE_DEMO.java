import java.util.*;

public class IF_ELSE_DEMO {
    // Java program to illustrate if-else statement

        public static void main(String args[])
        {
            Scanner sc = new Scanner(System.in);
            System.out.println("Please enter a number");
            int i = sc.nextInt();

            if (i < 15)
                System.out.println("i is smaller than 15");
            else
                System.out.println("i is greater than 15");

            System.out.println("Outside if-else block");
        }


}
