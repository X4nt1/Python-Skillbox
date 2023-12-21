class Cell:
    value_cell = {2: 'empty', 1: 'zero', 0: 'cross'}
    free = True
    num = None
    symbol = value_cell[2]
    def __init__(self,num = None):
        self.num = num
class Board:

    state_cells = [Cell() for i in range(9)]
    def reset(self):
        self.state_cells = [Cell() for _ in range(9)]
    def change_cell(self, num, num_player):
        self.state_cells[num-1].symbol = self.state_cells[num-1].value_cell[num_player]
    def check_win(self):
        if self.state_cells[0].symbol == self.state_cells[1].symbol == self.state_cells[2].symbol != 'empty':
            return True
        elif self.state_cells[3].symbol == self.state_cells[4].symbol == self.state_cells[5].symbol != 'empty':
            return True
        elif self.state_cells[6].symbol == self.state_cells[7].symbol == self.state_cells[8].symbol != 'empty':
            return True
        elif self.state_cells[0].symbol == self.state_cells[3].symbol == self.state_cells[6].symbol != 'empty':
            return True
        elif self.state_cells[1].symbol == self.state_cells[4].symbol == self.state_cells[7].symbol != 'empty':
            return True
        elif self.state_cells[2].symbol == self.state_cells[5].symbol == self.state_cells[8].symbol != 'empty':
            return True
        elif self.state_cells[0].symbol == self.state_cells[4].symbol == self.state_cells[8].symbol != 'empty':
            return True
        elif self.state_cells[2].symbol == self.state_cells[4].symbol == self.state_cells[6].symbol != 'empty':
            return True
        else:
            return False
class Player:
    name = None
    count_win = 0
    def __init__(self, name):
        self.name = name
    def do_step(self):
        num = int(input(f'{self.name} введите номер клетки: '))
        while num < 1 and num > 9:
            num = int(input('Некорректный номер. Попробуйте еще раз! '))
        return num
class Game:
    stats_game = {0: 'play', 1: 'win', 2: 'draw'}
    stat_game = stats_game[0]
    players = []
    board = Board()
    def __init__(self, player_1, player_2):
        self.players.append(player_1)
        self.players.append(player_2)
    def do_step(self, player, num_player):
        num = player.do_step()
        while self.board.state_cells[num-1].symbol != 'empty':
            print('Клетка занята, пробуйте другую клетку!')
            num = player.do_step()
        self.board.change_cell(num,num_player)
        print(f'Сходил {self.players[num_player].name}')
        return self.board.check_win()
    def go_game(self):
        self.board.reset()
        print('Игра началсь')
        for i in range(9):
            if self.do_step(self.players[i % 2], i % 2):
                self.stat_game = self.stats_game[1]
                self.players[i % 2].count_win += 1
                print(f'{self.players[i % 2].name} победил!')
                return True
        else:
            self.stat_game = self.stats_game[2]
            print('Ничья!')
        return True
    def go_games(self):
        check_continue = True
        while check_continue:
            self.go_game()
            print(f'{self.players[0].count_win} : {self.players[1].count_win}')
            player_1 = input(f'{self.players[0].name} хотите ли вы прододжить играть?').lower() == 'да'
            player_2 = input(f'{self.players[1].name} хотите ли вы прододжить играть?').lower() == 'да'
            if not(player_1 and player_2):
                check_continue = False
        print('Игры окончены')

player_1 = Player('Егор')
player_2 = Player('Валя')
game_1 = Game(player_1, player_2)
game_1.go_games()








