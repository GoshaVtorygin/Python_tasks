import itertools

def factorial(number):
    if number == 1 or number == 0:
        return 1
    return number * factorial(number-1)

class Factorial:
    class FactIter:

        def __init__(self):
            self.i = 1

        def __next__(self):
            cur_fact = factorial(self.i)
            self.i += 1
            return cur_fact

    def __iter__(self):
        return Factorial.FactIter()

fact = Factorial()
for i, f in zip(itertools.count(1), itertools.islice(fact, 15)):
    print(i, f)
