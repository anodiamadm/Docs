import java.util.*;
public class TestArray {
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);

        String employees[] = new String [5];
        /*employees[0] = "Deb";
        employees[1] = "Amitabh";
        employees[2] = "Raja";
        employees[3] = "Shub";
        employees[4] = "Dhirendra";*/
        System.out.println("Please enter the names of the employees:-");
        for (int i = 0; i< employees.length; i++)
        {
            employees[i] = sc.nextLine();
        }
        System.out.println("The list of employees :");
        for (int i = 0; i< employees.length; i++)
        {
            System.out.println(employees[i]);
        }

    }
}
