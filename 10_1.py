class calculator{
	public int add(int a, int b){
		return a+b;
	}

	public double add(double a, double b){
		return a+b;
	}

	public int add(int a, int b, int c){
		return a+b+c;
	}
}

class clac{
	public static void main(String[] args){
		calculator c = new calculator();
		System.out.println("addition of two int num is "+c.add(5,2));
		System.out.println("addition of two double num is "+c.add(5.4,2.7));
		System.out.println("addition of three int num is "+c.add(5,2,8));
	}
}
