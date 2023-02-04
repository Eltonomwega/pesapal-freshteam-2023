## Problem 3

Build a TCP server that can accept and hold a maximum of N clients (where N is configurable).
These clients are assigned ranks based on first-come-first-serve, i.e whoever connects first receives the next available high rank. Ranks are from 0–N, 0 being the highest rank.

Clients can send to the server commands that the server distributes among the clients. Only a client with a lower rank can execute a command of a higher rank client. Higher rank clients cannot execute commands by lower rank clients, so these commands are rejected. The command execution can be as simple as the client printing to console that command has been executed.

If a client disconnects the server should re-adjust the ranks and promote any client that needs to be promoted not to leave any gaps in the ranks.

---
## Multi-threaded TCP server (Java)

This is a multithreaded tcp server written in Java that can serve a configurable number of clients.

## Requirements
This project requires Java to be installed on your system.

## Server
The server is implemented in the `Server.java` file. It listens on port 8080 and creates a new thread for each incoming connection.

## Client
The client is implemented in the `Client.java` file. It connects to the server and sends a message to it.

## Running the project
- Compile the server and client `javac *.java`
- Start the server `java Server` and set the number of clients that can connect
- Start up a client `java Client`

To send a command to the server `<targetRank> <command>` eg. `0 print`

To quit the connection type `quit`

---
## References
- [ChatGPT](https://chat.openai.com/chat) for the generation of code skeleton i.e the server class skeleton
