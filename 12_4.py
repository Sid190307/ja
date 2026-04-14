import java.io.File;
import java.io.IOException;
public class CreateFile
{

public static void main(String[] args)
{

try {
File Obj = new File(&quot;myfile.txt&quot;);

// Creating File
if (Obj.createNewFile()) {
System.out.println(&quot;File created: &quot; + Obj.getName());
}
else {
System.out.println(&quot;File already exists.&quot;);
}
}

// Exception Thrown
catch (IOException e) {
System.out.println(&quot;An error has occurred.&quot;);
e.printStackTrace();
}
}
}
