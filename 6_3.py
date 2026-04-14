1.	Scanner
Code:
import java.util.Scanner;

public class Prog3 
{
    public static void main(String[] args) 
{

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        System.out.println("You entered: " + n);
    }
}


2.	Random
Code:
import java.util.Random;

public class Prog4 
{
    public static void main(String[] args) 
{

        Random r = new Random();

        int num = r.nextInt(10); // generates number from 0 to 9

        System.out.println("Random number: " + num);
    }
}
