import socket
import pickle

server_ip = '192.168.0.110'
server_port = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

while True:
    data_bytes = client_socket.recv(4096)
    if not data_bytes:
        break
    data_list = pickle.loads(data_bytes)
    
    if "STOP" in data_list:
        break
    
    print("The final answer:")
    for item in data_list:
        print(item)

client_socket.close()


