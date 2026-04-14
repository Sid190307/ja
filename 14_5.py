class MyThread extends Thread {
    public void run() {
        System.out.println("Hello, World!");
    }
}

public class SimpleThread {
    public static void main(String[] args) {
        MyThread t1 = new MyThread();
        t1.start();
    }
}

