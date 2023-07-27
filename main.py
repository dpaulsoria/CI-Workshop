class DiningExperienceManager:

    def __init__(self):
        self.menu = {
            'Meal1': {'price': 5, 'type': 'Regular'},
            'Meal2': {'price': 5, 'type': 'Regular'},
            'Meal3': {'price': 10, 'type': 'ChefSpecial'},
            'Meal4': {'price': 10, 'type': 'ChefSpecial'},
        }
        self.order = {}
        self.total_cost = 0
        self.discount = 0

    def show_menu(self):
        menu_str = "Menu:\n"
        for meal, details in self.menu.items():
            menu_str += f"{meal} ({details['type']}) - ${details['price']}\n"
        return menu_str


    def take_order(self, meal_name, quantity):
        if meal_name.lower() == 'done':
            return

        if meal_name not in self.menu:
            raise ValueError("Invalid meal selection. Please try again.")

        if not (quantity.isdigit() and int(quantity) > 0 and int(quantity) <= 100):
            raise ValueError("Invalid quantity. Please try again.")

        self.order[meal_name] = self.order.get(meal_name, 0) + int(quantity)


    def calculate_cost(self):
        self.total_cost = 0
        for meal, quantity in self.order.items():
            self.total_cost += self.menu[meal]['price'] * quantity

        if self.total_cost > 100:
            self.discount = 25
        elif self.total_cost > 50:
            self.discount = 10
        else:
            self.discount = 0

        meal_count = sum(self.order.values())
        if meal_count > 10:
            self.discount += self.total_cost * 0.2
        elif meal_count > 5:
            self.discount += self.total_cost * 0.1


    def confirm_order(self, confirmation):
        order_str = "\nYour order:\n"
        for meal, quantity in self.order.items():
            order_str += f"{meal}: {quantity}\n"

        self.calculate_cost()

        order_str += (f"\nTotal cost: ${self.total_cost}\n"
                    f"Discount: ${self.discount}\n"
                    f"Final cost: ${self.total_cost - self.discount}\n")

        if confirmation.lower() == 'y':
            order_str += "Order confirmed. Enjoy your meal!\n"
            return order_str, self.total_cost - self.discount
        elif confirmation.lower() == 'n':
            order_str += "Order cancelled.\n"
            return order_str, -1
        else:
            raise ValueError("Invalid option. Please try again.")


    def manage(self, meal_name, quantity, confirmation):
        menu = self.show_menu()
        self.take_order(meal_name, quantity)
        order_str, result = self.confirm_order(confirmation)
        return menu + order_str, result


def main(): # pragma: no cover
    manager = DiningExperienceManager()
    result = manager.manage()
    print(f"Result: {result}")

if __name__ == "__main__":  # pragma: no cover
    main()
