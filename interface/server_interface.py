import socket

def send_data_to_server(data, HOST='127.0.0.1', PORT=2222):
    byte_data = bytes(data, encoding = 'UTF-8')
    received_data = b''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(byte_data)
        s.settimeout(2.0)
        received_data = s.recv(1024)
    received_data = received_data.decode()
    return received_data
