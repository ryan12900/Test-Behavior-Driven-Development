import math

def cc_payoff(cc_balance, cc_interest_rate, months):
    try:
        cc_balance = float(cc_balance)
    except ValueError:
        return "CC balance input value must be numeric."
    try: 
        cc_interest_rate= float(cc_interest_rate)
    except ValueError:
        return "CC interest rate input value must be numeric."
    try:
        months = int(months)
    except ValueError:
        return "Desired months to payoff input value must be numeric."
    if cc_balance < 0:
        return "CC balance cannot be negative."
    if cc_interest_rate < 0:
        return "CC interest rate cannot be negative."
    if months < 0:
        return "Desired months to payoff cannot be negative."

    monthly_payment = 0
    total_interest = 0
    low_monthly_payment = cc_balance / months
    high_monthly_payment = (cc_balance * (1 + (cc_interest_rate/100.00/12 * months))) / months
    balance = cc_balance
    while balance != 0:
        monthly_payment = (low_monthly_payment + high_monthly_payment) / 2
        total_interest = 0
        balance = cc_balance
        m = 0
        while m < months:
            m += 1
            balance -= monthly_payment
            interest = balance * (cc_interest_rate/100.00/12)
            balance += interest
            total_interest += interest
        if balance <= 0:
            high_monthly_payment = monthly_payment
        elif balance >= 0:
            low_monthly_payment = monthly_payment
        balance = round(balance, 2)

    d = dict()
    d['Monthly Payment'] = round(monthly_payment, 2)
    d['Total Principal Paid'] = round(cc_balance, 2)
    d['Total Interest Paid'] = round(total_interest, 2)
    return d
    

def simpleSavingsCalc():
    return 0

def ccMinPaymentCalc(ccBalance, ccInterestRate, minPaymentPercent):
    try:
        math.isnan(ccBalance)
    except TypeError:
        return "CC balance input value must be numeric."
    try: 
        math.isnan(ccInterestRate)
    except TypeError:
        return "CC interest rate input value must be numeric."
    try:
        math.isnan(minPaymentPercent)
    except TypeError:
        return "Minimum payment percent input value must be numeric."
    if ccBalance < 0:
        return "CC balance cannot be negative."
    if ccInterestRate < 0:
        return "CC interest rate cannot be negative."
    if minPaymentPercent < 0:
        return "Minimum payment percent cannot be negative."
    if minPaymentPercent > 20:
        return "Minimum payment percent input value should not be greater than 20%."
    monthlyPayment = round((minPaymentPercent / 100.00) * ccBalance, 2)
    months = -1
    currentBalance = ccBalance 
    totalPayment = ccBalance
    while currentBalance > 0.00:
        currentPayment = round(currentBalance * (minPaymentPercent/100.00),2)
        interestAmnt = round(currentBalance * (ccInterestRate/100.00/12),2)
        if currentPayment < 15:
            currentPayment = 15
        
        currentBalance -= currentPayment
        currentBalance += interestAmnt
        totalPayment += interestAmnt
        months += 1

    totalPayment = round(totalPayment, 2)
    d = dict()
    d['Monthly Payment'] = monthlyPayment
    d['Months'] = months
    d['Total Payment'] = totalPayment
    return d

def mortgageCalc():
    return 0

def cdCalc():
    return 0


def main():
    while(1):
        option = int(input("Please select a bank function to execute:\n1. Credit Card Payoff\n2. Simple Savings Calculator\n3. Credit Card Minimum Payment Calculator\n4. Mortgage Calculator\n5. CD Calculator\n6. Exit\n"))
        if option == 1:
            cc_balance = float(input("Please enter the CC balance (eg. 1234.56): "))
            cc_interest_rate = float(input("Please enter the CC interest rate (eg. 12.3): "))
            months = int(input("Please enter the desired months to payoff (eg. 12): "))
            result = cc_payoff(cc_balance, cc_interest_rate, months)
            print(result)
        elif option == 2:
            simpleSavingsCalc()
        elif option == 3:
            ccBalance = float(input("Please enter the CC balance (eg. 1234.56): "))
            ccInterestRate = float(input("Please enter the CC interest rate (eg. 12.3): "))
            minPaymentPercent = float(input("Please enter the minimum payment percentage (eg 12.3): "))
            result = ccMinPaymentCalc(ccBalance, ccInterestRate, minPaymentPercent)
            print(result)
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