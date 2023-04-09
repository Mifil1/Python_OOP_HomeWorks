##############################
# Блок підключення бібліотек #
##############################
# -*- coding: utf-8 -*-

##############################
#        Кінець блоку        #
#    підключення бібліотек   #
##############################

###########################
#  Блок реалізації класів #
###########################

class MobilePhone:
    __count_numbers: int = 0
    __p_number: str = "0000000000"
    _call_counter: int = 0

    # set functions
    def set_phone_number(self, number: str) -> bool:
        if str.isdigit(number) and len(number) == 10 or len(number) == 11:
            self.__p_number = number
            return True
        return False

    # get functions
    def get_phone_number(self) -> str:
        return self.__p_number

    def get_count_calls(self) -> int:
        return self._call_counter

    # Magic functions
    def __init__(self, pnumber = ""):
        if self.set_phone_number(pnumber):
            pass
        else:
            self.__p_number = MobilePhone._create_number()
            #self.__p_number = self.__create_number()

    # static functions
    @staticmethod
    def _create_number() -> str:
        "Not work"
        MobilePhone.__count_numbers += 1
        return "0" * (11 - len(str(MobilePhone.__count_numbers))) + str(MobilePhone.__count_numbers)

    # other functions

    def call(self):
        self._call_counter += 1

    def info(self):
        return f"Phone number is {self.__p_number}\nCount calls = {self._call_counter}"


###########################
#       Кінець блоку      #
#    реалізації класів    #
###########################

###########################
# Блок реалізації функцій #
###########################
def caller(phone: MobilePhone, count=10):
    for i in range(count):
        phone.call()

def count_calls(lst:list) -> int:
    temp_sum = 0
    for i in lst:
        if isinstance(i, MobilePhone):
            temp_sum += i.get_count_calls()
    return temp_sum

###########################
#       Кінець блоку      #
#    реалізації функцій   #
###########################


#################################
# Основний цикл роботи програми #
#################################
while True:
    print("Введи номер завдання. От 1 до 3. Введи 0 чтобы выйти. ")
    your_choice = int(input())
    print(f"Вы ввели: {str(your_choice)}")
    if(your_choice):
        print(f"Завдання №{your_choice}")
    match (your_choice):
        case 1:
            print("")
            #Phone 1
            phone1 = MobilePhone()
            phone1.set_phone_number("88005553535")
            caller(phone1, 10)
            print(phone1.info())
            #Phone 2
            phone2 = MobilePhone("78732187928")
            phone2.set_phone_number("00006660000")
            caller(phone2, 2)
            print(phone2.info())
            #Phone 3
            phone3 = MobilePhone()
            # phone3.set_phone_number("1")
            caller(phone3, 18)
            print(phone3.info())

            print(f"All count calls = {count_calls([phone1, phone2, phone3])}")
        case 2:
            print("")

        case 0:
            break
        case _:
            print("Ваш выбор не входит в диапазон")
    print("\n")
    if not your_choice:
        break
print("\nПрограма закінчила роботу. До зустрічі!\n")

#################################
#         Кінець роботи         #
#    основного циклу програми   #
#################################
