import java.util.Arrays;
import java.util.Scanner;

class Employee
{ int id;
  String name;
  int exp;
  int sal;
  public Employee(int nid, String nname, int nexp, int nsal)
   { id = nid;
     name = nname;
     exp = nexp;
     sal = nsal;
   }
}

public class Prog4
{ public static void main(String[] args)
  { 
    Employee arr[] = new Employee[5];
    int i=0;
    Scanner a = new Scanner(System.in);
    while(i<1)
     { System.out.print("Enter employee id: ");
       int id;
       id = a.nextInt();
       System.out.print("Enter employee name: ");
       String name;
       name = a.next();
       System.out.print("Enter employee experience: ");
       int exp;
       exp = a.nextInt();
       System.out.print("Enter employee salary: ");
       int sal;
       sal = a.nextInt();
       if (exp>10)
        { sal += sal*0.5;}
       arr[i] = new Employee(id, name, exp, sal);
       i++;
     }
    System.out.print("Enter the id to find: ");
    int x = a.nextInt();
    i = 0;
    while(i<1)
     { if (arr[i].id == x)
        { System.out.println("Name: "+arr[i].name);
          System.out.println("ID :"+arr[i].id);
          System.out.println("Experience :"+arr[i].exp);
          System.out.println("Salary :"+arr[i].sal);
        }
       else 
        { System.out.print("ID not found");}
       i++;
     }
  }
}
