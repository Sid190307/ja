import java.util.Scanner;

public class Prac4
{ 
  public static void main (String[] args)
 {
   Scanner a = new Scanner(System.in);
   System.out.println("Enter two strings (Each on new line)");
   String txt1 = a.nextLine();
   String txt2 = a.nextLine();
   
   System.out.println("\n1. String at position 0 for first string: "+ txt1.charAt(0));

   System.out.println("\n2. Length of the first String : "+ txt1.length());

   System.out.println("\n3. Comparing both Strings : "+ txt1.compareTo(txt2));

   System.out.println("\n4. First String in Uppercase : "+ txt1.toUpperCase());
   System.out.println("\n5. Second String in Lowercase : "+ txt2.toLowerCase());

   System.out.println("\n6. First String contains 'q' : "+ txt1.contains("q"));

   System.out.println("\n7. Concatenating strings : "+ txt1.concat(txt2));

   System.out.println("\n8. Index of 'o' in the first string : "+ txt1.indexOf("o"));

   System.out.println("\n9. Checking whether a first string is empty or not : "+ txt1.isEmpty());

   System.out.println("\n10. The substring in the first string is : "+ txt1.substring(2,4));

   System.out.println("\n11. Last Index no of the first string is : "+ txt1.lastIndexOf("l"));

   System.out.println("\n12. Trimming first string : "+ txt1.trim());

   System.out.println("\n13. Checking whether second string is ending with 'e' : "+ txt1.endsWith("e"));

   System.out.println("\n14. Replacing 'lo' in first string with 'olol' : "+ txt1.replace("lo","olol"));

   System.out.println("\n15. Matching the first string  : "+ txt1.matches("Wo.*"));

   System.out.println("\n16. Replacing all 'l' with 'u' in first string : "+ txt1.replaceAll("l","u"));

   System.out.println("\n17. Equals Ignore case  : "+ txt1.equalsIgnoreCase(txt2));

   System.out.println("\n18. reapeating the first string 5 times  : "+ txt1.repeat(4));

   System.out.println("\n19. Checking whether first string starts with 's' : "+ txt1.startsWith("S"));

   System.out.println("\n20. Converting the first string into an array : ");
   char[] array = txt1.toCharArray();
   for (char c : array)
    { System.out.print(c +" ");}

}
}
