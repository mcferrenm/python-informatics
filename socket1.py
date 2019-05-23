import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = raw_input('Enter - ')

# Handle error if improperly formatted or non existent URL
try:
	host = url.split('/')[2]
	mysock.connect((host, 80))
	cmd = 'GET %s HTTP/1.0\r\n\r\n' % url.encode() 
	mysock.send(cmd)
except:
	print('URL cannot be opened:', url)
	exit()

while True:
	data = mysock.recv(512)
	if len(data) < 1:
		break
	print(data.decode())

mysock.close()
