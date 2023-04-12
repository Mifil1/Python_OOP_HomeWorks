##############################
# Блок підключення бібліотек #
##############################
# -*- coding: utf-8 -*-
from typing import Tuple


##############################
#        Кінець блоку        #
#    підключення бібліотек   #
##############################

###########################
#  Блок реалізації класів #
###########################
class Figure:
    __x: int = 0
    __y: int = 0
    # if color = True - white else black
    _color: bool = True

    def __init__(self, position: Tuple[int, int] = (0, 0), color: bool = True):
        self.__color = color
        if self.on_the_board(position):
            self.__x, self.__y = position
        elif self.__color:
            self.__x, self.__y = 0, 0
        else:
            self.__x, self.__y = 7, 7

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def get_color(self) -> bool:
        return self.__color

    def color(self) -> bool:
        if self.__color:
            return "White"
        else:
            return "Black"

    def change_color(self):
        self.__color = not self.__color

    @staticmethod
    def on_the_board(position: Tuple[int, int]) -> bool:
        # position[0] = x, position[1] = y
        return 0 <= position[0] < 8 and 0 <= position[1] < 8

    def change_position(self, position: Tuple[int, int]):
        if self.is_possible_move(position):
            self.__x, self.__y = position
            return True
        return False

    def is_possible_move(self, position: Tuple[int, int]) -> bool:
        if not self.on_the_board(position):
            return False

    def info(self):
        return f"It`s {self.__class__} \nx = {self.__x} \ny = {self.__y} \n" \
               f"color = {self.color()}"


###########################
#       Кінець блоку      #
#    реалізації класів    #
###########################

###########################
# Блок реалізації функцій #
###########################
def print_hello():
    print("Hello")

###########################
#       Кінець блоку      #
#    реалізації функцій   #
###########################
