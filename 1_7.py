public class Prog7
{
  public static void main(String[] args)
{
  int n1 = 10;
  int n2 = 5;
  int n3 = 11;
  if (n1>n2 && n1>n3)
   { System.out.println(n1+" is the largest number");}
  else if (n2>n1 && n2>n3)
   { System.out.println(n2+" is the largest number");}
  else if (n3>n1 && n3>n2)
   { System.out.println(n3+" is the largest number");}
  System.out.print("The smallest number is: ");
  if (n1<n2 && n1<n3)
   { System.out.print(n1);}
  else if (n2<n1 && n2<n3)
   { System.out.print(n2);}
  else if (n3<n1 && n3<n2)
   { System.out.print(n3);}
}
}
