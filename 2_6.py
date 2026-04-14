public class Prog6
{
public static void main(String[] args)
{
int num = 1234567, temp = num, count= 0;
while(temp!=0)
{
temp = temp/10;
count = count + 1;
}
System.out.println("The number of digits in" + num + "is :" + count);

}
}
