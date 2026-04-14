class MyRunnable implements Runnable {
    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Thread is running (Step " + i + ")");
            try {
                // This makes the thread wait for 1000 milliseconds (1 second)
                Thread.sleep(1000); 
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

public class RunnableExample {
    public static void main(String[] args) {
        MyRunnable myTask = new MyRunnable();
        Thread thread = new Thread(myTask); // Pass the task to the thread
        thread.start(); // Start the work
    }
}
