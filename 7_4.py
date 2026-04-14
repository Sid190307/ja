#EMPLOYEE
public class Employee
{
  private String name;
  private String jobTitle;
  private double salary;

  public Employee(String name, String jobTitle, double salary)
  {
    this.name = name;
    this.jobTitle = jobTitle;
    this.salary = salary;
  }
  
  public String getName()
  {
    return name;
  }
  
  public void setName(String name)
  {
    this.name = name;
  }
  
  public String getjobTitle()
  {
    return jobTitle;
  }
  
  public void setjobTitle(String jobTitle)
  {
    this.jobTitle = jobTitle;
  }

  public double getsalary()
  {
    return salary;
  }
  
  public void setSalary(double salary)
  {
    this.salary = salary;
  }
  
  public void raiseSalary(double percentage)
  {
    salary = salary + salary * percentage / 100;
  }
  
  public void printEmployeedetails()
  {
    System.out.println("Name: "+name);
    System.out.println("Job Title: "+jobTitle);
    System.out.println("Salary: "+salary);
  }
}

#MAIN
public class Main
{
  public static void main(String[] args)
  {
    Employee emp1 = new Employee("Ramesh", "HR Manager",40000);
    Employee emp2 = new Employee("Suresh", "Software Engineer",60000);
    System.out.println("\nEmployee Details: ");
    emp1.printEmployeedetails();
    emp2.printEmployeedetails();

    emp1.raiseSalary(8);
    emp2.raiseSalary(12);

    System.out.println("\nAfter raising salary: ");
    System.out.println("\n8% for 'Ramesh': ");
    emp1.printEmployeedetails();
    System.out.println("\n12% for 'Suresh': ");
    emp2.printEmployeedetails();
  }
}
