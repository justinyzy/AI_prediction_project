import socket

server_ip = '192.168.0.1'
server_port = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

data = client_socket.recv(1024).decode('utf-8')

print(f"The final answer：{data}")

input("按 Enter 鍵退出...")

client_socket.close()