import java.util.Scanner;
public class Employee {

    private Integer id;
    private String code;
    private String name;
    private String address;
    private Double salary;

    public void getEmployeeDetails()
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Employee Details");
        System.out.println("----------------------");
        System.out.print("Enter Employee Id: ");
        id=sc.nextInt();
        
        System.out.print("Enter Employee Code: ");
        code=sc.nextLine();
        sc.close();
    }
    public static void main(String[] args) {
        Employee objEmployee=new Employee();
        objEmployee.getEmployeeDetails();
    }
}