import socket

s = socket.socket()
#host = socket.gethostname()
host = '172.16.0.1'
port = 6543
s.bind((host,port))
s.listen(1)
print(host)
print('Esperanco conexões')
conn, addr = s.accept()
print(addr,'Foi conectado')

filename= input(str('Entre como o nome do arquivo: '))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print('Enviado com sucesso')
