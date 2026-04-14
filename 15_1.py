// Abstract class with an abstract method 
abstract class Animal { 
 // Abstract method (no implementation) 
 abstract void makeSound(); 
} 
class Dog extends Animal { 
 // Provide implementation for the abstract method 
 void makeSound() { 
 System.out.println("Bark"); 
 } 
} 
public class Main { 
 public static void main(String[] args) {
 Animal dog = new Dog(); 
 dog.makeSound(); // Output: Bark 
 } 
} 
