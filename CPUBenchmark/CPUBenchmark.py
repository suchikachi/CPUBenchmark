import cpuinfo
import easygui
from Color_Console import *
import time
from progressbar import ProgressBar



def main():
    li = [ 'black','bright white' ]
    
    print("PyMark test")
    color ( text = "red" )
    playSim(chooseVer())

def chooseVer():
    color ( text = "white" )
    while True:
        try:
            choice = int(input("1. Quick test (usually less accurate)\n2. Normal test (accurate)\n"))
            if choice == 1 or choice == 2:
                return choice
            else:
                easygui.msgbox("Error: Please enter a valid option!", title="you silly user!!")
        except:
            easygui.msgbox("Error: Please enter a valid option!", title="you silly user!!")

def playSim(type):
    if type == 1:
        shortTest()
    elif type == 2:
        longTest()

def shortTest():
    print("Beginning short test!")
    # todo short test
    main()
        

def longTest():
    print("Beginning long test!")
    # todo long test
    main()


pbar = ProgressBar()

def job():
    for i in pbar(range(5)):
        print(i)

job()


if __name__ == "__main__":
    main()