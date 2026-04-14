public class Prog11
{
public static void main(String[] args)
{
int start = 1;
int end = 30;

for (int num = start; num <= end; num++)
      {
	int count = 0;
	for (int i = 1; i <= num; i++)
	      {	
		if (num % i == 0)
		      {
			count = count + 1;
		      }
	      }
	if (count == 2)
	     {
		System.out.println("Prime numbers between 1-30 :-" + num);
	     }
      }     
}
}
