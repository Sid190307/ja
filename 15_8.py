interface printable{
void print();

}

class document implements printable{
@Override
public void print(){
System.out.println("Printing document...."); 
}
}

class photo implements printable{
@Override
public void print(){
System.out.println("Printing photo...."); 
}
}

public class pro7{
public static void main(String args[]){
document  d = new document();
photo p = new photo();
d.print();
p.print();
}
