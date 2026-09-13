from product import Product

class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, name, category, cost, quantity):
        product = Product(name, category, cost, quantity)

        self.products.append(product)

    def show_products(self):
        if not len(self.products):
            return False

        info = ""
        
        for item in self.products:
            info_item = f"""
Название: {item.name} | Категория: {item.category} | Цена: {item.cost} | {item.quantity}шт. """
            info += info_item
        return info

    def find_product(self, name):
        for item in self.products:
            if item.name == name:
                info_item = """
Название: {item.name} | Категория: {item.category} | Цена: {item.cost} | {item.quantity}шт. """
                return info_item
        return False

    def change_countity_product(self, name, number):
        for item in self.products:
            if item.name == name:
                item.quantity = number
                return True
        return False

    def delete_product(self, name):
        for item in self.products:
            if item.name == name:
                self.products.remove(item)
                return True
        return False

    def total_cost_products(self):
        result = 0
        for item in self.products:
            result += (item.cost * item.quantity)
            return result

    def find_products_category(self, category):
        lst = []

        for item in self.products:
            if item.category == category:
                lst.append(item)
        return lst

    