public class Prog1
{ static int add (int a, int b)
   { return (a+b);}

  static int sub (int a, int b)
   { return (a-b);}

  static int mul (int a, int b)
   { return (a*b);}

  static float div (int a, int b)
   { return (a/b);}

  public static void main(String[] args)
   { 
     System.out.println("The addition of 10 and 5 is: "+ add(10,5));
     System.out.println("The subtraction of 10 and 5 is: "+ sub(10,5));
     System.out.println("The multiplication of 10 and 5 is: "+ mul(10,5));
     System.out.println("The division of 10 and 5 is: "+ div(10,5));
   }
}
