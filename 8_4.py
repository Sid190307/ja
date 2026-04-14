class Employee
{
  int salary;
  Employee(int salary)
  { this.salary = salary;}
}

class Programmer extends Employee
{
  int bonus;
  Programmer(int salary, int bonus)
  { 
    super(salary);
    this.bonus = bonus;
  }
  
  void display()
  {
    System.out.println("Total income: "+(salary + bonus));
  }
}

public class Prog4
{
  public static void main(String[] args)
  {
    Programmer per1 = new Programmer(45000, 5000);
    per1.display();
  }
}
