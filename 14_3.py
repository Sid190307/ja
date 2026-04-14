class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public synchronized int getCount() {
        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Counter myCounter = new Counter();


        myCounter.increment();
        myCounter.increment();

        System.out.println("Current Count: " + myCounter.getCount());
    }
}
