import itertools

class Factorial:
    class FactIter:

        def __init__(self):
            self.i = 1
            self.cur_fact = 1

        def __next__(self):
            self.cur_fact *= self.i
            self.i += 1
            return self.cur_fact

    def __iter__(self):
        return Factorial.FactIter()

fact = Factorial()
for i, f in zip(itertools.count(1), itertools.islice(fact, 15)):
    print(i, f)
