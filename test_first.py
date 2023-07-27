import unittest
from main import DiningExperienceManager

class TestDiningExperienceManager(unittest.TestCase):

    def setUp(self):
        self.manager = DiningExperienceManager()

    def test_show_menu(self):
        expected_output = "Menu:\nMeal1 (Regular) - $5\nMeal2 (Regular) - $5\nMeal3 (ChefSpecial) - $10\nMeal4 (ChefSpecial) - $10\n"
        self.assertEqual(self.manager.show_menu(), expected_output)

    def test_take_order(self):
        self.manager.take_order('Meal1', '2')
        self.assertIn('Meal1', self.manager.order)
        self.assertEqual(self.manager.order['Meal1'], 2)

        with self.assertRaises(ValueError):
            self.manager.take_order('Meal5', '2')

        with self.assertRaises(ValueError):
            self.manager.take_order('Meal1', '-1')

        with self.assertRaises(ValueError):
            self.manager.take_order('Meal1', '0')

        with self.assertRaises(ValueError):
            self.manager.take_order('Meal1', '101')

    def test_calculate_cost(self):
        self.manager.take_order('Meal1', '2')
        self.manager.calculate_cost()
        self.assertEqual(self.manager.total_cost, 10)
        self.assertEqual(self.manager.discount, 0)

        self.manager.take_order('Meal3', '5')
        self.manager.calculate_cost()
        self.assertEqual(self.manager.total_cost, 60)
        self.assertEqual(self.manager.discount, 16)

    def test_confirm_order(self):
        self.manager.take_order('Meal1', '2')
        result_str, result_val = self.manager.confirm_order('y')
        self.assertEqual(result_str, "\nYour order:\nMeal1: 2\n\nTotal cost: $10\nDiscount: $0\nFinal cost: $10\nOrder confirmed. Enjoy your meal!\n")
        self.assertEqual(result_val, 10)

        # Se crea una nueva instancia de manager para reiniciar los valores
        self.manager = DiningExperienceManager()
        self.manager.take_order('Meal1', '2')
        result_str, result_val = self.manager.confirm_order('n')
        self.assertEqual(result_str, "\nYour order:\nMeal1: 2\n\nTotal cost: $10\nDiscount: $0\nFinal cost: $10\nOrder cancelled.\n")
        self.assertEqual(result_val, -1)

        # Verificar excepción con valor inválido
        with self.assertRaises(ValueError):
            self.manager.confirm_order('x')


    def test_manage(self):
        result_str, result_val = self.manager.manage('Meal1', '2', 'y')
        self.assertEqual(result_str, "Menu:\nMeal1 (Regular) - $5\nMeal2 (Regular) - $5\nMeal3 (ChefSpecial) - $10\nMeal4 (ChefSpecial) - $10\n\nYour order:\nMeal1: 2\n\nTotal cost: $10\nDiscount: $0\nFinal cost: $10\nOrder confirmed. Enjoy your meal!\n")
        self.assertEqual(result_val, 10)

    def test_done_order(self):
        result_str, result_val = self.manager.manage('done', '1', 'y')
        self.assertEqual(result_str, "Menu:\nMeal1 (Regular) - $5\nMeal2 (Regular) - $5\nMeal3 (ChefSpecial) - $10\nMeal4 (ChefSpecial) - $10\n\nYour order:\n\nTotal cost: $0\nDiscount: $0\nFinal cost: $0\nOrder confirmed. Enjoy your meal!\n")
        self.assertEqual(result_val, 0)


    def test_no_discount(self):
        self.manager.take_order('Meal1', '1')
        self.manager.calculate_cost()
        self.assertEqual(self.manager.total_cost, 5)
        self.assertEqual(self.manager.discount, 0)

    def test_cancel_order(self):
        self.manager.take_order('Meal1', '2')
        result_str, result_val = self.manager.confirm_order('n')
        self.assertEqual(result_str, "\nYour order:\nMeal1: 2\n\nTotal cost: $10\nDiscount: $0\nFinal cost: $10\nOrder cancelled.\n")
        self.assertEqual(result_val, -1)

    def test_invalid_confirmation(self):
        with self.assertRaises(ValueError):
            self.manager.manage('Meal1', '2', 'invalid')

    def test_large_order(self):
        result_str, result_val = self.manager.manage('Meal3', '11', 'y')
        self.assertEqual(self.manager.total_cost, 110)
        self.assertEqual(self.manager.discount, 47)
        self.assertEqual(result_val, 63)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.manager.manage('Meal1', 'invalid', 'y')


if __name__ == "__main__":
    unittest.main()
