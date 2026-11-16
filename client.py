import socket

# Server connection information
HOST = "127.0.0.1"
PORT = 5000


def start_client():

    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

            # Set timeout to 5 seconds
            client.settimeout(5)

            print("Client starting...")
            print(f"Connecting to {HOST}:{PORT}")

            # Connect to server
            client.connect((HOST, PORT))

            print("Successfully connected to server!")

            # Message to send
            message = "Hello Server! This is the Python client."

            # Send message
            client.sendall(message.encode("utf-8"))

            print(f"Message sent: {message}")

            # Receive response
            response = client.recv(1024).decode("utf-8")

            print(f"Server response: {response}")

    except ConnectionRefusedError:

        print("ERROR: Server is not running.")

    except socket.timeout:

        print("ERROR: Connection timed out.")

    except OSError as error:

        print(f"Connection error: {error}")

    finally:

        print("Client disconnected safely.")


if __name__ == "__main__":
    start_client()