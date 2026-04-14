class TimerThread extends Thread {
    int time;
    public TimerThread(String name, int time) {
        super(name);
        this.time = time;
    }
    public void run() {
        try {
            while(true) {
                Thread.sleep(time * 1000);
                System.out.println(getName() + " message after " + time + " seconds");
            }
        } catch (InterruptedException e) {
            System.out.println(e);
        }
    }
}

public class SleepTest {
    public static void main(String[] args) {
        new TimerThread("Thread 1", 2).start();
        new TimerThread("Thread 2", 3).start();
    }
}
