#########################匯入模組#########################
import socket

#########################函式與類別定義#########################

#########################宣告與設定#########################
client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 5438))
#########################主程式#########################
while True:
    msg = input("Input Message:")
    client_socket.send(msg.encode("utf8"))
    reply = client_socket.recv(128).decode("utf8")
    if reply == "quit":
        print("disconnected")
        client_socket.close()
        break
    print(reply)
