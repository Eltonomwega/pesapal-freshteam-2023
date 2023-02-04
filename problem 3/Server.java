import java.io.*;
import java.net.*;
import java.util.*;

public class Server {
  private static int N =0;
  private static ArrayList<ClientHandler> clients = new ArrayList<>();

  public static void main(String[] args) throws IOException {

    Scanner scan = new Scanner(System.in);
    while(N <= 0){
      System.out.print("Set the maximum number of clients: ");
      N = scan.nextInt();
    }
    //close the scanner
    scan.close();
    try (ServerSocket server = new ServerSocket(8080)) {
        // check if server connections have reached the maximum
        while (clients.size() < N) {
          Socket socket = server.accept();
          ClientHandler client = new ClientHandler(socket);
          clients.add(client);
          new Thread(client).start();
        }
    }
  }

  static class ClientHandler implements Runnable {
    private Socket socket;
    private int rank;
    private BufferedReader in;
    private PrintWriter out;

    ClientHandler(Socket socket) {
      this.socket = socket;
      this.rank = clients.size();
    }

    public void run() {
      try {
        in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        out = new PrintWriter(socket.getOutputStream(), true);

        out.println("Welcome! Your rank is: " + rank);

        while (true) {
          String input = in.readLine();
          if (input == null || input.equals("quit")) {
            out.println("Goodbye!");
            break;
          }

          String[] parts = input.split(" ");
          int targetRank = Integer.parseInt(parts[0]);
          String command = parts[1];

          if (targetRank > rank) {
            out.println("You cannot execute this command.");
            continue;
          }
          clients.get(rank).out.println("Command executed: " + command);
        }
      } catch (IOException e) {
        System.err.println(e);
      } finally {
        try {
          socket.close();
        } catch (IOException e) {
          System.err.println(e);
        }
        // remove the client from the arraylist
        clients.remove(this);
        for (int i = rank; i < clients.size(); i++) {
          clients.get(i).rank--;
        }
      }
    }
  }
}
