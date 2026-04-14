import java.util.Scanner;

public class Prog8
{ 
  static double area (float r)
   { return ( 3.142*r*r);}
  static double circumference (float r)
   { return (2*3.142*r);}

  public static void main (String[] args)
  {
    Scanner a = new Scanner(System.in);
    System.out.print("Enter the radius: ");
    int x = a.nextInt();
    double carea = area(x);
    double circum = circumference(x);
    System.out.println("Area of the circle is: "+ carea);
    System.out.println("Circumference of the circle is: "+ circum);
  }
}
