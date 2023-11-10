
# noinspection PyUnusedLocal
# skus = unicode string


def get_pricing_table():
    return  {
        "A": {
            "one": 50,
            "triple": 130
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
        }
    }

def checkout(skus):
    pricing_table = get_pricing_table()

    skus_copy = skus
    for key, _ in pricing_table:
        skus_copy.replace(key, "")

    if skus_copy != "":
        # If there are still elements in the SKUS, there are invalid items
        return -1

    current_basket = {
        "A": skus.count("A"),
        "B": skus.count("B"),
        "C": skus.count("C"),
        "D": skus.count("D"),
    }
    basket_value = 0

    for key, value in current_basket:
        if key == "A":
            basket_value += (value // 3) * pricing_table[key]["triple"]
            basket_value += (value % 3) * pricing_table[key]["one"]
            # do something
        elif key == "B":
            basket_value += (value // 2) * pricing_table[key]["double"]
            basket_value += (value // 2) * pricing_table[key]["one"]
        else:
            basket_value += value * pricing_table[key]["one"]

    return basket_value



