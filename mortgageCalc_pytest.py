import BankFunctions

def test_negative_home_price():
    assert BankFunctions.mortgage_calc(-480000, 50, 30, 10) == "Home price should not be negative"
    print("--Should reject a negative home price input--")

def test_negative_down_payment():
    assert BankFunctions.mortgage_calc(480000, -50, 30, 10) == "Down payment should not be negative"
    print("--Should reject a negative down payment input--")

def test_negative_loan_length():
    assert BankFunctions.mortgage_calc(480000, 50, -30, 10) == "Loan length should not be negative"
    print("--Should reject a negative loan length input--")

def test_negative_interest_rate():
    assert BankFunctions.mortgage_calc(480000, 50, 30, -10) == "Interest rate should not be negative"
    print("--Should reject a negative interest rate input--")

def test_exceeded_down_payment():
    assert BankFunctions.mortgage_calc(480000, 101, 30, 10) == "Down payment should not be over 100%"
    print("--Should reject a down payment input over 100--")

def test_nan_home_price():
    assert BankFunctions.mortgage_calc("Yarp", 50, 30, 10) == "Home price must be a float"
    print("--Should reject a home price that is not a float--")

def test_nan_down_payment():
    assert BankFunctions.mortgage_calc(480000, "Yarp", 30, 10) == "Down payment percentage must be a float"
    print("--Should reject a down payment that is not a float--")

def test_nan_loan_length():
    assert BankFunctions.mortgage_calc(480000, 50, "Yarp", 10) == "Loan length in years must be an integer"
    print("--Should reject a loan length that is not a int--")

def test_nan_interest_rate():
    assert BankFunctions.mortgage_calc(480000, 50, 30, "Yarp") == "Interest rate must be a float"
    print("--Should reject a interest rate that is not a float--")

def test_float_loan_length():
    assert BankFunctions.mortgage_calc(480000, 50, 30.5, 10) == "Loan length in years must be an integer"
    print("--Should reject a float loan length--")

def test_mortgage_calc1():
    d = dict()
    d['Monthly Payment'] = 2106.17
    d['Amount Paid in Interest'] = 518221.84
    d['Amount Paid in Principle'] = 240000.00
    d['Total Amount Paid'] = 758221.84
    assert BankFunctions.mortgage_calc(480000, 50, 30, 10) == d
    print("--Should accurately calculate the monthly payment, the amount paid in interest, the amount paid in principle, and the total amount paid based on inputs--")

def test_mortgage_calc2():
    d = dict()
    d['Monthly Payment'] = 710.85
    d['Amount Paid in Interest'] = 19801.75
    d['Amount Paid in Principle'] = 65500.33
    d['Total Amount Paid'] = 85302.08
    assert BankFunctions.mortgage_calc(100000.5, 34.5, 10, 5.5) == d
    print("--Should accurately calculate the monthly payment, the amount paid in interest, the amount paid in principle, and the total amount paid based on inputs--")