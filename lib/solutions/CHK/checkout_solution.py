# noinspection PyUnusedLocal
# skus = unicode string


def get_pricing_table():
    return {
        "A": {
            "one": 50,
            "three": 130,
            "five": 200
        },
        "B": {
            "one": 30,
            "two": 45
        },
        "C": {
            "one": 20
        },
        "D": {
            "one": 15
        },
        "E": {
            "one": 40
        },
        "F": {
            "one": 10
        },
        "G": {
            "one": 20
        },
        "H": {
            "one": 10,
            "five": 45,
            "ten": 80,
        },
        "I": {
            "one": 35,
        },
        "J": {
            "one": 60,
        },
        "K": {
            "one": 80,
            "two": 150
        },
        "L": {
            "one": 90,
        },
        "M": {
            "one": 15,
        },
        "N": {
            "one": 40,
        },
        "O": {
            "one": 10,
        },
        "P": {
            "one": 50,
            "five": 200,
        },
        "Q": {
            "one": 30,
            "three": 80,
        },
        "R": {
            "one": 50,
        },
        "S": {
            "one": 20,
            "special": 45
        },
        "T": {
            "one": 20,
            "special": 45
        },
        "U": {
            "one": 40,
        },
        "V": {
            "one": 50,
            "two": 90,
            "three": 130,

        },
        "W": {
            "one": 20,
        },
        "X": {
            "one": 17,
            "special": 45
        },
        "Y": {
            "one": 20,
            "special": 45
        },
        "Z": {
            "one": 21,
            "special": 45
        },
    }


def single_discount(value, item, pricing_table, discount_1, discount_1_s):
    amount = 0
    amount += (value // discount_1) * pricing_table[item][discount_1_s]
    amount += (value % discount_1) * pricing_table[item]["one"]
    if amount < 0:
        return 0
    return amount


def double_discount(value, item, pricing_table, discount_2, discount_2_s, discount_1, discount_1_s):
    amount = 0
    amount += value // discount_1 * pricing_table[item][discount_1_s]
    leftover_1 = value % discount_1
    amount += (leftover_1 // discount_2) * pricing_table[item][discount_2_s]
    leftover_2 = leftover_1 % discount_2
    amount += leftover_2 * pricing_table[item]["one"]
    if amount < 0:
        return 0
    return amount


def internal_removal(value, amount):
    items_to_pay = 0
    while True:
        if value < amount:
            items_to_pay += value
            break
        if value == 0:
            break
        items_to_pay += amount
        value -= amount
        if value != 0:
            value -= 1
    if items_to_pay < 0:
        return 0
    return items_to_pay


def checkout(skus):
    pricing_table = get_pricing_table()

    skus_copy = skus
    for key, _ in pricing_table.items():
        skus_copy = skus_copy.replace(key, '')

    if skus_copy != "":
        # If there are still elements in the SKUS, there are invalid items
        return -1

    current_basket = {
        "N": skus.count("N"),
        "R": skus.count("R"),
        "A": skus.count("A"),
        "E": skus.count("E"),
        "B": skus.count("B"),
        "C": skus.count("C"),
        "D": skus.count("D"),
        "F": skus.count("F"),
        "G": skus.count("G"),
        "H": skus.count("H"),
        "I": skus.count("I"),
        "J": skus.count("J"),
        "K": skus.count("K"),
        "L": skus.count("L"),
        "M": skus.count("M"),
        "O": skus.count("O"),
        "P": skus.count("P"),
        "Q": skus.count("Q"),
        "S": skus.count("S"),
        "T": skus.count("T"),
        "U": skus.count("U"),
        "V": skus.count("V"),
        "W": skus.count("W"),
        "X": skus.count("X"),
        "Y": skus.count("Y"),
        "Z": skus.count("Z"),
    }

    basket_value = 0

    for item, value in current_basket.items():
        match item:
            case "A":
                basket_value += double_discount(value, item, pricing_table, 3, "three",  5, "five")
            case "B":
                if value < 0:
                    value = 0
                basket_value += single_discount(value, item, pricing_table, 2, "two")
            case "E":
                # Remove extra deals and calculate as regular
                discounted_amount = value // 2
                current_basket["B"] = current_basket["B"] - discounted_amount
                basket_value += value * pricing_table[item]["one"]
            case "F":
                # Remove extra deals and calculate as regular
                if value > 2:
                    items_to_pay = internal_removal(value, 2)
                    basket_value += items_to_pay * pricing_table[item]["one"]
                else:
                    basket_value += value * pricing_table[item]["one"]
            case "H":
                basket_value += double_discount(value, item, pricing_table, 5, "five", 10, "ten")
            case "K":
                basket_value += single_discount(value, item, pricing_table, 2, "two")
            case "P":
                basket_value += single_discount(value, item, pricing_table, 5, "five")
            case "Q":
                basket_value += single_discount(value, item, pricing_table, 3, "three")
            case "V":
                basket_value += double_discount(value, item, pricing_table, 2, "two", 3, "three")
            case "U":
                # Remove extra deals and calculate as regular
                if value > 3:
                    items_to_pay = internal_removal(value, 3)
                    basket_value += items_to_pay * pricing_table[item]["one"]
                else:
                    basket_value += value * pricing_table[item]["one"]
            case "N":
                # Remove extra deals and calculate as regular
                discounted_amount = value // 3
                current_basket["M"] = current_basket["M"] - discounted_amount
                basket_value += value * pricing_table[item]["one"]
            case "R":
                # Remove extra deals and calculate as regular
                discounted_amount = value // 3
                current_basket["Q"] = current_basket["Q"] - discounted_amount
                basket_value += value * pricing_table[item]["one"]
            case "S":
                basket_value += single_discount(value, item, pricing_table, 3, "special")
                # current_basket["S"] = value % 3
            case "T":
                basket_value += single_discount(value, item, pricing_table, 3, "special")
                # current_basket["T"] = value % 3
            case "X":
                basket_value += single_discount(value, item, pricing_table, 3, "special")
                # current_basket["X"] = value % 3
            case "Y":
                basket_value += single_discount(value, item, pricing_table, 3, "special")
                # current_basket["Y"] = value % 3
            case "Z":
                basket_value += single_discount(value, item, pricing_table, 3, "special")
                # current_basket["Z"] = value % 3
            case _:
                if value < 0:
                    value = 0
                basket_value += value * pricing_table[item]["one"]

    return basket_value



