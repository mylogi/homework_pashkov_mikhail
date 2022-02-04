""" Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list
for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books

```

class Library:

    pass



class Book:

    pass



class Author:

    pass

"""


# Solution:

class Author:

    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday

    def __repr__(self):
        return str(f'Name: {self.name}\nCountry: {self.country}\nBirthday: {self.birthday}')

    # def __str__(self):
    #     return self.__repr__()


class Book:
    books = 0
    books_dict = {}

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.books += 1
        Book.books_dict[self.name] = {'author': author, 'year': year}

    def __repr__(self):
        return str(f'Name: "{self.name}"\nAuthor: {self.author}\nYear: {self.year}')

    # def __str__(self):
    #     return self.__repr__()


class Library:
    books_list_library = {}
    number_of_books = 0

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return str(f'Name: {self.name}\nNumber of books: {self.number_of_books}')

    def new_book(self, name: str, year: int, author: Author):
        for key, value in Book.books_dict.items():
            if key == name and value['author'] == author and value['year'] == year:
                self.books_list_library[name] = Book.books_dict[name]
                self.number_of_books += 1

    def group_by_author(self, author: Author):
        print([
            (key, value)
            for key, value in self.books_list_library.items()
            if value['author'] == author
        ], '\n')

    def group_by_year(self, year: int):
        print([
            (key, value)
            for key, value in self.books_list_library.items()
            if value['year'] == year
        ], '\n')


def main():
    a_1 = Author('Alexander Pushkin', 'Russian empire', '26/05/1799')
    a_2 = Author('William Shakespeare', 'England', '26/04/1564')
    b_1 = Book('Richard III', 1591, a_2)
    b_2 = Book('Eugene Onegin', 1833, a_1)
    b_3 = Book('King Lear', 1606, a_2)
    l_1 = Library('l_1')
    # print(Book.books_dict)
    l_1.new_book('Richard III', 1591, a_2)
    l_1.new_book('Eugene Onegin', 1833, a_1)
    l_1.new_book('King Lear', 1606, a_2)
    print(l_1.books_list_library, '\n')
    l_1.group_by_author(a_2)
    l_1.group_by_year(1606)
    print(f'Number of books: {Book.books}', '\n')
    print(a_1, '\n')
    print(b_1, '\n')
    print(l_1)


if __name__ == '__main__':
    main()
