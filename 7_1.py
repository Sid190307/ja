class Student
{ 
  String name;
  int roll_no;
}

class Ans
{ 
  public static void main(String[] args)
  {
    Student s = new Student();
    s.name = "john";
    s.roll_no = 3;
    System.out.println("Name is "+s.name+" and roll number "+s.roll_no);
  }
}
