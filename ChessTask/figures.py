##############################
# Блок підключення бібліотек #
##############################
# -*- coding: utf-8 -*-
from base_figure import Figure
from typing import Tuple


##############################
#        Кінець блоку        #
#    підключення бібліотек   #
##############################

###########################
#  Блок реалізації класів #
###########################
class Pawn(Figure):
    def __init__(self, position: Tuple[int, int] = (0, 0), color_: bool = True):
        super().__init__(position, color_)
        # if direction = 1 down->up elif direction = -1 up->down else - error
        self._direction = self._get_direction(color_)
        self._first_move = True

    def change_color(self):
        super().change_color()
        self._direction *= -1

    @staticmethod
    def _get_direction(color_: bool) -> int:
        if color_:
            return 1
        else:
            return -1

    def direction(self):
        if self._direction > 0:
            return "Up"
        else:
            return "Down"

    def change_position(self, position: Tuple[int, int]):
        super().change_position(position)
        if self._first_move:
            self._first_move = False

    def can_move(self, position: Tuple[int, int]) -> bool:
        super().can_move(position)
        delta_x, delta_y = self.get_delta(position)
        if self._first_move and delta_x == self._direction * 2:
            return True
        if delta_x != self._direction:
            return False
        if delta_y:
            return False
        return True

    def info(self):
        return super().info() + f"\ndirection = {self.direction()}\n" \
                                f"is first move = {self._first_move}"


class King(Figure):
    def can_move(self, position: Tuple[int, int]) -> bool:
        super().can_move(position)
        delta_x, delta_y = self.get_delta_abs(position)
        return delta_x <= 1 and delta_y <= 1


class Knight(Figure):
    def can_move(self, position: Tuple[int, int]) -> bool:
        super().can_move(position)
        delta_x, delta_y = self.get_delta_abs(position)
        return delta_x == 2 and delta_y == 1 \
            or delta_x == 1 and delta_y == 2


class Bishop(Figure):
    def can_move(self, position: Tuple[int, int]) -> bool:
        super().can_move(position)
        delta_x, delta_y = self.get_delta_abs(position)
        return delta_x == delta_y


class Rook(Figure):
    def can_move(self, position: Tuple[int, int]) -> bool:
        super().can_move(position)
        delta_x, delta_y = self.get_delta_abs(position)
        return delta_x == 0 or delta_y == 0


class Queen(Rook, Bishop):
    def can_move(self, position: Tuple[int, int]) -> bool:
        return Rook.can_move(self, position) \
            or Bishop.can_move(self, position)


###########################
#       Кінець блоку      #
#    реалізації класів    #
###########################

###########################
# Блок реалізації функцій #
###########################
def checker(lst: list, pos: Tuple[int, int]):
    return [i for i in lst if i.can_move(pos)]


###########################
#       Кінець блоку      #
#    реалізації функцій   #
###########################

#################################
# Основний цикл роботи програми #
#################################
if __name__ == "__main__":

    li_fig = [
        Pawn((5, 4), False),
        King((3, 3)),
        Bishop((0, 0)),
        Rook((0, 4)),
        Queen((4, 0)),
        Pawn((0, 4), True),
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
            if figure.can_move((x, y)):
                figure.change_position((x, y))
                print("Пішли\n")
            else:
                print("Не можна!\n")

    print("\nПрограма закінчила роботу. До зустрічі!\n")
#################################
#         Кінець роботи         #
#    основного циклу програми   #
#################################
