#include "client.h"

#include <arpa/inet.h>
#include <sys/socket.h>
#include <unistd.h>

#include <cstring>
#include <iostream>

Client::Client(const char* address, int port)
    : address_(address), port_(port), clientSocket_(0) {}

void Client::Connect() {
  // Create socket
  clientSocket_ = socket(AF_INET, SOCK_STREAM, 0);
  if (clientSocket_ == -1) {
    std::cerr << "Error creating socket" << std::endl;
    return;
  }

  // Connect
  sockaddr_in serverAddr;
  serverAddr.sin_family = AF_INET;
  serverAddr.sin_port = htons(port_);
  if (inet_pton(AF_INET, address_, &serverAddr.sin_addr) <= 0) {
    std::cerr << "Invalid address" << std::endl;
    return;
  }

  if (connect(clientSocket_, (struct sockaddr*)&serverAddr,
              sizeof(serverAddr)) == -1) {
    std::cerr << "Connection failed" << std::endl;
    return;
  }
}

void Client::Send(const char* message) {
  send(clientSocket_, message, strlen(message), 0);

  char buffer[1024];
  int bytesReceived = recv(clientSocket_, buffer, sizeof(buffer), 0);
  buffer[bytesReceived] = '\0';
  std::cout << "Received: " << buffer << std::endl;
}

void Client::Disconnect() { close(clientSocket_); }
