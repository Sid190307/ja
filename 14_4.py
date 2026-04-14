class Account {
    private int balance = 1000;

    public synchronized void transfer(Account target, int amount) {
        if (this.balance >= amount) {
            this.balance -= amount;
            target.deposit(amount);
            System.out.println("Transferred " + amount + " to target account");
        } else {
            System.out.println("Insufficient funds for transfer");
        }
    }

    public synchronized void deposit(int amount) {
        this.balance += amount;
    }

    public int getBalance() {
        return balance;
    }
}

public class BankExample {
    public static void main(String[] args) {
        Account account1 = new Account();
        Account account2 = new Account();

        Thread t1 = new Thread(() -> account1.transfer(account2, 500));
        Thread t2 = new Thread(() -> account2.transfer(account1, 300));

        t1.start();
        t2.start();

        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Account1 balance: " + account1.getBalance());
        System.out.println("Account2 balance: " + account2.getBalance());
    }
}
