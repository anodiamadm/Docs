from abc import ABC,abstractmethod

class School(ABC):                              # ABSTRACT CLASS
    @abstractmethod
    def Student(self):                          # ABSTRACT METHOD
        pass

class Desk(School):                             # INHERITING ABSTRACT CLASS
    pass


Rupa = School()
Monika = Desk()

Rupa.Student()


# SECOND SCENARIO

class School(ABC):
    @abstractmethod
    def Student(self):
        pass

class Desk(School):                             # HAS OWN METHOD SO NOT INHERITING
    def Student(self):
        print("Studying")


Monika = Desk()
Monika.Student()
