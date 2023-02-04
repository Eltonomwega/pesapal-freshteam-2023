import java.io.*;
import java.net.*;
import java.util.*;

public class TCPServer {
  private static final int N = 5;
  private static ArrayList<ClientHandler> clients = new ArrayList<>();

  public static void main(String[] args) throws IOException {
    try (ServerSocket server = new ServerSocket(8080)) {
        while (true) {
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

        clients.remove(this);
        for (int i = rank; i < clients.size(); i++) {
          clients.get(i).rank--;
        }
      }
    }
  }
}
