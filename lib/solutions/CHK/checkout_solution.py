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
        "B": skus.count("B"),
        "C": skus.count("C"),
        "D": skus.count("D"),
        "E": skus.count("E"),
    }

    basket_value = 0

    for item, value in current_basket.items():
        if item == "A":
            basket_value += value // 5 * pricing_table[item]["quintuple"]
            quintuple_leftover = value % 5
            basket_value += (quintuple_leftover // 3) * pricing_table[item]["triple"]
            triple_leftover = quintuple_leftover % 3
            basket_value += triple_leftover * pricing_table[item]["one"]
        elif item == "B":
            basket_value += (value // 2) * pricing_table[item]["double"]
            basket_value += (value % 2) * pricing_table[item]["one"]
        elif item == "E":
            price_deals = value // 2
            basket_value += price_deals * 2 * pricing_table[item]["one"]
            price_removal = (value % 2) - price_deals
            if price_removal < 0:
                price_removal = 0
            basket_value += price_removal * pricing_table[item]["one"]
        else:
            basket_value += value * pricing_table[item]["one"]

    return basket_value




