class Animal
{
  void eat()
  { System.out.println("Animal is eating");}
}

class Dog extends Animal
{
  void bark()
  { System.out.println("Dog is barking");}
}

class BabyDog extends Dog
{
  void weep()
  { System.out.println("Baby dog is weeping");}
}

public class Prog5
{
  public static void main(String[] args)
  {
    BabyDog dog = new BabyDog();
    dog.eat();
    dog.bark();
    dog.weep();
  }
}
