class Person
{
  public String name;
  private int age;
  protected String jobTitle;
  String Address;
  
  public Person(String name, int age, String jobTitle, String Address)
  {
    this.name = name;
    this.age = age;
    this.jobTitle = jobTitle;
    this.Address = Address;
  }
  
  public void displayPublicInfo()
  { System.out.println("Name: "+name); }

  public void displayPrivateInfo()
  { System.out.println("Age: "+age); }

  public void displayProtectedInfo()
  { System.out.println("Job Title: "+jobTitle); }

  public void displayDefaultInfo()
  { System.out.println("Address: "+Address); }
}

class Employee extends Person
{
  public Employee(String name, int age, String jobTitle, String Address)
  { super(name,age,jobTitle,Address); }
  
  public void displayEmployeeInfo()
  {
    System.out.println("Employee Name(from public field): "+name);
    // System.out.println("Employee age(from private field): "+age);
    System.out.println("Employee Job Title(from protected field): "+jobTitle);
    System.out.println("Employee Address(from default field): "+Address);
    
    displayPublicInfo();
    // displayPrivateInfo();
    displayProtectedInfo();
    displayDefaultInfo();
  }
}

public class TestAccess
{
  public static void main(String[] args)
  {
    Person person = new Person("Johnathan Wick",50,"Contracts","21st Jump Street");
    System.out.println("\nAccessing public field from person: "+person.name);
    person.displayPublicInfo();
    
    // System.out.println(person.age);
    // person.displayPrivateInfo();
    
    System.out.println("\nAccessing protected field from person: ");
    person.displayProtectedInfo();
    
    System.out.println("\nAccessing default field from person: ");
    person.displayDefaultInfo();

    System.out.println("\n");
    
    Employee employee = new Employee("Ethan Hunt",45,"Spy agent","Unknown");
    employee.displayEmployeeInfo();
  }
}

