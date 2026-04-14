import java.io.FileWriter;
import java.io.IOException;

public class WriteFile
{
public static void main(String[] args)

{
// Writing Text File
try {

FileWriter Writer = new FileWriter(&quot;myfile.txt&quot;);

// Writing File
Writer.write(&quot;Files in Java are seriously good!!&quot;);
Writer.close();

System.out.println(&quot;Successfully written.&quot;);
}

// Exception Thrown
catch (IOException e) {
System.out.println(&quot;An error has occurred.&quot;);
e.printStackTrace();
}
}
}
