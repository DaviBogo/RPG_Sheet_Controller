import controller
import server
from model import Player

def start_program():
    start = input('Gostaria de entrar no jogo? [s/n]: ')
    
    if start == 's':
        controller.get_address_list()
        server.start_hosting()
        print('Passe suas informações conforme o pedido.')
        name = input('Seu nome: ')
        response = input('Você é mestre? [s/n]: ')
        if response == 's':
            is_dungeon_master = True
        else:
            is_dungeon_master = False
        controller.service.player = Player(name, is_dungeon_master)
        while True:
            command = input('Comando ("ajuda" para lista de comandos): ')
            controller.manage_command(command)
            if command == 'sair':
                break
            

if __name__ == '__main__':
    start_program()