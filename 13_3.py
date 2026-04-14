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
            
	    BufferedReader input = new BufferedReader(new InputStreamReader (socket.getInputStream()));
	    PrintWriter output = new PrintWriter(socket.getOutputStream(), true);

	    String message = input.readLine();
	    System.out.println("Client Says : "+message);
	    output.println("Hello Rishabh");
	    
	    input.close();
	    output.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

Client Code:
import java.io.*;
import java.net.*;

public class RemoteClient {
    public static void main(String[] args) {
        // REPLACE THIS IP with the IP of your Server PC
        String serverIP = "192.168.2.63";
        int port = 5000;

        try (Socket socket = new Socket(serverIP, port)) {
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
   
            // Read the welcome message from the server
            String response = in.readLine();
            System.out.println("Server says: " + response);

            BufferedReader userInput=new BufferedReader(new InputStreamReader(System.in));

            PrintWriter output=new PrintWriter(socket.getOutputStream(),true);
            BufferedReader serverInput=new BufferedReader(new InputStreamReader(socket.getInputStream()));
           
            System.out.println("Enter message to send to server : ");
            String message=userInput.readLine();
            output.println(message);

            String response2=serverInput.readLine();
            System.out.println("Server Says : "+response2);

        } catch (IOException e) {
            System.out.println("Could not connect. Check IP and Firewall!");
            e.printStackTrace();
        }
    }
}
