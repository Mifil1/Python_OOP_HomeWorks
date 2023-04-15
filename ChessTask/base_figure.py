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
def on_the_board(position: Tuple[int, int]) -> bool:
    # position[0] = x, position[1] = y
    return 0 <= position[0] < 8 and 0 <= position[1] < 8


class Figure:
    # Construct
    def __init__(self, position: Tuple[int, int] = (0, 0), color: bool = True):
        self._color = color
        if on_the_board(position):
            self._x, self._y = position
        elif self._color:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = 7, 7

    # methods get
    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def get_color(self) -> bool:
        return self._color

    @property
    def color_tx(self) -> str:
        if self._color:
            return "White"
        else:
            return "Black"

    def get_delta(self, position: Tuple[int, int]):
        return position[0] - self.x, position[1] - self.y
    def get_delta_abs(self, position: Tuple[int, int]):
        return abs(self.get_delta(position)[0]), abs(self.get_delta(position)[1])

    # other methods
    def change_color(self):
        self._color = not self._color

    def change_position(self, position: Tuple[int, int]):
        if self.can_move(position):
            self._x, self._y = position
            return True
        return False

    def can_move(self, position: Tuple[int, int]) -> bool:
        if not on_the_board(position):
            return False

    def info(self):
        return f"It`s {self.__class__.__name__} \nx = {self._x} \ny = {self._y}\n" \
               f"color = {self.color_tx}"

    # magic methods (dander)
    def __str__(self):
        return f"{self.__class__.__name__} x = {self._x} y = {self._y} " \
               f"{self.color_tx}"

    def __repr__(self):
        return f"{self.__class__.__name__} x = {self._x} y = {self._y} " \
               f"{self.color_tx}"


###########################
#       Кінець блоку      #
#    реалізації класів    #
###########################

###########################
# Блок реалізації функцій #
###########################
def print_hello() -> None:
    print("Hello")

###########################
#       Кінець блоку      #
#    реалізації функцій   #
###########################
