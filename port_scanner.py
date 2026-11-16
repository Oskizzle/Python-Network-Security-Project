import socket
import time
from datetime import datetime

# Authorized targets only
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "scanme.nmap.org"]


def scan_port(host, port):
    """Check whether a TCP port is open."""

    try:
        # Create TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:

            # Set connection timeout
            scanner.settimeout(1)

            # Attempt connection
            result = scanner.connect_ex((host, port))

            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: CLOSED or FILTERED")

    except socket.timeout:
        print(f"Port {port}: Connection timed out")

    except OSError as error:
        print(f"Port {port}: Error - {error}")


def start_scanner():

    print("=" * 40)
    print("PYTHON NETWORK PORT SCANNER")
    print("=" * 40)

    # Display current date and time
    print(f"Start Time: {datetime.now()}")

    # Get target host
    host = input("Enter target host: ").strip().lower()

    # Validate host
    if host not in ALLOWED_HOSTS:
        print("ERROR: Unauthorized target.")
        return

    try:
        # Get port range
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        # Validate port numbers
        if not (1 <= start_port <= 65535):
            print("ERROR: Invalid starting port.")
            return

        if not (1 <= end_port <= 65535):
            print("ERROR: Invalid ending port.")
            return

        if start_port > end_port:
            print("ERROR: Starting port must be less than ending port.")
            return

        # Limit the number of ports scanned
        if end_port - start_port + 1 > 100:
            print("ERROR: Maximum scan range is 100 ports.")
            return

        print(f"\nScanning host: {host}")
        print(f"Port range: {start_port} - {end_port}")

        start_time = time.time()

        # Scan each port
        for port in range(start_port, end_port + 1):

            scan_port(host, port)

            # Delay between connection attempts
            time.sleep(0.1)

        # Calculate scan duration
        duration = time.time() - start_time

        print("\nScan completed.")
        print(f"Total scan time: {duration:.2f} seconds")
        print(f"End Time: {datetime.now()}")

    except ValueError:
        print("ERROR: Port numbers must be integers.")

    except KeyboardInterrupt:
        print("\nScan stopped by user.")


if __name__ == "__main__":
    start_scanner()