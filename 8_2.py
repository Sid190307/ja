class Person{
String name;
int age;
Person(String name,int age){
this.name = name;
this.age = age;
}
void displayInfo(){
System.out.println(&quot;Person Name: &quot;+name+ &quot;,Person Age :&quot;+age);
}
}
class Student extends Person{
int Studentid;
Student(String name,int age,int Studentid){
super(name,age);
this.Studentid = Studentid;
}
void displayStudentInfo(){
displayInfo();
System.out.println(&quot;Student ID:&quot;+ Studentid);
}
}
class Graduate extends Student{
String field ;
Graduate(String name, int age,int Studentid, String field){

super(name,age,Studentid);
this.field = field;
}
void displayGraduateInfo(){
displayStudentInfo();
System.out.println(&quot;Graduate field:&quot;+field);
}
}
public class prog2{
public static void main(String [] args){
Graduate grad1= new Graduate(&quot;Gaurav&quot;,18,101,&quot;Computer Science&quot;);
grad1.displayGraduateInfo();
}
}
