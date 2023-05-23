import cpuinfo
import time

def __main__():
    print("pymark test")
    chooseVer(selection())

def selection():
    while (True):
        choice = int(input("1. Quick test (usually less accurate)\n2. Normal test (accurate)"))
        try:
            if choice == 1:
                return 1
            if choice == 2:
                return 2
        except:
            print("Error: Please choose a valid option")

def chooseVer(selection):
    if selection == 1:
        shortTest()
    if selection == 2:
        longTest()

def shortTest():
    print("Beginning short test!")
    for x in 15:
        print(x)

def longTest():
    print("Beginning long test!")
    for x in 50:
        print(x)