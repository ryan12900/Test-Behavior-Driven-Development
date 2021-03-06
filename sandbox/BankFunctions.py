import math
from flask import jsonify
import json

def cc_payoff(cc_balance, cc_interest_rate, months):
    try:
        cc_balance = float(cc_balance)
    except ValueError:
        return jsonify({'result': "CC balance input value must be numeric."})
    try: 
        cc_interest_rate= float(cc_interest_rate)
    except ValueError:
        return jsonify({'result':"CC interest rate input value must be numeric."})
    try:
        months = int(months)
    except ValueError:
        return jsonify({'result':"Desired months to payoff input value must be numeric."})
    if cc_balance < 0:
        return jsonify({'result':"CC balance cannot be negative."})
    if cc_interest_rate < 0:
        return jsonify({'result':"CC interest rate cannot be negative."})
    if months < 0:
        return jsonify({'result':"Desired months to payoff cannot be negative."})

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
    return json.dumps(d)
    #return d
    

def simple_savings_calc(initial_deposit, monthly_contrib, time_period, interest_rate):
    try:
        initial_deposit = float(initial_deposit)
    except ValueError:
        return jsonify({'result': "Initial deposit value must be numeric."})
    try:
        monthly_contrib = float(monthly_contrib)
    except ValueError:
        return jsonify({'result': "Monthly contribution value must be numeric."})
    try:
        time_period = float(time_period)
    except ValueError:
        return jsonify({'result': "Time period must be numeric, and in year form. e.g: 2.5 (years)"})
    try:
       interest_rate = float(interest_rate)
    except ValueError:
        return jsonify({'result': "Interest rate value must be numeric."})
    if initial_deposit < 0:
        return jsonify({'result': "Initial deposit cannot be negative."})
    if monthly_contrib < 0:
        return jsonify({'result': "Monthly contribution cannot be negative."})
    if time_period < 0:
        return jsonify({'result': "Time period cannot be negative."})
    if interest_rate < 0:
        return jsonify({'result': "Interest rate cannot be negative."})

    months = math.floor(time_period * 12)
    count = 0
    total_balance = initial_deposit + 0.0
    interest = interest_rate / 100.0
    accum_interest = 0.0

    while (count < months):
        total_balance += monthly_contrib
        count+=1
        if (count % 12 == 0):
            accum_interest += (total_balance * interest)
            total_balance = round(((total_balance * interest) + total_balance),2)
        
    
    total_balance = round(total_balance, 2)
    total_contrib = round((monthly_contrib * months),2)
    accum_interest = round(accum_interest,2)
    d = dict()

    d['Total Savings balance'] = total_balance
    d['Total Contributions'] = total_contrib
    d['Interest Earned'] = accum_interest

    return json.dumps(d)

def cc_min_payment_calc(cc_balance, cc_interest_rate, min_payment_percent):
    try:
        cc_balance = float(cc_balance)
    except ValueError:
        return jsonify({'result': "CC balance input value must be numeric."})
    try: 
        cc_interest_rate = float(cc_interest_rate)
    except ValueError:
        return jsonify({'result': "CC interest rate input value must be numeric."})
    try:
        min_payment_percent = float(min_payment_percent)
    except ValueError:
        return jsonify({'result': "Minimum payment percent input value must be numeric."})
    if cc_balance < 0:
        return jsonify({'result': "CC balance cannot be negative."})
    if cc_interest_rate < 0:
        return jsonify({'result': "CC interest rate cannot be negative."})
    if min_payment_percent < 0:
        return jsonify({'result': "Minimum payment percent cannot be negative."})
    if min_payment_percent > 20:
        return jsonify({'result': "Minimum payment percent input value should not be greater than 20%."})
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
    return json.dumps(d)

def mortgage_calc(home_price, down_payment, loan_length, interest_rate):
    try:
        if not float(loan_length).is_integer():
            return jsonify({'result': "Loan length in years must be an integer"})
        loan_length = int(loan_length)
    except(ValueError):
        return jsonify({'result': "Loan length in years must be an integer"})
    try:
        home_price = float(home_price)
    except(ValueError):
        return jsonify({'result': "Home price must be a float"})
    try:
        down_payment = float(down_payment)
    except(ValueError):
        return jsonify({'result': "Down payment percentage must be a float"})
    try:
        interest_rate = float(interest_rate)
    except(ValueError):
        return jsonify({'result': "Interest rate must be a float"})

    if home_price < 0:
        return jsonify({'result': "Home price should not be negative"})
    if down_payment < 0:
        return jsonify({'result': "Down payment should not be negative"})
    if loan_length < 0:
        return jsonify({'result': "Loan length should not be negative"})
    if interest_rate < 0:
        return jsonify({'result': "Interest rate should not be negative"})
    if(down_payment > 100):
        return jsonify({'result': "Down payment should not be over 100%"})

    r = interest_rate / 1200
    n = 12 * loan_length
    p = home_price*(1-down_payment/100)
    m = p * ((r*(1+r)**n) / (((1+r)**n)-1))

    d = dict()
    d['Monthly Payment'] = round(m, 2)
    d['Amount Paid in Interest'] = round(m * n - p, 2)
    d['Amount Paid in Principle'] = round(p, 2)
    d['Total Amount Paid'] = round(m * n, 2)
    return json.dumps(d)
    #return d

def cdCalc(init_Deposit, year_Period, interest_Rate):
    try:
        math.isnan(init_Deposit)
    except TypeError:
        return jsonify({'result': "Initial deposit input value must be numeric."})
    try: 
        math.isnan(year_Period)
    except TypeError:
        return jsonify({'result': "Period in years input value must be numeric."})
    try:
        math.isnan(interest_Rate)
    except TypeError:
        return jsonify({'result': "Interest rate input value must be numeric."})
    if init_Deposit < 0:
        return jsonify({'result': "Initial deposit cannot be negative."})
    if year_Period < 0:
        return jsonify({'result': "Period in years cannot be negative."})
    if interest_Rate < 0:
        return jsonify({'result': "Interest rate cannot be negative."})

    tot_Balance = init_Deposit
    tot_Interest = 0
    months = math.floor(year_Period*12)
    tot_Balance = round(init_Deposit*((1+(0.01*interest_Rate)) ** (months/12)),2)
    tot_Interest= round(tot_Balance - init_Deposit,2)
    d = dict()
    d['Total Balance'] = tot_Balance
    d['Total Interest'] = tot_Interest
    return json.dumps(d)
    #return d


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
            initial_deposit = input("Please enter the initial deposit amount (eg. 1000.00): ")
            monthly_contrib = input("Please enter the desired monthly contribution amount (e.g 100.00): ")
            time_period = input("Please enter a numerical time period in years (e.g 2.5 ): ")
            interest_rate = input("Please enter an interest rate as a percentage (e.g 10.52): ")
            result = simple_savings_calc(initial_deposit,monthly_contrib, time_period, interest_rate)
            print(result)
        elif option == 3:
            cc_balance =input("Please enter the CC balance (eg. 1234.56): ")
            cc_interest_rate = input("Please enter the CC interest rate (eg. 12.3): ")
            min_payment_percent = input("Please enter the minimum payment percentage (eg 12.3): ")
            result = cc_min_payment_calc(cc_balance, cc_interest_rate, min_payment_percent)
            print(result)
        elif option == 4:
            home_price = input("Enter the home price: ")
            down_payment = input("Enter the down payment as a percentage: ")
            loan_length = input("Enter the loan length in years: ")
            interest_rate = input("Enter the interest rate: ")
            result = mortgage_calc(home_price, down_payment, loan_length, interest_rate)
            print(result)
        elif option == 5:
            init_Deposit = float(input("Please enter the initial deposit amount (eg. 1000.50): "))
            year_Period = float(input("Please enter the period in years(eg. 2.5): "))
            interest_Rate = float(input("Please enter the interest rate calculated yearly (eg. 10.5): "))
            result = cdCalc(init_Deposit,year_Period,interest_Rate)
            print(result)
        elif option == 6:
            print("Quitting program.")
            break
        else:
            print("Invalid input, please select a valid option.")

if __name__ == '__main__':
    main()