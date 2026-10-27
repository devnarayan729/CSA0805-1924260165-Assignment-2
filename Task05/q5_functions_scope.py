def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order


def calculate_bill(price, quantity=1, tax_rate=0.05):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return subtotal, tax


global_total = 0


def add_to_global(amount):
    global global_total
    global_total += amount


def make_counter():
    count = 0

    def increase():
        nonlocal count
        count += 1
        return count

    return increase


print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print("Buggy defaults:", add_item_buggy.__defaults__)
print(add_item("Tea"), add_item("Vada"))

customers = []
for items in (["Tea", "Vada"], ["Coffee"], ["Idli", "Tea", "Water"]):
    order = []
    for item in items:
        add_item(item, order)
    customers.append(order)
print("Customer orders:", customers)

print("Bill:", calculate_bill(20, 2))
print("Keyword bill:", calculate_bill(price=20, quantity=2, tax_rate=0.05))
add_to_global(50)
print("Global total:", global_total)
counter = make_counter()
print("Nonlocal counter:", counter(), counter())
