def __main__():
    print("pymark test")
    chooseVersion()

def chooseVersion():
    while (True):
        choice = int(input("1. Quick test (usually less accurate)\n2. Normal test (accurate)"))
        try:
            if choice == 1:
                pass
                #shortTest()
            if choice == 2:
                pass
                #longTest()
        except:
            print("Error: Please choose a valid option")