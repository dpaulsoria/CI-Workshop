import pytest
from main import DiningExperienceManager

def test_init():
    manager = DiningExperienceManager()
    assert manager.total_cost == 0
    assert manager.discount == 0
    assert manager.order == {}

def test_show_menu():
    manager = DiningExperienceManager()
    expected_output = ("Menu:\n"
                       "Meal1 (Regular) - $5\n"
                       "Meal2 (Regular) - $5\n"
                       "Meal3 (ChefSpecial) - $10\n"
                       "Meal4 (ChefSpecial) - $10\n")
    assert manager.show_menu() == expected_output


def test_take_order():
    manager = DiningExperienceManager()
    manager.take_order('Meal1', '5')
    assert manager.order == {'Meal1': 5}

    with pytest.raises(ValueError):
        manager.take_order('InvalidMeal', '5')

    with pytest.raises(ValueError):
        manager.take_order('Meal1', 'InvalidQuantity')

def test_calculate_cost():
    manager = DiningExperienceManager()
    manager.order = {'Meal1': 5, 'Meal2': 5}
    manager.calculate_cost()
    assert manager.total_cost == 50
    assert manager.discount == 5  # 10% off for ordering more than 5 meals

def test_calculate_cost_with_discount():
    manager = DiningExperienceManager()
    manager.order = {'Meal1': 11}
    manager.calculate_cost()
    assert manager.total_cost == 55
    assert manager.discount == 21  # 20% off for ordering more than 10 meals + $10 for total cost over $50


def test_confirm_order():
    manager = DiningExperienceManager()
    manager.order = {'Meal1': 5}
    order_str, result = manager.confirm_order('y')
    assert result == 25.0
    assert "Order confirmed. Enjoy your meal!" in order_str

def test_manage():
    manager = DiningExperienceManager()
    menu_order_str, result = manager.manage('Meal1', '5', 'y')
    assert result == 25.0
    assert "Menu:" in menu_order_str
    assert "Your order:" in menu_order_str
    assert "Order confirmed. Enjoy your meal!" in menu_order_str
