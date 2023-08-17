#pragma once

class Server {
 public:
  Server(int port);
  void Start();
  void Stop();

 private:
  int port_;
  int serverSocket_;
};
