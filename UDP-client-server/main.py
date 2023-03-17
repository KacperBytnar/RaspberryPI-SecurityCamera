import socket
import json
import base64

# f = open(image,  'rb')
# img_data = f.read()
# f.close()
# enc_data = base64.b64encode(img_data)
# json.dump({'image':enc_data}, open('c:/out.json', 'w'))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('', 12000)
s.bind(server_address)  # localhost + port
s.listen()
print("a")

while True:
    clientSocket, address = s.accept()
    print(f"connection from {address} has been established")

    dataFromClient = clientSocket.recv(50000000)  #its a json

    img = json.loads(dataFromClient)

    newfile = open('C:\\Users\\kengo\\Desktop\\test2.jpg', "wb")
    base = base64.b64decode(img["image1"].encode("utf-8"))
    newfile.write(base)
    newfile.close()

    print(dataFromClient)
