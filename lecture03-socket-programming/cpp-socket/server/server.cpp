#include "server.h"

#include <arpa/inet.h>
#include <sys/socket.h>
#include <unistd.h>

#include <cstring>
#include <iostream>

Server::Server(int port) : port_(port), serverSocket_(0) {}

void Server::Start() {
  // Create socket
  serverSocket_ = socket(AF_INET, SOCK_STREAM, 0);
  if (serverSocket_ == -1) {
    std::cerr << "Error creating socket" << std::endl;
    return;
  }

  // Bind
  sockaddr_in serverAddr;
  serverAddr.sin_family = AF_INET;
  serverAddr.sin_addr.s_addr = INADDR_ANY;
  serverAddr.sin_port = htons(port_);

  if (bind(serverSocket_, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) ==
      -1) {
    std::cerr << "Error binding" << std::endl;
    return;
  }

  // Listen
  if (listen(serverSocket_, 5) == -1) {
    std::cerr << "Error listening" << std::endl;
    return;
  }

  // Accept connections and handle data
  sockaddr_in clientAddr;
  socklen_t clientSize = sizeof(clientAddr);
  int clientSocket =
      accept(serverSocket_, (struct sockaddr*)&clientAddr, &clientSize);
  if (clientSocket == -1) {
    std::cerr << "Error accepting connection" << std::endl;
    return;
  }

  char buffer[1024];
  while (true) {
    int bytesReceived = recv(clientSocket, buffer, sizeof(buffer), 0);
    if (bytesReceived <= 0) {
      std::cout << "Client disconnected" << std::endl;
      break;
    }
    buffer[bytesReceived] = '\0';
    std::cout << "Received: " << buffer << std::endl;
    send(clientSocket, buffer, bytesReceived, 0);
  }

  close(clientSocket);
}

void Server::Stop() { close(serverSocket_); }
