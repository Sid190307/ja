import java.util.Scanner;

public class Prog4
{ 
  static void smallest(int a, int b, int c)
   {
     if (a<b & a<c)
      { System.out.println(a+" is the smallest number amongst the three");}
     else if (b<a & b<c)
      { System.out.println(b+" is the smallest number amongst the three");}
     else if (c<a & c<b)
      { System.out.println(c+" is the smallest number amongst the three");}
   }

  public static void main(String[] args)
  { 
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter three numbers: ");
    int n1 = scanner.nextInt();
    int n2 = scanner.nextInt();
    int n3 = scanner.nextInt();
  
    smallest(n1,n2,n3);
  }
