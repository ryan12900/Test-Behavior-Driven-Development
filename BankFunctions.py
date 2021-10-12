import math

def cc_payoff():
    return 0

def simpleSavingsCalc(initialDeposit, monthlyContrib, timePeriod, interestRate):
    try:
        initialDeposit = float(initialDeposit)
    except ValueError:
        return "Initial deposit value must be numeric."
    try:
        monthlyContrib = float(monthlyContrib)
    except ValueError:
        return "Monthly contribution value must be numeric."
    try:
        timePeriod = float(timePeriod)
    except ValueError:
        return "Time period must be numeric, and in year form. e.g: 2.5 (years)"
    try:
       interestRate = float(interestRate)
    except ValueError:
        return "Interest rate value must be numeric."
    if initialDeposit < 0:
        return "Initial deposit cannot be negative."
    if monthlyContrib < 0:
        return "Monthly contribution cannot be negative."
    if timePeriod < 0:
        return "Time period cannot be negative."
    if interestRate < 0:
        return "Interest rate cannot be negative."

    months = math.floor(timePeriod * 12)
    count = 0
    totalBalance = initialDeposit + 0.0
    interest = interestRate / 100.0
    accumInterest = 0.0

    while (count < months):
        totalBalance += monthlyContrib
        count+=1
        if (count % 12 == 0):
            accumInterest += (totalBalance * interest)
            totalBalance = round(((totalBalance * interest) + totalBalance),2)
        
    
    totalBalance = round(totalBalance, 2)
    totalContrib = round((monthlyContrib * months),2)
    accumInterest = round(accumInterest,2)
    d = dict()

    d['Total Savings balance'] = totalBalance
    d['Total Contributions'] = totalContrib
    d['Interest Earned'] = accumInterest

    return d

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
            initialDeposit = input("Please enter the initial deposit amount (eg. 1000.0): ")
            monthlyContrib = input("Please enter the desired monthly contribution amount (e.g 100.0): ")
            timePeriod = input("Please enter a numerical time period in years (e.g 2.5 ): ")
            interestRate = input("Please enter an interest rate as a percentage (e.g 10.52): ")
            result = simpleSavingsCalc(initialDeposit,monthlyContrib, timePeriod, interestRate)
            print(result)
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