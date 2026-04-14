import java.util.Arrays;
import java.util.Scanner;

class Student
{ int id;
  String name;
  public Student(int nid, String nname)
   { id = nid;
     name = nname;
   }
}

public class Prog3
{ public static void main(String[] args)
  { 
    Student arr[] = new Student[5];
    int i=0;
    Scanner a = new Scanner(System.in);
    while(i<3)
     { System.out.print("Enter your id: ");
       int id;
       id = a.nextInt();
       System.out.print("Enter your name: ");
       String name;
       name = a.next();
       arr[i] = new Student(id, name);
       i++;
     }
    int x = 0;
    System.out.print("Enter the id you want to find: ");
    x = a.nextInt();
    i=0;
    while(i<3)
     { if (arr[i].id == x)
        { System.out.print("Name: "+arr[i].name);
          System.out.print("  ID :"+arr[i].id);
        }
       else 
        { System.out.print("ID not found");}
       i++;
     }
  }
}
