import math

def cc_payoff():
    return 0

def simple_savings_calc():
    return 0

def cc_min_payment_calc(cc_balance, cc_interest_rate, min_payment_percent):
    try:
        cc_balance = float(cc_balance)
    except ValueError:
        return "CC balance input value must be numeric."
    try: 
        cc_interest_rate = float(cc_interest_rate)
    except ValueError:
        return "CC interest rate input value must be numeric."
    try:
        min_payment_percent = float(min_payment_percent)
    except ValueError:
        return "Minimum payment percent input value must be numeric."
    if cc_balance < 0:
        return "CC balance cannot be negative."
    if cc_interest_rate < 0:
        return "CC interest rate cannot be negative."
    if min_payment_percent < 0:
        return "Minimum payment percent cannot be negative."
    if min_payment_percent > 20:
        return "Minimum payment percent input value should not be greater than 20%."
    monthly_payment = round((min_payment_percent / 100.00) * cc_balance, 2)
    months = -1
    current_balance = cc_balance 
    total_payment = cc_balance
    while current_balance > 0.00:
        current_payment = round(current_balance * (min_payment_percent/100.00),2)
        interest_amnt = round(current_balance * (cc_interest_rate/100.00/12),2)
        if current_payment < 15:
            current_payment = 15

        current_balance -= current_payment
        current_balance += interest_amnt
        total_payment += interest_amnt
        months += 1

    total_payment = round(total_payment, 2)
    d = dict()
    d['Monthly Payment'] = monthly_payment
    d['Months'] = months
    d['Total Payment'] = total_payment
    return d

def mortgage_calc():
    return 0

def cd_calc():
    return 0


def main():
    while(1):
        option = int(input("Please select a bank function to execute:\n1. Credit Card Payoff\n2. Simple Savings Calculator\n3. Credit Card Minimum Payment Calculator\n4. Mortgage Calculator\n5. CD Calculator\n6. Exit\n"))
        if option == 1:
            cc_payoff()
        elif option == 2:
            simple_savings_calc()
        elif option == 3:
            cc_balance =input("Please enter the CC balance (eg. 1234.56): ")
            cc_interest_rate = input("Please enter the CC interest rate (eg. 12.3): ")
            min_payment_percent = input("Please enter the minimum payment percentage (eg 12.3): ")
            result = cc_min_payment_calc(cc_balance, cc_interest_rate, min_payment_percent)
            print(result)
        elif option == 4:
            mortgage_calc()
        elif option == 5:
            cd_calc()
        elif option == 6:
            print("Quitting program.")
            break
        else:
            print("Invalid input, please select a valid option.")

if __name__ == '__main__':
    main()