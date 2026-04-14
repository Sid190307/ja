class Shape{
	public int area(int side){
		return side*side;
	}
	
	public int area(int length, int breadth){
		return length*breadth;
	}
	
	public double area(double radius){
		return 3.14*radius*radius;
	}
}

class Area{
	public static void main(String[] args){
		Shape s = new Shape();
		System.out.println("Area of square: "+s.area(5));
		System.out.println("Area of rectangle: "+s.area(5,2));
		System.out.println("Area of square: "+s.area(2.4));
	}
}
