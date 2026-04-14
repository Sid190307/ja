import java.io.File;

public class DeleteFile

{
public static void main(String[] args)
{
File Obj = new File(&quot;myfile.txt&quot;);

// Deleting File
if (Obj.delete()) {
System.out.println(&quot;The deleted file is : &quot; + Obj.getName());

}
else {
System.out.println(
&quot;Failed in deleting the file.&quot;);
}
}
}

