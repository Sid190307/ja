abstract class vehicle{
abstract void start();

abstract void stop();
}



class car extends vehicle{

@Override
public void start(){
System.out.println("Car is starting...");
}

@Override
public void stop(){
System.out.println("The  vehicle has stopped...");
}

}

class bike extends vehicle{

@Override
public void start(){
System.out.println("Bike is starting...");
}

@Override
public void stop(){
System.out.println("The  vehicle has stopped...");
}
}

public class pro4{
public static void main(String args[]){
car  c = new car();
bike b = new bike();
c.start();
c.stop();
b.start();
b.stop();
}
}
