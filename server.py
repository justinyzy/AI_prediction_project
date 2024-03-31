import socket
import pickle

def connect_server():
# IP & port number
    server_ip = '192.168.0.110'
    server_port = 5001

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))

    server_socket.listen()
    print(f"等待client的連線...")

    client_socket, (client_ip, client_port) = server_socket.accept()
    print(f"已收到 {client_ip}:{client_port} 的連線")

    return server_socket,client_socket

def close_connect(server_socket,client_socket):
    client_socket.close()
    server_socket.close()


def send_data(client_socket,inf_res):
    data_bytes = pickle.dumps(inf_res)
    client_socket.send(data_bytes)