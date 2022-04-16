from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup


# @dataclass
# class HCPVariant:
#     price: int
#     size: str


@dataclass
class HairCareProduct:
    old_price: str
    new_price: str
    product_link: str
    name: str
    brand: str
    descr: str
    image: str
    volume: str

    def load_me(self):
        pass


class ParseConnect:
    BASE_URL = 'https://sisters.co.ua/v-nezmivn-zasobi'
    session = requests.Session()
    res = session.get(BASE_URL, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    })
    bs = BeautifulSoup(res.text, 'lxml')
    main_div = bs.find_all('div', class_='card')

    @classmethod
    def fill_info(cls):
        for link in cls.main_div:
            name = link.find('div', class_='card-inner').text.strip()
            image = 'https://sisters.co.ua' + link.find('img').attrs['src']
            brand = link.find('div', class_='card-brand').text.strip()
            new_price = link.find('p')
            # find('div', class_='card-price has-text-centered').
            # k = new_price.find('p')
            print(new_price)


# class HCPList:
#     list_of_hcp = []
#
#     def __iter__(self):
#         i = 0
#
#         self.setup_class()
#         self.fill_info(self.bs_data())
#
#     def setup_class(self):
#         self.list_of_hcp = []
#
#     @staticmethod
#     def bs_data() -> BeautifulSoup:
#         res = requests.get('https://cipollino.ua/pizza', headers={
#             'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
#         })
#         return BeautifulSoup(res.text, 'lxml')
#
#     def fill_info(self, bs: BeautifulSoup):
#         for link in ParseConnect.main_div('div', class_='card'):
#             self.pizza_list.append(self.parse_product_block(link))
#
#     @staticmethod
#     def parse_product_block(link: BeautifulSoup) -> Pizza:
#         pizza_name = link.find('div', class_="cipollino-product-name").text.strip()
#         pizza_descr = link.find('div', class_='cipollino-product-ingredients').text.strip()
#         pizza_image = link.find('img').attrs['data-src']
#         price_class = link.find_all('div', class_="cipollino-product-option-price")
#         pizza_prices = []
#
#         for new_link in price_class:
#             price = new_link.find('p', class_='cipollino-price').text
#             weight = new_link.find('p', class_='cipollino-weight').text
#             pizza = PizzaPrice(price=price, weight=weight)
#             pizza_prices.append(pizza)
#
#         return Pizza(name=pizza_name, descr=pizza_descr, img=pizza_image, variants=pizza_prices)
#
#     def __next__(self) -> Pizza:
#         if self.pizza_list:
#             if self.i <= len(self.pizza_list) - 1:
#                 self.i += 1
#                 return self.pizza_list[self.i - 1]
#         raise StopIteration


# print(ParseConnect.main_div)

b = ParseConnect
b.fill_info()
