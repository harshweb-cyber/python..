#server
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1',8888))

print("Listening...")

s.listen(1)
#accept method to accept request from client
client,addr = s.accept()
print("conected")

client.send("Hello".encode())

while True:
  cmd = input("$ ")
  client.send(cmd.encode())
  output = (client.recv(1024)).decode()
  print(output)
  
#s.setsockopt(level, option, value):
# This is a method used to set options for a socket.
# level: Specifies the protocol level at which the option is applied.
#     socket.SOL_SOCKET indicates that the option is applied at the socket level.
# option: The specific option being set.
#     socket.SO_REUSEADDR allows a socket to bind to a port that is already in the TIME_WAIT state.
# value: The value to set for the option.
#     1 (or True) enables the option.
