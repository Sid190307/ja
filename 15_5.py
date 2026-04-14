abstract class shape{
abstract void area();
}

class circle extends shape{
int r;
double a;

circle(int r){
this.r = r;
}

@Override
public void area(){
a = 3.14*r*r;
System.out.println("The area of circle is : "+a); 
}
}

class rectangle extends shape{
int l,b,a;

rectangle(int l,int b){
this.l = l;
this.b = b;
}

@Override
public void area(){
a = l*b;
System.out.println("The area of rectangle is : "+a); 
}
}

public class pro5{
public static void main(String args[]){
circle  c = new circle(5);
rectangle r = new rectangle(2,5);
c.area();
r.area();
}
}
