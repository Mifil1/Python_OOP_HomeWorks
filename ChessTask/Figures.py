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

###########################
#       Кінець блоку      #
#    реалізації класів    #
###########################

###########################
# Блок реалізації функцій #
###########################
def checker(lst: list, pos: Tuple[int, int]):
    temp_lst = []
    for i in lst:
        if not isinstance(i, Figure):
            continue
        if i.is_possible_move(pos):
            temp_lst.append(i)
    return temp_lst


###########################
#       Кінець блоку      #
#    реалізації функцій   #
###########################

#################################
# Основний цикл роботи програми #
#################################
if __name__ == "__main__":

    li_fig = [
        Pawn((5, 4), 0),
        King((3, 3)),
        Bishop((0, 0)),
        Rook((0, 4)),
        Queen((4, 0)),
        Pawn((0, 4), 1),
        King((1, 3)),
    ]
    print(li_fig)
    li_fig = checker(li_fig, (4, 4))
    print(str(li_fig) + "\n")

    while True:
        print("Фігура")
        print("1.Пішак")
        print("2.Король")
        print("3.Кінь")
        print("4.Офіцер")
        print("5.Ладья")
        print("6.Королева")
        print("Будь - яке слово - вихід")
        try:
            your_choice = int(input("Зроби свій вибір: "))
        except ValueError:
            break
        print(f"Вы ввели: {your_choice}")
        x = int(input("Введи початкову х: "))
        y = int(input("Введи початкову у: "))
        print("Кольор")
        print("0. Чорний")
        print("1. Білий")
        color = bool(int(input("- ")))
        print("\n")
        figure = Figure()

        match your_choice:
            case 1:
                figure = Pawn((x, y), color)
            case 2:
                figure = King((x, y), color)
            case 3:
                figure = Knight((x, y), color)
            case 4:
                figure = Bishop((x, y), color)
            case 5:
                figure = Rook((x, y), color)
            case 6:
                figure = Queen((x, y), color)
            case 0:
                break
            case _:
                print("Ваш выбор не входит в диапазон")
        while True:
            print(figure.info())
            print("Куди?")
            x = int(input("Введи х: "))
            y = int(input("Введи у: "))
            if figure.is_possible_move((x, y)):
                figure.change_position((x, y))
                print("Пішли\n")
            else:
                print("Не можна!\n")

    print("\nПрограма закінчила роботу. До зустрічі!\n")
#################################
#         Кінець роботи         #
#    основного циклу програми   #
#################################
