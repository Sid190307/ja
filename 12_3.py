import java.io.FileOutputStream;
import java.io.OutputStream;

public class Outputstream {

public static void main(String args[]) {
String data = &quot;This is Fybsc java&quot;;

try {
OutputStream out = new FileOutputStream(&quot;output.txt&quot;);

// Converts the string into bytes
byte[] dataBytes = data.getBytes();

// Writes data to the output stream
out.write(dataBytes);
System.out.println(&quot;Data is written to the file.&quot;);

// Closes the output stream
out.close();

}

catch (Exception e) {
e.getStackTrace();

}
}
}
