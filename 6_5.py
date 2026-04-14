1.	Write
Code:
public class Prog7 
{
    public static void main(String[] args) throws Exception 
{

        FileWriter fw = new FileWriter("data.txt");

        fw.write("Welcome to Java IO"); // write() function
        fw.close();

        System.out.println("File written successfully");
    }
}




2.	Read
Code:
package forest;
import java.util.*;

public class Tiger
{ 
  public void getDetails(String nickName, int weight)
  {
    System.out.println("Tiger nick name is: "+ nickName);
    System.out.println("Tiger weight is: "+ weight);
  }
}


Package for Lion:
package forest;
import java.util.*;

public class Lion
{ 
  public void getDetails(String nickName, int weight)
  {
    System.out.println("Lion nick name is: "+ nickName);
    System.out.println("Lion weight is: "+ weight);
  }
}

Package for elephant:
package forest;
import java.util.*;

public class Elephant
{ 
  public void getDetails(String nickName, int weight)
  {
    System.out.println("Elephant nick name is: "+ nickName);
    System.out.println("Elephant weight is: "+ weight);
  }
}

Main program:
import forest.Tiger;
import forest.Lion;
import forest.Elephant;

public class Prog
{
  public static void main(String args[])
  {
    Tiger t1= new Tiger();
    t1.getDetails("Sheru",50);
    
    Lion l1 = new Lion();
    l1.getDetails("Mufasa",100);
    
    Elephant e1 = new Elephant();
    e1.getDetails("Padmanabhan",170);
  }
}
