nums = [1, 2, 3, 4, 5, 6]  # LIST - AN ITERABLE OBJECT

Itrt = iter(nums)  # FUNCTION TO CREATE ITERATOR

print(Itrt.__next__())  # METHOD TO CONTINUE ITERATING
print(Itrt.__next__())
print(next(Itrt))  # ANOTHER WAY OF CALLING NEXT

for i in nums:  # ITERATION USING FOR LOOP
    print(i)

# DEFINING OWN ITERATOR

class Firstfive:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration

Values = Firstfive()

for i in Values:
    print(i)

# GENERATORS

def Firstten():
    yield 1  # KEYWORD FOR GENERATOR
    yield 2

Values = Firstten()

print(next(Values))
print(next(Values))
