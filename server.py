import socket

# Server IP address and port
HOST = "127.0.0.1"
PORT = 5000


def start_server():

    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

            # Allow the port to be reused
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Bind the server to the address and port
            server.bind((HOST, PORT))

            # Listen for incoming connections
            server.listen(1)

            print("Server is starting...")
            print(f"Server listening on {HOST}:{PORT}")

            # Wait for a client to connect
            connection, address = server.accept()

            with connection:

                print(f"Client connected from {address}")

                # Receive a message
                message = connection.recv(1024).decode("utf-8")

                if message:

                    print(f"Message received: {message}")

                    # Send a response
                    response = "Hello Client! Message received."

                    connection.sendall(response.encode("utf-8"))

                    print(f"Response sent: {response}")

                print("Client disconnected.")

    except OSError as error:

        print(f"Server error: {error}")

    finally:

        print("Server shutdown complete.")


if __name__ == "__main__":
    start_server()