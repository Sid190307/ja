Hi
Hello
Good Morning !!

import java.io.FileInputStream;
public class Allchar {
public static void main(String args[]){
try{
FileInputStream fin=new FileInputStream(&quot;file.txt&quot;);
int i=0;
while((i=fin.read()) !=- 1){
System.out.print((char)i);
}
fin.close();
}catch(Exception e){System.out.println(e);}
}
}
