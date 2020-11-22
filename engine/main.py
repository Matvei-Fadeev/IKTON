import asyncore
import socket
import time

import cfg
from process_data import process_user_data


class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        for attempt in range(cfg.g_max_attempts):
            try:
                data = self.recv(cfg.g_count_of_received_symbols)
                response = bytes(process_user_data(data), encoding = 'ascii')
                self.send(response + b"\n\n" + b'\0')
                print("End = ", response)
            except Exception as err:
                time.sleep(cfg.g_error_sleep_sec)
            else:
                break


class EchoServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(11)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            handler = EchoHandler(sock)


def main():
    while True:
        try:
            server = EchoServer(cfg.HOST, cfg.PORT)
            asyncore.loop()
        except Exception as err:
            time.sleep(cfg.g_error_sleep_sec)


if "__main__" == __name__:
    main()
