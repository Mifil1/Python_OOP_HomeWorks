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
        return position[0] == self.get_x() + 1\
            or position[1] == self.get_y() + 1


if __name__ == "__main__":
    p = Pawn((0, 0), True)
    print(p.info() + "\n")
    print(p.is_possible_move((2, 0)))
    p.change_position((2, 0))
    print(p.info() + "\n")
    print(p.is_possible_move((2, 0)))
    p.change_color()
    print(p.info() + "\n")
    print(p.is_possible_move((1, 0)))

    k = King((0, 0), True)
    print(k.info() + "\n")
    print(k.is_possible_move((2, 1)))
    k.change_position((1, 0))
    print(k.info() + "\n")
    print(k.is_possible_move((2, 0)))
    k.change_color()
    print(k.info() + "\n")
    print(k.is_possible_move((1, 1)))



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
