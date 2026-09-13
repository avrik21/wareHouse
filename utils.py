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

def click_enter():
    input("Нажмите Enter ")