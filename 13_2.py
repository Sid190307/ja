Server code:
import java.io.*;
import java.net.*;
public class RemoteServer {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(5000)) {
            System.out.println("Server started. Waiting for a client...");
            
            Socket socket = serverSocket.accept();
            System.out.println("Client connected from: " + socket.getInetAddress());

            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            out.println("Connection Successful! You are talking to PC A.");
            
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

Client code:
import java.io.*;
import java.net.*;

public class RemoteClient {
    public static void main(String[] args) {
        // REPLACE THIS IP with the IP of your Server PC
        String serverIP = "192.168.1.15"; 
        int port = 5000;

        try (Socket socket = new Socket(serverIP, port)) {
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            
            // Read the welcome message from the server
            String response = in.readLine();
            System.out.println("Server says: " + response);

        } catch (IOException e) {
            System.out.println("Could not connect. Check IP and Firewall!");
            e.printStackTrace();
        }
    }
}
