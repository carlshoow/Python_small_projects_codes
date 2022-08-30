
class Lottery:
    

    def __init__(self,min=1, max=60, max_numbers=6):
        #Attributes of the class
        self.min = min
        self.max = max
        self.max_numbers = max_numbers
        self.numbers = []


    def generate_numbers(self):
        from random import randint

        c = 0
        while c < self.max_numbers:
            n = randint(self.min, self.max)
            if n in self.numbers:
                c = c
            else:
                self.numbers.append(n)
                c += 1
        return self.numbers

megasena = Lottery(1, 60, 7)

print(sorted(megasena.generate_numbers()))












