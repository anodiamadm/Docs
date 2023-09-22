class A():

    def __init__(self):
        print("A init")

    def f1(self):
        print("This is f1 from A")

class B(A):

    def __init__(self):
        super().__init__()                      # CALLING SUPER CLASS INIT
        print("B init")

    def f2(self):
        print("This is f2 from B")

obj1 = B()                                      # A -> B



class A():

    def __init__(self):
        print("A init")

    def f1(self):
        print("This is f1 from A")

class B:

    def __init__(self):
        print("B init")

    def f2(self):
        print("This is f2 from B")

class C(B,A):
    def __init__(self):
        super().__init__()                      # B -> A (LEFT TO RIGHT) || MRO
        print("C init")

    def feat(self):
        super().f2()

obj2 = C()
obj2.feat()
