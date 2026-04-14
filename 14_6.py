class MyRunnable implements Runnable {
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println("Thread is running");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

public class RunnableTask {
    public static void main(String[] args) {
        MyRunnable myTask = new MyRunnable();
        Thread t1 = new Thread(myTask);
        t1.start();
    }
}
