import sys


# Menú con opciones de comida y precios
menu = {
    "1": {"meal": "Spaghetti", "category": "Italian", "price": 8},
    "2": {"meal": "Sushi", "category": "Japanese", "price": 10},
    "3": {"meal": "Tacos", "category": "Mexican", "price": 6},
    # Agrega más opciones de comida al menú según tus preferencias
}

# Opciones de descuento
discounts = {
    5: 0.1,   # Descuento del 10% para más de 5 comidas
    10: 0.2   # Descuento del 20% para más de 10 comidas
}

# Opciones de descuento especial
special_discounts = {
    50: 10,   # Descuento de $10 para un total de más de $50
    100: 25   # Descuento de $25 para un total de más de $100
}

# Opciones de categoría especial
special_category = ["Chef's Specials"]

# Límite máximo de cantidad de comidas por pedido
max_order_quantity = 100


def display_menu():
    print("Menu:")
    for key, value in menu.items():
        print(f"{key}. {value['meal']} ({value['category']}): ${value['price']}")


def get_user_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nOrder canceled.")
        sys.exit()


def validate_quantity(quantity):
    try:
        quantity = int(quantity)
        if quantity > 0:
            return quantity
        else:
            return None
    except ValueError:
        return None


def calculate_cost(order):
    total_cost = 0
    for meal, quantity in order.items():
        price = menu[meal]['price']
        total_cost += price * quantity

    # Aplicar descuento según la cantidad de comidas
    if len(order) > max(discounts.keys()):
        total_cost *= (1 - max(discounts.values()))

    # Aplicar descuento especial según el total del pedido
    for amount, discount in special_discounts.items():
        if total_cost > amount:
            total_cost -= discount

    # Aplicar recargo por categoría especial
    for meal, quantity in order.items():
        if menu[meal]['category'] in special_category:
            total_cost += menu[meal]['price'] * quantity * 0.05

    return total_cost


def validate_order(order):
    # Verificar si las comidas seleccionadas están en el menú
    for meal in order.keys():
        if meal not in menu:
            print(f"Error: '{meal}' is not a valid meal selection.")
            return False

    # Verificar si la cantidad de comidas es válida
    for quantity in order.values():
        if quantity is None:
            print("Error: Invalid quantity entered.")
            return False

    # Verificar si la cantidad de comidas supera el límite máximo
    total_quantity = sum(order.values())
    if total_quantity > max_order_quantity:
        print(f"Error: Maximum order quantity exceeded. Maximum: {max_order_quantity}")
        return False

    return True


def confirm_order(order, total_cost):
    print("\nSelected Meals:")
    for meal, quantity in order.items():
        print(f"{menu[meal]['meal']} ({menu[meal]['category']}): {quantity} x ${menu[meal]['price']}")

    print(f"\nTotal Cost: ${total_cost}")

    user_input = get_user_input("\nConfirm order? (Y/N): ").lower()

    if user_input == 'y':
        return total_cost
    else:
        print("Order canceled.")
        return -1


def dining_experience_manager():
    display_menu()

    order = {}
    while True:
        meal = get_user_input("\nEnter meal number to order (or 'done' to finish): ")

        if meal == 'done':
            break

        quantity = get_user_input("Enter quantity for the meal: ")
        quantity = validate_quantity(quantity)

        if quantity is None:
            print("Error: Invalid quantity entered. Please enter a positive integer.")
            continue

        order[meal] = quantity

    if not validate_order(order):
        return -1

    total_cost = calculate_cost(order)
    return confirm_order(order, total_cost)


if __name__ == '__main__':
    result = dining_experience_manager()
    if result != -1:
        print(f"\nThank you for your order! Total cost: ${result}")