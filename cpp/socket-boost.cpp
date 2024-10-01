#include <iostream>
#include <asio.hpp>

using namespace boost::asio;
using ip::tcp;

int main() {
    try {
        // Initialize the Boost Asio library
        io_service io_service;

        // Create a TCP resolver to resolve the IP address and port
        tcp::resolver resolver(io_service);

        // Resolve the IP address and port
        tcp::resolver::query query("192.168.0.2", "5764");
        tcp::resolver::iterator endpoint_iterator = resolver.resolve(query);

        // Create a TCP socket
        tcp::socket socket(io_service);

        // Attempt to connect to the remote endpoint
        boost::asio::connect(socket, endpoint_iterator);

        // If we reach this point, the connection was successful
        std::cout << "Connected to 192.168.0.2 on port 5764" << std::endl;

    } catch (std::exception& e) {
        // If an exception occurs, print the error message
        std::cerr << "Exception: " << e.what() << std::endl;
    }

    return 0;
}