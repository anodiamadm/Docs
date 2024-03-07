import java.util.ArrayList;
import java.util.List;
public class Human_Resource {
    public void add_Employees()
    {
        List<Employee> lstEmployee = new ArrayList<Employee>();
        Employee emp = new Employee();

        emp.setID(1);
        emp.setCode("E001");
        emp.setName("John");
        emp.setSalary(20000);
        lstEmployee.add(emp);

        emp = new Employee();
        emp.setID(2);
        emp.setCode("E002");
        emp.setName("Rajesh");
        emp.setSalary(30000);
        lstEmployee.add(emp);

        System.out.println("No Employees: " + lstEmployee.size());
        for(int i=0;i< lstEmployee.size();i++)
        {
            System.out.println("Employee " + (i+1));
            System.out.println("Employee Id: " + lstEmployee.get(i).getID());
            System.out.println("Employee Code: " + lstEmployee.get(i).getCode());
            System.out.println("Employee Name: " + lstEmployee.get(i).getName());
            System.out.println("Employee Salary: " + lstEmployee.get(i).getSalary());

        }


    }
}
