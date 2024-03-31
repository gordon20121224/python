#########################匯入模組#########################
import socket

#########################函式與類別定義#########################

#########################宣告與設定#########################
HOST = "localhost"
PORT = 5438
server_socket = socket.socket()
server_socket.bind((HOST.PORT))
server_socket.listen(5)
print("server:{} port:() start".format(HORT, PORT)
client.addr = server_socket.accept()
print("client address:{}, port:{}".format(addr[0], addr[1]))
#########################主程式#########################

while True:
    msg = client.recv(128.decode("utf8")
    print("Recieve message:" msg)
    reply = ""

    if msg=="Hi":
        reply = "hello"
        client.send(reply.encode("utf8"))
    elif msg =="Bye":
        client.send(b"quit")
        break
    else:
        reply = "what?"
        client.send(reply.encode("utf8"))

client.close()
server_socket.close()