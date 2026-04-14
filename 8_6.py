class Shape
{
  void draw()
  { System.out.println("Drawing a shape");}
}

class Circle extends Shape
{
  @Override
  void draw()
  { System.out.println("Drawing a circle");}
}

class Rectangle extends Shape
{
  @Override
  void draw()
  { System.out.println("Drawing a rectangle");}
}

public class Prog6
{ 
  public static void main(String[] args)
  {
    Circle cir = new Circle();
    Rectangle rect = new Rectangle();

    cir.draw();
    rect.draw();
  }
}
