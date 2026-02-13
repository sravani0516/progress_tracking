import json
from datetime import datetime
from functools import wraps



def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("inventory_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()} - {func.__name__} executed\n")
        return result
    return wrapper


class Product:
    def __init__(self, product_id, name, price, quantity):
        self.__product_id = product_id       # Encapsulation
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    
    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.__quantity = quantity

    def get_details(self):
        return {
            "type": "Product",
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "quantity": self.__quantity
        }



class Electronics(Product):
    def __init__(self, product_id, name, price, quantity, warranty_years):
        super().__init__(product_id, name, price, quantity)
        self.__warranty_years = warranty_years

    def get_details(self):  
        data = super().get_details()
        data["type"] = "Electronics"
        data["warranty_years"] = self.__warranty_years
        return data



class Grocery(Product):
    def __init__(self, product_id, name, price, quantity, expiry_date):
        super().__init__(product_id, name, price, quantity)
        self.__expiry_date = expiry_date

    def get_details(self):  
        data = super().get_details()
        data["type"] = "Grocery"
        data["expiry_date"] = self.__expiry_date
        return data



class InventoryIterator:
    def __init__(self, products):
        self._products = products
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._products):
            result = self._products[self._index]
            self._index += 1
            return result
        raise StopIteration



class Inventory:
    def __init__(self):
        self.__products = []

    def __iter__(self):
        return InventoryIterator(self.__products)

    @log_action
    def add_product(self, product):
        self.__products.append(product)
        print("Product added successfully.")

    @log_action
    def remove_product(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                self.__products.remove(product)
                print("Product removed successfully.")
                return
        print("Product not found.")

    @log_action
    def update_stock(self, product_id, quantity):
        for product in self.__products:
            if product.get_id() == product_id:
                product.set_quantity(quantity)
                print("Stock updated successfully.")
                return
        print("Product not found.")

    def search_product(self, keyword):
        results = []
        for product in self.__products:
            if keyword.lower() in product.get_name().lower():
                results.append(product)
        return results

    @log_action
    def save_to_file(self, filename="inventory.json"):
        data = [product.get_details() for product in self.__products]
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Inventory saved to file.")

    def load_from_file(self, filename="inventory.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            for item in data:
                if item["type"] == "Electronics":
                    product = Electronics(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["quantity"],
                        item["warranty_years"]
                    )
                elif item["type"] == "Grocery":
                    product = Grocery(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["quantity"],
                        item["expiry_date"]
                    )
                else:
                    product = Product(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["quantity"]
                    )

                self.__products.append(product)

            print("Inventory loaded successfully.")

        except FileNotFoundError:
            print("No previous inventory file found.")
        except Exception as e:
            print("Error loading file:", e)



def main():
    inventory = Inventory()
    inventory.load_from_file()

    while True:
        print("\n==== Inventory Management ====")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Show All Products")
        print("6. Save & Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                p_type = input("Enter type (Electronics/Grocery): ").strip().lower()
                pid = input("Enter Product ID: ")
                name = input("Enter Name: ")
                price = float(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))

                if p_type == "electronics":
                    warranty = int(input("Enter Warranty Years: "))
                    product = Electronics(pid, name, price, quantity, warranty)
                elif p_type == "grocery":
                    expiry = input("Enter Expiry Date: ")
                    product = Grocery(pid, name, price, quantity, expiry)
                else:
                    product = Product(pid, name, price, quantity)

                inventory.add_product(product)

            elif choice == "2":
                pid = input("Enter Product ID to remove: ")
                inventory.remove_product(pid)

            elif choice == "3":
                pid = input("Enter Product ID: ")
                quantity = int(input("Enter New Quantity: "))
                inventory.update_stock(pid, quantity)

            elif choice == "4":
                keyword = input("Enter name to search: ")
                results = inventory.search_product(keyword)
                for product in results:
                    print(product.get_details())

            elif choice == "5":
                for product in inventory:
                    print(product.get_details())

            elif choice == "6":
                inventory.save_to_file()
                print("Exiting program...")
                break

            else:
                print("Invalid choice!")

        except ValueError as ve:
            print("Input Error:", ve)
        except Exception as e:
            print("Unexpected Error:", e)


if __name__ == "__main__":
    main()
