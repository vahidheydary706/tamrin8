class Time:
    def __init__(self):
        self.hour1 = int(input("Hour1: "))
        self.minutes1 = int(input("Minutes1: "))
        self.seconds1 = int(input("Seconds1: "))
        self.hour2 = int(input("Hour2: "))
        self.minutes2 = int(input("Minutes2: "))
        self.seconds2 = int(input("Seconds2: "))

    def show(self):
        print(f"{self.hour1} : {self.minutes1} : {self.seconds1}", end="\t")
        print(f"{self.hour2} : {self.minutes2} : {self.seconds2}")
    def sum(self):
        self.hour = self.hour1 + self.hour2
        self.minutes = self.minutes1 + self.minutes2
        self.seconds = self.seconds1 + self.seconds2

        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        if self.minutes >= 60:
            self.minutes -= 60
            self.hour += 1
        return f"{self.hour} : {self.minutes} : {self.seconds}"
    def show_sum(self):
        print(self.sum())
    def minus(self):
        self.hour = self.hour1 - self.hour2
        self.minutes = self.minutes1 - self.minutes2
        self.seconds = self.seconds1 - self.seconds2

        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        if self.minutes >= 60:
            self.minutes -= 60
            self.hour += 1
        return f"{self.hour} : {self.minutes} : {self.seconds}"
    def show_minus(self):
        print(self.minus())
r= Time()
r.show()
r.show_sum()
r.show_minus()