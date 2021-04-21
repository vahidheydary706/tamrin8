class Fraction:
    def __init__(self):
        self.s1 = int(input("S1: "))
        self.m1 = int(input("m1: "))
        self.s2 = int(input("S2: "))
        self.m2 = int(input("m2: "))

    def sum(self):
        return f" Sum: {(self.s1 * self.m2) + (self.s2 * self.m1)} / {self.m1 * self.m2} "

    def show_sum(self):
        print(self.sum())

    def multi(self):
        return f" Multiplication: {(self.s1 * self.s2)} / {self.m1 * self.m2} "

    def show_multi(self):
        print(self.multi())

    def minus(self):
        m = self.m1 * self.m2
        return f" Minus: {(m // self.m1) * self.s1 - (m // self.m2) * self.s2} / {m} "

    def show_minus(self):
        print(self.minus())

    def divide(self):
        return f" Divide: {self.s1 * self.m2} / {self.s2 * self.m1} "

    def show_divide(self):
        print(self.divide())


r = Fraction()

r.show_sum()

r.show_multi()

r.show_minus()

r.show_divide()