"""Modulo cal"""


class Calc():
    """Modulo cal"""
    def soma(self, x: int, y: int):
        """Modulo cal"""
        return 'A soma é:', x + y

    def sub(self, x: int, y: int):
        """Modulo cal"""
        return 'A sub é:', x - y

calc = Calc()

print(calc.soma(15, 25))

print(calc.sub(15, 25))
