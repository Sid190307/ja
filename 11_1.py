import java.io.*;

class prog1{
	public static void main(String[] args){
		try{
		   int n = 50/0;
		} 
		catch(ArithmeticException e){System.out.println(e);}

		try{
		   String s = "Hello";
		   System.out.println(Integer.parseInt(s));
		} 
		catch(NumberFormatException e){System.out.println(e);}

		try{
		   int arr[] = {1,2,3,4};
		   System.out.println(arr[11]);
		}
		catch(ArrayIndexOutOfBoundsException e)
			{ System.out.println(e); }

		try{
		   String u = null;
		   System.out.println(u.toUpperCase());
		}
		catch(NullPointerException e){ System.out.println(e);}

		try{
		   FileInputStream file = new FileInputStream("abc.txt");
		}
		catch(FileNotFoundException e){ System.out.println(e);}

		try{
		   throw new IOException("Manual I/O Trigger");
		}
		catch(IOException e){ System.out.println(e);}
	}
}
