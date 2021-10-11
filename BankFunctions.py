def ccPayoff():
    return 0

def simpleSavingsCalc():
    return 0

def ccMinPaymentCalc():
    return 0

def mortageCalc():
    return 0

def cdCalc():
    return 0:


def main():
    while(1):
        option = input("Please select a bank function to execute:\n1. Credit Card Payoff\n2. Simple Savings Calculator\n3. Credit Card Minimum Payment Calculator\n4. Mortgage Calculator\n5. CD Calculator\n6. Exit\n")
        if option == 1:
            ccPayoff()
        elif option == 2:
            simpleSavingsCalc()
        elif option == 3:
            ccMinPaymentCalc()
        elif option == 4:
            mortgageCalc()
        elif option == 5:
            cdCalc()
        elif option == 6:
            print("Quitting program.")
            break
        else:
            print("Invalid input, please select a valid option.")

if __name__ == '__main__':
    main()