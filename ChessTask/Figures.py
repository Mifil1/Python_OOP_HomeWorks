##############################
# Блок підключення бібліотек #
##############################
# -*- coding: utf-8 -*-
from BaseFigure import Figure
from typing import Tuple


##############################
#        Кінець блоку        #
#    підключення бібліотек   #
##############################

###########################
#  Блок реалізації класів #
###########################
class Pawn(Figure):
    _name = "Pawn"
    # if direction = 1 down->up elif direction = -1 up->down else - error
    __direction: int = 1
    __is_first_move: bool = True

    def __init__(self, position: Tuple[int, int] = (0, 0), color: bool = True):
        super().__init__(position, color)
        self.__direction = self._get_direction(color)
        self.__is_first_move = True

    def change_color(self):
        super().change_color()
        self.__direction *= -1

    @staticmethod
    def _get_direction(color: bool) -> int:
        if color:
            return 1
        else:
            return -1
    def direction(self):
        if self.__direction > 0:
            return "Up"
        else:
            return "Down"
    def change_position(self, position: Tuple[int, int]):
        super().change_position(position)
        if self.__is_first_move:
            self.__is_first_move = False

    def is_possible_move(self, position: Tuple[int, int]) -> bool:
        super().is_possible_move(position)
        return position[0] == self.get_x() + self.__direction \
            and self.get_y() == position[1] or position[0] == self.get_x() \
            + (self.__direction * 2) and self.get_y() == position[1] \
            and self.__is_first_move

    def info(self):
        return super().info() + f"\ndirection = {self.direction()}\n" \
                                f"is first move = {self.__is_first_move}"


class King(Figure):
    def is_possible_move(self, position: Tuple[int, int]) -> bool:
        super().is_possible_move(position)
        return abs(position[0] - self.get_x()) <= 1\
            and abs(position[1] - self.get_y()) <= 1


class Knight(Figure):
    def is_possible_move(self, position: Tuple[int, int]) -> bool:
        super().is_possible_move(position)
        return abs(position[0] - self.get_x()) == 2\
            and abs(position[1] - self.get_y()) == 1\
            or abs(position[0] - self.get_x()) == 1\
            and abs(position[1] - self.get_y()) == 2


class Bishop(Figure):
    def is_possible_move(self, position: Tuple[int, int]) -> bool:
        super().is_possible_move(position)
        return abs(position[0] - self.get_x())\
            == abs(position[1] - self.get_y())


class Rook(Figure):
    def is_possible_move(self, position: Tuple[int, int]) -> bool:
        super().is_possible_move(position)
        return abs(position[0] - self.get_x()) == 0\
            or abs(position[1] - self.get_y()) == 0


class Queen(Rook, Bishop):
    def is_possible_move(self, position: Tuple[int, int]) -> bool:
        return Rook.is_possible_move(self, position)\
            or Bishop.is_possible_move(self, position)


if __name__ == "__main__":

    k = Queen((4, 4), True)
    print(k.info())
    while True:
        x = int(input())
        y = int(input())
        if k.is_possible_move((x, y)):
            k.change_position((x, y))
            print("Go" + "\n")
        else:
            print("No" + "\n")
        print(k.info() + "\n")




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

#################################
# Основний цикл роботи програми #
#################################
p = Pawn()
p.is_possible_move((1, 1))
p.change_position((1, 1))
#################################
#         Кінець роботи         #
#    основного циклу програми   #
#################################
