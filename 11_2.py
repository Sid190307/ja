import java.util.Scanner;

class NegativeNumberException extends Exception{
	public NegativeNumberException(String message){
		super(message);
	}
}

public class prog2{
	public static void checkandsquare(int number) throws NegativeNumberException{
		if (number < 0){
			throw new NegativeNumberException("negative numbers not allowed");
		}
		else {
			System.out.println("The square of "+ number +" is: "+ (number*number));
		}
	}

	public static void main(String[] args){
		Scanner a = new Scanner(System.in);
		
		try{
		   System.out.println("Enter an integer: ");
		   int number = a.nextInt();

		   checkandsquare(number);
		}
		catch (NegativeNumberException e){
			System.out.println(e.getMessage());
		}
		catch (Exception e){
			System.out.println("invalid input");
		}
		finally{
			System.out.println("Program executed");
		}
	}
}
