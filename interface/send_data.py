import socket


def send_data(send_data, HOST='127.0.0.1', PORT=2222):
    received_data = b''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(send_data)
        received_data = s.recv(1024)
    return received_data

if "__main__" == __name__:
    print(send_data(b"create|qwe|qwe|123|qwe"))
    print(send_data(b"afsas"))
    print(send_data(b"12312"))
