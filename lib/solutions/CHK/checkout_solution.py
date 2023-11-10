
# noinspection PyUnusedLocal
# skus = unicode string


def get_pricing_table():
    return  {
        "A": {
            1: 50,
            3: 130
        },
        "B": {
            1: 30,
            2: 45
        },
        "C": {
            1: 20
        },
        "D": {
            1: 15
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
            # do something
        elif key == "B":
            # do something:
        else:
            basket_value += value * pricing_table[key]

    return basket_value



