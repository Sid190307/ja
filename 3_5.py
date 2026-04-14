import java.util.Scanner;

public class Prog5
{
  static float average(float a, float b, float c)
   { return ( (a+b+c)/3 ); }

  public static void main(String[] args)
  { 
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter three numbers: ");
    int x = scanner.nextInt();
    int y = scanner.nextInt();
    int z = scanner.nextInt();
    float avg = average(x,y,z);
    System.out.println("The average of the numbers is: "+avg);
  }
}
