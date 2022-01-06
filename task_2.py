"""

Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total
price of stock.

"""

# Function:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def work_with_dictionary():
    new_dict = {}
    for key_stock, value_stock in stock.items():
        for key_prices, value_prices in prices.items():
            if key_stock == key_prices:
                full_price = int(value_stock * value_prices)
                new_dict[key_stock] = full_price
    return new_dict


def main():
    for key, value in work_with_dictionary().items():
        key_upper = key.title()
        print(f'{key_upper} price: {value}')


if __name__ == '__main__':
    main()
