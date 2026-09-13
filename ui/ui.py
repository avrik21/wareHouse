from ..logic.warehouse import Warehouse
from ..utils import *

warehouse = Warehouse()

class Ui:
    def request_add_product():
        input_name = input("Название товара: ")
        input_category = input("Категория товара: ")
        input_cost = input_number_user("Цена товара")
        input_quantity = input_number_user("Количество товара")

        warehouse.add_product(input_name, input_category, input_cost, input_quantity)
        click_enter()

    def request_show_products():
        info = warehouse.show_products()
        if not info:
            print("Товара нет")
            click_enter()
            return
        print(info)
        click_enter()

    def request_find_priduct():
        input_name = input("Что вы ищите?(Название): ")
        result = warehouse.find_product(input_name)
        if not result:
            print("Такого товара нет!")
            click_enter()
            return
        print(result)
        click_enter()

    def request_change_countity_product():
        input_name = input("Что добавить?(Название): ")
        input_quantity = input_number_user("Сколько добавить")
        result = warehouse.change_countity_product(input_name, input_quantity)
        if not result:
            print("Такого товара нет!")
            click_enter()
            return
        print("Выполнено!!!")
        click_enter()

    def request_delete_product():
        input_name = input("Что удалить?(Название): ")
        result = warehouse.delete_product(input_name)
        if not result:
            print("Такого товара нет!")
            click_enter()
            return
        print("Выполнено!!!")
        click_enter()

    def request_total_cost_products():
        result = warehouse.total_cost_products()