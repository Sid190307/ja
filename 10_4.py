class Bank{
	public double getInterestRate(){
		return 0;
	}
}

class SBI extends Bank{
	@Override
	public double getInterestRate(){
		return 6.5;
	}
}

class ICICI extends Bank{
	@Override
	public double getInterestRate(){
		return 7.0;
	}
}

class interest{
	public static void main(String[] args){
		SBI a = new SBI();
		ICICI b = new ICICI();
		System.out.println(a.getInterestRate());
		System.out.println(b.getInterestRate());
	}
}
