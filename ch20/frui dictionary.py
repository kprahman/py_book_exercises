def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = inventory.get(fruit,0) + quantity
    return


from unit_test import test
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
test("strawberries" in new_inventory)
test(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
test(new_inventory["strawberries"] == 35)