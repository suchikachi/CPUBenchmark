from asyncio.windows_events import NULL
import math
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


    main()
        

def longTest():
    print("Beginning long test!")

    main()


pbar = ProgressBar()

'''def job():
    for i in pbar(range(5)):
        print(i)

job()'''

def sieve_of_eratosthenes(n):
    pnum  = [True for _ in range(n + 1)]
    pnum[0] = pnum[1] = False  # 0 and 1 are not prime numbers

    # apply sieve of eratosthenes algorithm
    for i in range(2, int(math.sqrt(n)) + 1):
        if pnum[i]:
            # mark all multiples of i as non-prime
            for j in range(i * i, n + 1, i):
                pnum[j] = False

    # return all prime values
    primes = [i for i in range(2, n + 1) if pnum[i]]
    return primes


if __name__ == "__main__":
    main()