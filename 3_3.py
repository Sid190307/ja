public class Prog3
{ 
  static double volume (int r, int h)
   { return( 3.142*r*r*h );}
  static double volume (int r)
   { return ( (4/3)*3.142*r*r*r );}
  static double volume (int l, int b, int h)
   { return ( l*b*h );}

  public static void main(String[] args)
  { System.out.println("The volume of the cylinder is: "+ volume(5,7));
    System.out.println("The volume of the sphere is: "+ volume(5));
    System.out.println("The volume of the cuboid is: "+ volume(5,7,2));
  }
}
