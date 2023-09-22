from threading import *
from time import sleep

class Hey(Thread):
    def run(self):
        for i in range(10):
            print("Hey")
            sleep(1)                     # SETTING EXECUTION TIME

class Bye(Thread):
    def run(self):
        for i in range(10):
            print("Bye")
            sleep(1)


T1 = Hey()
T2 = Bye()

T1.start()                               # IN-BUILT START CALLS RUN

sleep(0.5)                               # GAP BETWEEN TWO THREADS

T2.start()

T1.join()                                # MAKING MAIN WAIT TILL T1 IS DONE
T2.join()

print("End")                             # EXECUTED BY MAIN THREAD
