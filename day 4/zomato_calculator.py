def show_menu():
    print("\n🍽️ ZOMATO MENU")
    print("1. Pizza  - ₹150")
    print("2. Burger - ₹100")
    print("3. Pasta  - ₹120")
    print("4. Exit")


def get_price(choice):
    menu = {
        1: ("Pizza", 150),
        2: ("Burger", 100),
        3: ("Pasta", 120)
    }

    if choice in menu:
        return menu[choice]
    else:
        raise ValueError("Invalid menu choice")


def calculate_gst(amount):
    return amount * 0.05


def calculate_discount(amount):
    if amount > 500:
        return amount * 0.10
    return 0


try:
    print("🍕 Welcome to Zomato Order Calculator 🍔")
    orders = []
    total_amount = 0

    while True:
        show_menu()
        choice = int(input("Enter item number: "))

        if choice == 4:
            break

        item_name, price = get_price(choice)

        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            raise ZeroDivisionError("Quantity must be greater than zero")

        cost = price * quantity
        orders.append((item_name, quantity, cost))
        total_amount += cost

        print(f"✅ Added {quantity} x {item_name} to cart")

except ValueError:
    print("❌ Invalid input! Please enter correct numbers.")

except ZeroDivisionError:
    print("❌ Quantity cannot be zero or negative.")

except Exception as e:
    print("❌ Unexpected error:", e)

else:
    print("\n🧾 ORDER SUMMARY")
    print("----------------")
    for item, qty, cost in orders:
        print(f"{item} x {qty} = ₹{cost}")

    gst = calculate_gst(total_amount)
    discount = calculate_discount(total_amount)
    final_amount = total_amount + gst - discount

    print("\n💰 BILL DETAILS")
    print(f"Subtotal : ₹{total_amount}")
    print(f"GST (5%) : ₹{gst:.2f}")
    print(f"Discount : ₹{discount:.2f}")
    print(f"Total Payable : ₹{final_amount:.2f}")

finally:
    print("\n🙏 Thank you for ordering with Zomato!")
