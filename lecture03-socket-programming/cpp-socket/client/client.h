#pragma once

class Client {
 public:
  Client(const char* address, int port);
  void Connect();
  void Send(const char* message);
  void Disconnect();

 private:
  const char* address_;
  int port_;
  int clientSocket_;
};
