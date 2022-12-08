import socket
import service
from model import Item

address_list = []
players_dict = {}


def send_message(host, message):
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()

    print('Retorno: ' + data)

    client_socket.close()

    return data


def get_address_list():
    host = socket.gethostname()
    port = 8220

    client_socket = socket.socket()
    client_socket.connect((host, port))

    client_socket.send('get_address_list'.encode())
    data = client_socket.recv(1024).decode()
    data = data.replace('[', '')
    data = data.replace(']', '')
    data = data.replace('\'', '')

    for d in data.split(','):
        address_list.append(d)

    client_socket.close()

    print(f"Você está conectado junto à {len(address_list)} jogadores!")
    get_players_names()


def get_players_names():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    for address in address_list:
        if address != ip:
            players_dict.add(send_message(address, 'get_player_name'), address)


def manage_command(command):
    if 'troca' in command:
        service.exchange_item_with_player(command.split(':')[1], command.split(':')[2])
    if 'sugere' in command:
        item = Item(command.split(':')[3], command.split(':')[4], command.split(':')[5])
        service.suggest_item_to_dungeon_master(item, command.split(':')[2])
    if 'envia' in command:
        service.send_item_to_player(command.split(':')[1], command.split(':')[2])
    if 'atualiza' in command:
        service.update_player_hit_point(command.split(':')[1], command.split(':')[2])


def get_host_by_player_name(player_name):
    return players_dict.get(player_name)
