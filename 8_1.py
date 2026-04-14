class Vehicle{
String make;
String model;
Vehicle(String make,String model){
this.make=make;
this.model=model;
}
void displayInfo(){
System.out.println("Vehicle Make: "+ make+", Model: "+model);
}
}
class Car extends Vehicle{
String type;
Car(String make, String model, String type){
super(make,model);
this.type=type;
}
void displayCarInfo(){
displayInfo();
System.out.println("Vehicle Type: "+ type);
}
}
public class Prog1{
public static void main(String [] args){
Car car1= new Car( "Mach-e","GT", "Sports Car");
car1.displayCarInfo();
}
}
