from burger import Burger
import pytest
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock


items = [
        Ingredient(INGREDIENT_TYPE_SAUCE, "огонь", 100.0),
        Ingredient(INGREDIENT_TYPE_SAUCE, "вода", 200.0),
        Ingredient(INGREDIENT_TYPE_SAUCE, "земля", 300.0),]

class TestBurger:
    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = Bun('булочка', 100.0)
        burger.set_buns(bun)

        assert burger.bun is bun


    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "малина", 200.0)
        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_remove_ingredient_by_index(self, index):
        burger = Burger()
        for it in items:
            burger.add_ingredient(it)

        removed = items[index]
        burger.remove_ingredient(index)

        assert removed not in burger.ingredients
        assert len(burger.ingredients) == 2


    def test_move_ingredient(self):
        burger = Burger()
        for it in items:
            burger.add_ingredient(it)
        burger.move_ingredient(0,1)

        assert burger.ingredients[0].name == "вода"

    
    def test_get_price(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 100.0
        ingredient = Mock()
        ingredient.get_price.return_value = 200.0
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == 400.0

    def test_get_receipt(self):
        burger = Burger()
        bun = Bun('булочка', 100.0)
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "малина", 200.0)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()

        assert "булочка" in receipt
        assert "малина" in receipt
        assert "Price: 400.0" in receipt