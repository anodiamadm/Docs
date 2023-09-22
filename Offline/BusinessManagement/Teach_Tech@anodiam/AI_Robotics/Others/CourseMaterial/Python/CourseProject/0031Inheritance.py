
class A():                                         # SUPER CLASS (PARENT)
    def f1(self):
        print("This is f1 from A")

class B(A):                                        # SINGLE LEVEL INHERITANCE || SUB CLASS (CHILD)
    def f2(self):
        print("This is f2 from B")

class C(B):                                        # MULTI LEVEL INHERITANCE
    def f3(self):
        print("This is f3 from C")

objC = C()

objC.f1()
objC.f2()
objC.f3()


class D:
    def f4(self):
        print("This is f4 from D")

class E:
    def f5(self):
        print("This is f5 from E")


class F(E,D):                                       # MULTIPLE INHERITANCE
    def f6(self):
        print("This is f6 from F")

objF = F()

objF.f4()
objF.f5()
objF.f6()
