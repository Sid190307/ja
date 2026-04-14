import java.util.Scanner;

class prog3{
	public static void main(String[] args){
		Scanner a = new Scanner(System.in);
		try{
			System.out.print("Enter a number: ");
			String x = a.nextLine();
			int num1 = Integer.parseInt(x);

			System.out.print("Enter a number: ");
			String y = a.nextLine();
			int num2 = Integer.parseInt(y);			

			try{
				int div;
		
				div = num1/num2;
				System.out.println("The division is: "+div);
			}
			catch(ArithmeticException e)
				{ System.out.println(e); }
		}
		catch(NumberFormatException e) 
			{System.out.println(e);}
	}
}
