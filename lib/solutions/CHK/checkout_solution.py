

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    pricing_table = {
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
    
    current_basket = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
    }


