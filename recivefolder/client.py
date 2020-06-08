import socket

s = socket.socket()
host = "192.168.1.5"
port = 8080
s.connect((host,port))

print("connected..")
filename = "output.docx"
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close
print("File has been recived.")