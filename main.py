from ui.ui import Ui
from utils import *

menu = """
1. Добавить товар
2. Показать все товары
3. Найти по названию
4. Найти по категории
5. Изменить кол-во товара
6. Общая стоимость товаров
7. Удалить товар
0. Выход
"""

ui = Ui()

while True:
    clear_terminal()
    print(menu)
    choice = input_choice(7)

    if choice == 1:
        function_call(ui.request_add_product)
    elif choice == 2:
        function_call(ui.request_show_products)
    elif choice == 3:
        function_call(ui.request_find_product)
    elif choice == 4:
        function_call(ui.request_find_products_category)
    elif choice == 5:
        function_call(ui.request_change_countity_product)
    elif choice == 6:
        function_call(ui.request_total_cost_products)
    elif choice == 7:
        function_call(ui.request_delete_product)
    elif choice == 0:
        break