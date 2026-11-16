# Python Network Security Project

## Project Description

This project demonstrates basic network communication
and port scanning using Python.

## Part 1: Socket Connection

The socket connection project includes:

- server.py
- client.py

The server listens for connections on localhost
using TCP port 5000.

The client connects to the server, sends a message,
and receives a response.

## Part 2: Port Scanner

The port scanner checks TCP ports to identify
open and closed or filtered ports.

Authorized testing targets:

- 127.0.0.1
- localhost
- scanme.nmap.org

## Running the Programs

Start the server:

python server.py

Start the client in another terminal:

python client.py

Run the port scanner:

python port_scanner.py

## Security Features

- Connection timeouts
- Error handling
- Input validation
- Limited scan ranges
- Delays between scans
- Authorized target restrictions

## Testing

Screenshots of program execution are included
in the screenshots folder.

## Ethical Considerations

This project is intended for educational purposes.

Port scanning should only be performed on systems
where authorization has been granted.
