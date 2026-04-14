interface Animal { 
 void sound(); // Abstract method 
} 
interface Playable { 
 void play(); // Abstract method 
}
class Dog implements Animal, Playable { 
 @Override 
 public void sound() { 
 System.out.println("Bark"); 
 } 
 @Override 
 public void play() { 
 System.out.println("Playing fetch!"); 
 } 
} 
