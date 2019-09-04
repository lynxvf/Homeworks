from math import gcd


class Fraction:

    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):
        res_num = self.num * other_fraction.den + self.den * other_fraction.num
        res_den = self.den * other_fraction.den
        return Fraction(*self.reduce_frac(res_num, res_den))

    def __sub__(self, other_fraction):
        res_num = self.num * other_fraction.den - self.den * other_fraction.num
        res_den = self.den * other_fraction.den
        return Fraction(*self.reduce_frac(res_num, res_den))

    def __mul__(self, other_fraction):
        res_num = self.num * other_fraction.num
        res_den = self.den * other_fraction.den
        return Fraction(*self.reduce_frac(res_num, res_den))

    def __truediv__(self, other_fraction):
        res_num = self.num * other_fraction.den
        res_den = self.den * other_fraction.num
        return Fraction(*self.reduce_frac(res_num, res_den))

    def reduce_frac(self, numerator, denominator):
        g_c_d = gcd(numerator, denominator)
        return numerator // g_c_d, denominator // g_c_d


if __name__ == '__main__':
    fraction1 = Fraction(3, 6)
    fraction2 = Fraction(5, 9)
    print(f"{fraction1} / {fraction2} =", fraction1 / fraction2)
    print(f"{fraction1} + {fraction2} =", fraction1 + fraction2)
    print(f"{fraction1} - {fraction2} =", fraction1 - fraction2)
    print(f"{fraction1} * {fraction2} =", fraction1 * fraction2)
    print(f"{fraction1} + {fraction2} * {fraction2} - {fraction1} / {fraction2}=",
          fraction1 + fraction2 * fraction2 - fraction1 / fraction2)
