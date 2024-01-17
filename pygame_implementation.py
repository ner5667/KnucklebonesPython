#THIS CODE WAS ADAPTED FROM https://www.codewithfaraz.com/python/19/create-a-chess-game-in-python-step-by-step-source-code
import pygame
from pygame.locals import *
import random
import math
import numpy as np
import numpy.ma as ma


pygame.init()

WIDTH = 800
HEIGHT = 800

#visuals
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Knucklebones (Cult of the Lamb) - Python adaptation")

clock = pygame.time.Clock()
FPS = 60 #shouldn't be an issue in future, if the implementation isn't half bad :D

#game logic
roll_dice = lambda: random.randint(1, 6)
def contains_zeros(matrix):
    return np.all(np.array(matrix) != 0)

def count_entries(arr):
    dct = dict()
    for entry in arr:
        if entry in dct:
            dct.update({entry: dct.get(entry) + 1})
        else:
            dct.update({entry: 1})
    return dct

class InvalidMoveError(Exception):
    "Raised when a wrong move was tried"
    pass

class Board:
    def __init__(self) -> None:
        self.board = np.zeros(shape=(3, 3), dtype=np.uint8)
    

    def remove_doubles(self, row, roll):
        if np.all(self.board[row] == roll):




#drawing stuff to the screen

