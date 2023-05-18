import socket
import random

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024
    lottery = random.randint(0,101)
    print(lottery)
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    while True:
      server_socket.listen(100)
      conn, address = server_socket.accept()  # accept new connection
      print("Connection from: " + str(address))
      # receive data stream. it won't accept data packet greater than 1024 bytes
      data = conn.recv(1024).decode()
      if int(data) == lottery:
        conn.send("***Won***".encode())
        conn.close()
      else:
        conn.send("Lost".encode())


if __name__ == '__main__':
    server_program()