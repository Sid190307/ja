class PriorityThread extends Thread {
    public PriorityThread(String name) {
        super(name);
    }
    public void run() {
        System.out.println(getName() + " executing");
    }
}

public class PriorityTest {
    public static void main(String[] args) {
        PriorityThread t1 = new PriorityThread("High Priority Thread");
        PriorityThread t2 = new PriorityThread("Low Priority Thread");

        t1.setPriority(Thread.MAX_PRIORITY);
        t2.setPriority(Thread.MIN_PRIORITY);

        t1.start();
        t2.start();
    }
}

