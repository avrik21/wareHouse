import os

def clear_terminal():
    os.system("cls")

def function_call(function):
    clear_terminal()
    function()

def check_number(number):
    try:
        int(number)
        return True
    except ValueError:
        print("Необходимо число!!!")

def input_number_user(message):
    while True:
        input_number = input(f"{message}: ")
        if check_number(input_number):
            break
    return int(input_number)

def input_choice(num):
    while True:
        try:
            choice = int(input("Выберите пункт: "))
            if choice < 0 or choice > num:
                print("Выберите то что в меню")
                continue
            return choice
        except ValueError:
            print("Только циферки")

def click_enter():
    input("Нажмите Enter ")