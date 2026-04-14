-abstract class Animal { 
 abstract void sound(); // Abstract method, must be implemented by subclasses  void breathe() { 
 System.out.println("Breathing..."); 
 } 
} 
class Dog extends Animal { 
 @Override 
 void sound() { 
 System.out.println("Bark");
 } 
} 
