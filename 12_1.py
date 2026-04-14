Hi
Hello
Good Morning !!

import java.io.FileInputStream;
public class Files {
public static void main(String args[]){
try{
FileInputStream fin= new FileInputStream(&quot;file.txt&quot;);
int i = fin.read();
System.out.print((char)i);
fin.close();
}

catch(Exception e){System.out.println(e);
}
}
}
