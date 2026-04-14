Server.java
Code:
import java.net.*;
import java.io.*;

public class Server {
	public static void main(String args[]) {
		try {
		  ServerSocket serversocket = new ServerSocket(1234);
		  System.out.println("Server is waiting for client connection...");
		  Socket socket = serversocket.accept();
		  System.out.println("Client Connected");
		  BufferedReader input = new BufferedReader(new InputStreamReader (socket.getInputStream()));
		  PrintWriter output = new PrintWriter(socket.getOutputStream(), true);

		  String message = input.readLine();
		  System.out.println("Client Says : "+message);
		  System.out.println("Hello from server");

		  input.close();
		  output.close();
		  socket.close();
		  serversocket.close();
		}

		catch(IOException e) {
			e.printStackTrace();
		}
	}
}

Client.java
Code:
import java.net.*;
import java.io.*;

public class Client {
	public static void main(String args[]) {
		try{
		  Socket socket = new Socket("localhost", 1234);
		  System.out.println("Connected to server");

		  BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
		  PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
		  BufferedReader serverInput = new BufferedReader(new InputStreamReader(socket.getInputStream()));

		  System.out.println("Enter a message to send to server: ");
		  String message = userInput.readLine();
		  output.println(message);

		  String response = serverInput.readLine();
		  System.out.println("Server says: "+response);

		  userInput.close();
		  output.close();
		  serverInput.close();
		  socket.close();
		}

		catch (IOException e) {
			e.printStackTrace();
		}
	}
}
