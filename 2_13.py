public class Prog13
{
public static void main(String[] args)
{
int num = 121;
int temp = num;
int rev = 0;

while (temp > 0)
      {
	int digit = temp % 10;
	rev = rev * 10 + digit;
	temp = temp / 10;
      }

if (rev == num)
      {
	System.out.println(num + "is Palindrome");
      }
else
      {
	System.out.println(num + "is Not a Palindrome");
      }
}
}
