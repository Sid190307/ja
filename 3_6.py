public class Prog7
{ 
  static void leapyear(int a)
   { if ( (a%4)==0 & (a%100)!=0 || (a%400)==0 )
      { System.out.println("The given year is leap year");}
     else
      { System.out.println("The given year is not a leap year");}
   }

  public static void main (String[] args)
  { 
    Scanner y = new Scanner(System.in);
    System.out.print("enter the leap year: ");
    int x = y.nextInt();
    leapyear(x);
  }
}
