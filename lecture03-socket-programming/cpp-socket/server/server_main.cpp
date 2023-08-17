#include "server.h"

int main() {
    // Create and start server
    Server server(12345);
    server.Start();
    server.Stop();

    return 0;
}
