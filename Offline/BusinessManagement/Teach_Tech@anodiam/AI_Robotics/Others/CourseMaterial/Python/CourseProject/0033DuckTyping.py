class Human:
    def run(self):
        print("Runs on two feet")

class Tiger:
    def run(self):
        print("Runs on four feet")

class Fish:
    def swim(self):
        print("Swims in water")

for entity in Human(), Tiger(), Fish():          # CREATING AN OBJECT NAMED ENTITY FROM ALL THREE CLASSES
    entity.run()                                 # HUMAN & TIGER CLASSES HAVE ATTRIBUTES WITH SAME NAME
