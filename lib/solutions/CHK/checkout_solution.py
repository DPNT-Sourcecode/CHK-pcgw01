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
            "one": 70,
            "two": 120
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
            "one": 20
        },
        "T": {
            "one": 20
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
            "one": 17
        },
        "Y": {
            "one": 20
        },
        "Z": {
            "one": 21
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

def collect_current_basket(skus):
    return {
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


def get_leftover_basket(current_basket):
    temp_skus = ""
    for letter in ["Z", "S", "T", "Y", "X"]:
        # Order them by price in order to be filtered correctly
        temp_skus += letter * current_basket[letter]
    return temp_skus


def checkout(skus):
    pricing_table = get_pricing_table()

    skus_copy = skus
    for key, _ in pricing_table.items():
        skus_copy = skus_copy.replace(key, '')

    if skus_copy != "":
        # If there are still elements in the SKUS, there are invalid items
        return -1

    current_basket = collect_current_basket(skus)
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
            case "K":
                basket_value += single_discount(value, item, pricing_table, 2, "two")
            case "Z" | "Y" | "X" | "T" | "S":
                pass
            case _:
                if value < 0:
                    value = 0
                basket_value += value * pricing_table[item]["one"]

    # Build a temporary SKUS to calculate optimized value
    temp_skus = get_leftover_basket(current_basket)

    left_pointer = 0
    temp_skus_size = len(temp_skus)
    while True:
        if left_pointer == temp_skus_size:
            # No more SKUS left , break out
            break

        right_pointer = left_pointer + 3

        if right_pointer > temp_skus_size:
            finality_skus = temp_skus[left_pointer:]
            leftover_basket = {
                "Z": finality_skus.count("Z"),
                "S": finality_skus.count("S"),
                "T": finality_skus.count("T"),
                "Y": finality_skus.count("Y"),
                "X": finality_skus.count("X")
            }
            for item, value in leftover_basket.items():
                if value < 0:
                    value = 0
                basket_value += value * pricing_table[item]["one"]
            break
        else:
            # Add 45 to the overall value and move to the next iteration
            basket_value += 45
            left_pointer += 3

    return basket_value
