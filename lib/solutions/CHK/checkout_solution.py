# noinspection PyUnusedLocal
# skus = unicode string


def get_pricing_table():
    return {
        "A": {
            "one": 50,
            "triple": 130,
            "quintuple": 200
        },
        "B": {
            "one": 30,
            "double": 45
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
        }
    }


def checkout(skus):
    pricing_table = get_pricing_table()

    skus_copy = skus
    for key, _ in pricing_table.items():
        skus_copy = skus_copy.replace(key, '')

    if skus_copy != "":
        # If there are still elements in the SKUS, there are invalid items
        return -1

    current_basket = {
        "A": skus.count("A"),
        "E": skus.count("E"),
        "B": skus.count("B"),
        "C": skus.count("C"),
        "D": skus.count("D"),
        "F": skus.count("F"),
    }

    basket_value = 0

    for item, value in current_basket.items():
        match item:
            case "A":
                # Calculate best deal for 5
                basket_value += value // 5 * pricing_table[item]["quintuple"]
                quintuple_leftover = value % 5
                # Calculate best deal for 3
                basket_value += (quintuple_leftover // 3) * pricing_table[item]["triple"]
                triple_leftover = quintuple_leftover % 3
                # Calculate leftovers
                basket_value += triple_leftover * pricing_table[item]["one"]
            case "B":
                if value < 0:
                    value =  0
                basket_value += (value // 2) * pricing_table[item]["double"]
                basket_value += (value % 2) * pricing_table[item]["one"]
            case "E":
                # Remove extra deals and calculate as regular
                discounted_amount = value // 2
                current_basket["B"] = current_basket["B"] - discounted_amount
                basket_value += value * pricing_table[item]["one"]
            case "F":
                # Remove extra deals and calculate as regular
                if value > 2:
                    items_to_pay = 0
                    while True:
                        if value <= 0:
                            break
                        items_to_pay += 2
                        value -= 2
                        if value > 0:
                            value - 1
                    basket_value += items_to_pay * pricing_table[item]["one"]
                else:
                    basket_value += value * pricing_table[item]["one"]
            case _:
                basket_value += value * pricing_table[item]["one"]

    return basket_value
