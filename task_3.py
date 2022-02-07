""" Fraction

Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) with appropriate
checking and error handling

```

class Fraction:

pass

x = Fraction(1/2)

y = Fraction(1/4)

x + y == Fraction(3/4)

"""


def nsd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


class Fraction:

    def __init__(self, fraction):
        self.fraction = fraction
        try:
            self.numerator, self.denominator = self.find_numerator_and_denominator(fraction)
            if self.denominator == 0:
                raise ZeroDivisionError('You can not divide by zero')
        except ValueError as exc:
            print('Give me fraction with / division sign')
            raise
        except TypeError as exc:
            print('Wrong type')
            raise
        except Exception as exc:
            print(exc)
            raise

    def __str__(self):
        return f'Fraction({self.numerator}/{self.denominator})'

    def find_numerator_and_denominator(self, fraction):
        try:
            temp_list = fraction.split('/')
            numerator = int(temp_list[0])
            denominator = int(temp_list[1])
            if numerator is None and denominator is None:
                raise ValueError('Wrong division sign')
            return numerator, denominator
        except ValueError as exc:
            print(exc)
            raise

    def check_type(self, other):
        if not isinstance(other, Fraction):
            raise TypeError('Wrong type')

    def __add__(self, other):
        try:
            self.check_type(other)
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            common = nsd(new_numerator, new_denominator)
            new_num = str(new_numerator // common) + '/' + str(new_denominator // common)
            return Fraction(new_num)
        except TypeError:
            print('Wrong type')
        except ValueError as exc:
            print(exc)

    def __sub__(self, other):
        try:
            self.check_type(other)
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            common = nsd(new_numerator, new_denominator)
            new_num = str(new_numerator // common) + '/' + str(new_denominator // common)
            return Fraction(new_num)
        except TypeError:
            print('Wrong type')
        except ValueError as exc:
            print(exc)

    def __mul__(self, other):
        try:
            self.check_type(other)
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            common = nsd(new_numerator, new_denominator)
            new_num = str(new_numerator // common) + '/' + str(new_denominator // common)
            return Fraction(new_num)
        except TypeError:
            print('Wrong type')
        except ValueError as exc:
            print(exc)

    def __truediv__(self, other):
        try:
            self.check_type(other)
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            common = nsd(new_numerator, new_denominator)
            new_num = str(new_numerator // common) + '/' + str(new_denominator // common)
            return Fraction(new_num)
        except TypeError:
            print('Wrong type')
        except ValueError as exc:
            print(exc)

    def __eq__(self, other):
        return self.__str__() == other.__str__()


def main():
    x = Fraction('1/2')
    y = Fraction('1/4')
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x + y == Fraction('3/4'))
    print(x + y == Fraction('2/4'))


if __name__ == '__main__':
    main()

# def find_top(self, fraction):
#     self._temp_fraction = list(''.join(fraction))
#     top = []
#
#     while self._temp_fraction:
#         if self._temp_fraction[0] == '/':
#             break
#         top.append(self._temp_fraction[0])
#         self._temp_fraction.remove(self._temp_fraction[0])
#     return int(''.join(top))
#
#
# def find_bottom(self, fraction):
#     bottom = [char for char in fraction if char != '/']
#     return int(''.join(bottom))
