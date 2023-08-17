#include "client.h"

int main() {
  // Create and connect client
  Client client("127.0.0.1", 12345);
  client.Connect();

  // Send and receive messages
  client.Send("Hello from client!");

  // Clean up
  client.Disconnect();

  return 0;
}
