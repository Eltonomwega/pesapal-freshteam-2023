import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) throws IOException {
        // Connect to the server
        Socket socket = new Socket("localhost", 8080);

        // Get the input and output streams from the socket
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

        // Read the first response from the server
        System.out.println(in.readLine());

        // Create a scanner to read input from the client
        Scanner scan = new Scanner(System.in);

        // Keep taking commands from the client and receiving responses from the server
        while (true) {
            // Read the next command from the client
            System.out.print("Enter a command: ");
            String command = scan.nextLine();

            // Send the command to the server
            out.println(command);

            // Receive the response from the server
            System.out.println("Server response: " + in.readLine());

            // Check if the command is "quit"
            if (command.equals("quit")) {
                break;
            }

        }

        // Close the socket
        socket.close();
    }
}
