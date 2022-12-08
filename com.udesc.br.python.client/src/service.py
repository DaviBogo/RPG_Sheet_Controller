from model import Player
import controller

player: Player


def exchange_item_with_player(item_name, player_name):
    item = player.get_item_by_name(item_name)
    if controller.send_message(controller.get_host_by_player_name(player_name), item) == 'sucesso':
        player.items.remove(item)
    print('Item trocado com sucesso')


def send_item_to_player(item_name, player_name):
    item = player.get_item_by_name(item_name)
    controller.send_message(
        controller.get_host_by_player_name(player_name), item)
    print('Item enviado com sucesso')


def suggest_item_to_dungeon_master(item, player_name):
    controller.send_message(
        controller.get_host_by_player_name(player_name), item)
    print('Item sugerido com sucesso')


def update_player_hit_point(hit_point, player_name):
    controller.send_message(
        controller.get_host_by_player_name(player_name), hit_point)
    print('Item sugerido com sucesso')


def manage_received_message(message):
    if message == 'get_player_name':
        return player.name
    else:
        return 'sucesso'
