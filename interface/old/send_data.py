import socket


def send_data(send_data, HOST='127.0.0.1', PORT=2222):
    received_data = b''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(send_data)
        s.settimeout(5.0)
        received_data = s.recv(1024)
    return received_data

if "__main__" == __name__:
    data = ["CMD|KIGK3122|MySuperNickname|TelegramID|",
    "create|QWE|Vasya|Petya|",
    "create|IKTK3122|Vasyaas|Petyaas|",
    "add|IKTK3122|Ghdfhkdjf|gflkbijgf|",
    "add|IKTK3122|asGhdfhkdjf|ASDgflkbijgf|",
    "show|IKTK3122|Ghdfhkdjf|gflkbijgf|",
    "show|IKTK3122|||",
    "add|KIGK3122|QWERTY|ASDFGH|",
    "remove|KIGK3122|QWERTY|ASDFGH|",
    "remove|KIGK3122|QWERT|ASDFG|",
    "add|IKTK3122|Gh",
    "add|IKTK3122",
    "add",
    "show|IKTK3122",
    "show|IKTK3122|||",
    "add|KIGK3122|QWERTY|ASDFGH|",
    "remove|KIGK3122|QWERTY|ASDFGH|"]

    for elem in data:
        byte_data = bytes(elem, encoding = 'ascii')
        print(send_data(byte_data))
