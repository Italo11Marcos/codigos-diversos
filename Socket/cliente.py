import socket
s = socket.socket()
host = '172.16.0.1'
port = 6543
s.connect((host,port))
print('Conectado')

filename = input(str('Nome do arquivo: '))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print('sucesso')


import subprocess
subprocess.Popen(['start','teste.mp3'],shell=True)
