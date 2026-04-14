import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadFile
{
public static void main(String[] args)
{
// Reading File
try {
File Obj = new File(&quot;myfile.txt&quot;);
Scanner Reader = new Scanner(Obj);

// Traversing File Data
while (Reader.hasNextLine()) {
String data = Reader.nextLine();
System.out.println(data);
}

Reader.close();

}

// Exception Cases
catch (FileNotFoundException e) {
System.out.println(&quot;An error has occurred.&quot;);
e.printStackTrace();
}
}
}
