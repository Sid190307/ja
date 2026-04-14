class Animal{
	public String sound(){
		return "animal sound";
	}
}

class dog extends Animal{
	@Override
	public String sound(){
		return "bark";
	}
}

class cat extends Animal{
	@Override
	public String sound(){
		return "meow";
	}
}

class ovr{
	public static void main(String[] args){
		dog d = new dog();
		cat c = new cat();
		System.out.println(d.sound());
		System.out.println(c.sound());
	}
}
