public class Prog9
{
  static void area (int a , int base, int height)
   { double x = (1.73/4)*a*a;
     double y = 0.5*base*height;
     System.out.println("Area of equilateral triangle: "+ x);
     System.out.println("Area of right angled triangle: "+ y);
   }

  public static void main(String[] args)
  {
    int a=5, b=3, h=4;
    area(a,b,h);
  }
}
