import socket

# Prompt the user for server IP address and port number
server_ip = input("Enter the server IP address: ")
server_port = int(input("Enter the server port number: "))

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = (server_ip, server_port)
client_socket.connect(server_address)

<<<<<<< HEAD
while True:
    # Prompt the user for input
    user_input = input("Enter a string (or press 'Q' to quit): ")

    # Break the loop if 'Q' or 'q' is entered
    if user_input.lower() == 'q':
        break

    # Send the user input to the server
    client_socket.sendall(user_input.encode('utf-8'))

    # Receive the reply from the server
    reply = client_socket.recv(1024).decode('utf-8')

    # Print the reply
    print("Reply from server:", reply)
=======
# Prompt the user for input
user_input = input("Enter a string: ")

# Send the user input to the server
client_socket.sendall(user_input.encode('utf-8'))

# Receive the reply from the server
reply = client_socket.recv(1024).decode('utf-8')

# Print the reply
print("Reply from server:", reply)
>>>>>>> 05d200d7f64d6acc1d185ad5054aaf3d6ebd479a

# Close the connection
client_socket.close()
