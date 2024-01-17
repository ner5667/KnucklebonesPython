import random
import os
import math
import numpy as np

roll_dice = lambda: random.randint(1, 6)
def print_boards(player_1_board, player_2_board):
    player_1_board.test()
    print("---------\n")
    player_2_board.test()
test = lambda: print_boards(player_1_board, player_2_board)
clear = lambda: os.system("cls")

def contain_zeros(matrix):
    np_matrix = np.array(matrix)
    return np.all(np_matrix != 0)

def count_entries(arr):
    dct = dict()
    for i in arr:
        if not i in dct:
            dct.update({i:1})
        else:
            dct.update({i:dct.get(i) + 1})
    return dct

class InvalidMoveError(Exception):
    "Raised when a wrong move was tried"
    pass

class Board:
    def __init__(self):    
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.used_cols = 0
        self.name = input("Please enter your player tag: ")


    def check_for_doubles(self, position, oponent_board: "Board"):
        for tile in self.board[position]:
            if tile in oponent_board.board[position]:
                for op_index, op_tile in enumerate(oponent_board.board[position]):
                    if tile == op_tile:
                        oponent_board.board[position][op_index] = 0
                        oponent_board.used_cols -= 1

    def insert_roll(self, position, roll):
        for index, tile in enumerate(self.board[position]):
            if tile == 0:
                self.board[position][index] = roll
                self.used_cols += 1
                return
        raise InvalidMoveError

    def score(self):
        score = 0
        for row in self.board:
            for i in count_entries(row):
                j = count_entries(row)[i]
                score += i * j**2
        return score

    def test(self):
        for row in self.board:
            print(f"{row}\n")


class Game:
    def __init__(self, player_1_board: "Board", player_2_board: "Board") -> None:
        self.player_1_board = player_1_board
        self.player_2_board = player_2_board
        self.roll_arr = []


    def turn(self, curr_player: "Board", oponent_player: "Board"):
        clear()
        curr_player_roll = roll_dice()
        self.roll_arr.append(curr_player)
        print(f"Current Score: {self.player_1_board.name} {self.player_1_board.score()} - {self.player_2_board.score()} {self.player_2_board.name}")
        test()
        print("Player 1: ")
        while True:
            try:
                curr_player_inp = input(f"Your roll was {curr_player_roll}. In what column do you want to put it?\n")
                curr_player_inp = (int(curr_player_inp) - 1) % 3
                curr_player.insert_roll(curr_player_inp, curr_player_roll)
                curr_player.check_for_doubles(curr_player_inp, oponent_player)
                break
            except InvalidMoveError:
                print(f"Invalid move, the row {curr_player_inp} is already full :(")
            except ValueError:
                print("Invalid input given, please input a number from 1, 2 or 3")


def end_of_game_check(board: "Board"):
    return contain_zeros(board.board)



def evaluate(board_position, oponent_board):
    player_score = 0
    op_score = 0
    def __score(position):
        var_score = 0
        for row in position:
            row_score_list = [i * j**2 for i, j in count_entries(row).items()]
            var_score += sum(row_score_list)
        return var_score
    player_score = __score(board_position)
    op_score = __score(oponent_board)
    if contain_zeros(board_position) or contain_zeros(oponent_board):
        return -500 + (player_score > op_score) * 1000
    return player_score - op_score


def search(player_board_position, oponent_position, depth):
    def __maxi(player_board, oponent_board, depth):
        if depth == 0:
            return evaluate(player_board, oponent_board)
        for possible_move in range(1, 4):
            best_score = -math.inf
            for dice_assumption in range(1, 7):
                combined_score += __mini(__insert_roll(player_1_board, possible_move, dice_assumption))
            if combined_score > best_score:
                best_score = combined_score / 6
        return best_score

    def __mini(player_board, oponent_board, depth):

        if depth == 0:
            return evaluate(player_board, oponent_board)
        depth -= 1
        for possible_move in range(1, 4):
            best_score = math.inf
            for dice_assumption in range(1, 7):
                combined_score += __maxi(__insert_roll(player_board, oponent_board, possible_move, dice_assumption))
            if combined_score < best_score:
                best_score = combined_score / 6
            return best_score

    def __insert_roll(board, oponent_board, position, roll):
        new_board = board
        relevant_row = new_board[position]
        if 0 in relevant_row:
            for index, i in enumerate(relevant_row):
                if i == 0:
                    new_board[position][index] = roll
        if roll in oponent_board[position]:
            for index, i in enumerate(oponent_board[position]):
                if i == roll:
                    oponent_board[position][index] = 0
        return new_board, oponent_board
    



player_1_board = Board()
player_2_board = Board()

game = Game(player_1_board, player_2_board)

while not (end_of_game_check(player_1_board) or end_of_game_check(player_2_board)):
    game.turn(player_1_board, player_2_board)
    if end_of_game_check(player_1_board) or end_of_game_check(player_2_board):
        break
    game.turn(player_2_board, player_1_board)

print(f"GG\nFinal score: P1 {game.player_1_board.score()} - {game.player_2_board.score()} P2")
