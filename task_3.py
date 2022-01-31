"""Product Store

Write a class Product that has three attributes:

type
name
price

Then create a class ProductStore, which will have some Products and will operate with all products in the store. All
methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional
classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30
percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input
identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case
raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.

```

class Product:

    pass

class ProductStore:

pass

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product(Food, 'Ramen, 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell(‘Ramen’, 10)

assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)

"""


# Solution:

class Product:
    dictionary_of_product = {}

    def __init__(self, type_1, name, price):
        self.type_1 = type_1
        self.name = name
        self.price = price
        Product.dictionary_of_product[self.name] = [self.type_1, self.price]

    def __repr__(self):
        return f'Product name: {self.name}, product type: {self.type_1}, product price: {self.price}'


class ProductStore:
    dictionary_of_store = {}
    dictionary_of_store_price = {}

    def __init__(self):
        self.income = 0

    def add(self, product, amount):
        product = product.name
        try:
            for k in Product.dictionary_of_product.keys():
                if product not in Product.dictionary_of_product.keys():
                    raise ValueError
                if k == product:
                    ProductStore.dictionary_of_store[product] = amount
                    for x, y in Product.dictionary_of_product.items():
                        if x == product:
                            margin_price = y[1] + y[1] * 0.3
                            ProductStore.dictionary_of_store_price[product] = [y[0], margin_price]
        except ValueError:
            print('This is mistake! ValueError')

    def set_discount(self, identifier, percent, type_product='name'):
        percent = percent.replace('%', '')
        for x, y in ProductStore.dictionary_of_store_price.items():
            if x == identifier or y[0] == type_product:
                y[1] -= y[1] * int(percent) * 0.01

    def sell_product(self, product_name, amount):
        for x, y in ProductStore.dictionary_of_store.items():
            if x == product_name and y >= amount:
                ProductStore.dictionary_of_store[x] -= amount
                for k, v in ProductStore.dictionary_of_store_price.items():
                    if k == product_name:
                        income = v[1] * amount
                        self.income += income

    def get_income(self):
        print(f'\nIncome: {self.income} $')

    def get_all_products(self):
        print('\nAll products:')
        for x, y in ProductStore.dictionary_of_store_price.items():
            print(f'\nGood - {x}: \ntype = {y[0]} \nprice = {y[1]}')

    def get_product_info(self, product_name):
        for x, y in ProductStore.dictionary_of_store.items():
            if x == product_name:
                get_tuple = (x, y)
                print(f'\n{get_tuple}')


def main():
    p_1 = Product('Sport', 'T-Shirt', 100)
    p_2 = Product('Food', 'Ramen', 1.5)

    # print(Product.dictionary_of_product)

    s = ProductStore()
    s.add(p_2, 300)
    s.add(p_1, 10)

    # print(ProductStore.dictionary_of_store)
    # print(ProductStore.dictionary_of_store_price)

    s.set_discount('Ramen', '30%')
    print(ProductStore.dictionary_of_store_price)
    s.sell_product('Ramen', 25)
    print(ProductStore.dictionary_of_store)
    # print(s.income)
    s.get_income()
    s.get_all_products()
    s.get_product_info('Ramen')

    # s.add("ssss", 23)
    # print(ProductStore.dictionary_of_store)


if __name__ == '__main__':
    main()
