# Underground Terminal-based Chat System

This repository contains two Python scripts that implement a terminal-based chat system where multiple users can communicate after logging into the same SSH server. The two main scripts are:
- `server.py`: The server-side script that manages user connections and broadcasts messages.
- `user.py`: The client-side script that allows individual users to send and receive messages.

## Table of Contents
1. [Features](#features)
2. [Specifications](#specifications)
3. [Installation](#installation)
4. [Usage](#usage)

## Features

- **Server-side script**: Manages multiple client connections and handles message broadcasting between users.
- **Client-side script**: Allows users to connect to the server and send/receive messages.
- **Multi-user support**: Multiple users can communicate in real-time through a shared SSH server.
- **Terminal-based UI**: The application is entirely text-based and runs in the terminal.

## Specifications

- **Language**: Python 3.x
- **Network Protocol**: TCP/IP
- **Server-client architecture**: The server listens for connections, and clients connect via IP and port.
- **Security**: For basic communication, this application assumes a trusted network setup like an SSH server for secure communication between clients and the server.

### Dependencies

- Python 3.x
- Socket programming library (part of the Python standard library)
- Threading (Python standard library)
- SSH server for multi-user login (recommended but optional for secure connections)

## Installation

### Step 1: Clone the repository
First, clone this repository to your local machine using git:
```
git clone https://github.com/AkbarWiraN/Online-Chatting.git
cd Online-Chatting
```
### Step 2: Install dependencies
Ensure that you have Python 3.x installed on your system.
You can check the version of Python installed by running:
```
python --version
python3 --version
```
No additional libraries need to be installed, as this system uses standard Python libraries (socket and threading).
### Step 3: Run the Server
Install Python 3.x.x:
```
sudo apt install python3
```
Install screen session:
```
sudo apt install screen
```
Create session:
```
screen -S Chatting
```
Open the session:
```
screen -r Chatting
```
Start by running the server script:
```
python3 server.py
```
The server will start and listen for client connections
### Step 4: Run the Client
Once the server is running, users can connect by running the client script. Open a new terminal window and execute:
```
python3 user.py
```
The client script will prompt you to input the server's IP address and port to establish a connection.
### Step 5: Multi-user setup (optional)
For a distributed setup, multiple users can log in via SSH to the same server where the **server.py** script is running. Each user can then run **user.py** from their SSH session to join the chat.
## Usage
1. Starting the server: Run server.py to initiate the chat server.
2. Connecting users: Each user runs user.py and connects to the server by providing the correct IP address and port.
3. Sending messages: Users can send messages from their terminal, which will be broadcast to all other connected users.
4. Exiting the chat: Press Ctrl+C or exit the program to leave the chat.

Example steps:
```
# In server terminal
python3 server.py

# In user terminals (multiple instances)
python3 user.py

```
### Expected Output
Once the server and client are running:
- The server terminal will show incoming connections and broadcast messages.
- The client terminal will display messages from other users, as well as allow the user to type and send messages.
