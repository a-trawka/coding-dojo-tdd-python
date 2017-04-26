discounts = [1.0, 1.0, 0.95, 0.90, 0.80, 0.75]


def add(list, element, index):
    if len(list) < index + 1:
        list.append([])
    if element not in list[index]:
        list[index].append(element)
    else:
        add(list, element, index + 1)


def price(l):
    a = []
    total_price = 0
    for book in l:
        add(a, book, 0)
    for cart in a:
        total_price += len(cart) * 8 * discounts[len(cart)]
    return total_price
