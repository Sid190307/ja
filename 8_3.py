class Shape{
String name;
Shape(String name){
this.name = name;
}
void displayShapeName(){
System.out.println(&quot;Shape Name:&quot;+name);
}
}
class Circle extends Shape{
int rad;
double area;
Circle(String name , int rad){
super(name);
this.rad = rad ;
}
void calarea(){
area = 3.14 * rad * rad ;
}
void displayCirarea(){
displayShapeName();
calarea();
System.out.println(&quot;Area of Circle:&quot;+area);

}
}
class Rectangle extends Shape{
int l;
int b;
int area;
Rectangle(String name,int l,int b){
super(name);
this.l = l;
this.b = b;
}
void calarea(){
area = l * b;
}

void displayRectarea(){
displayShapeName();
calarea();
System.out.println(&quot;Area of Rectangle:&quot;+area);
}
}

public class prog3{
public static void main(String [] args){
Circle cir1 = new Circle(&quot;Circle&quot;,5);
Rectangle rect1 = new Rectangle(&quot;Rectangle&quot;,10,5);

cir1.displayCirarea();
rect1.displayRectarea();
}
}
