from _thread import *
import threading
import service
import socket

print_lock = threading.Lock()


def threaded(c):
    while True:
        data = c.recv(1024)
        if not data:
            print_lock.release()
            break

        service.manage_received_message(data)
        c.send(data)

    c.close()


def main():
    host = socket.gethostname()
    port = 5000
    address = (host, port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(address)
    server_socket.listen(1)

    print("Host iniciado.")

    while True:

        conn, address = server_socket.accept()

        print_lock.acquire()
        print(f"Conectado à um jogador: {address}")

        start_new_thread(threaded, (conn,))


def start_hosting():
    if __name__ == "__main__":
        main()
