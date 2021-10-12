import BankFunctions

def test_negative_ccBalance():
    assert BankFunctions.cc_payoff(-1000, 12, 2) == "CC balance cannot be negative."
    print("--Should reject a negative CC balance input--")

def test_negative_ccInterestRate():
    assert BankFunctions.cc_payoff(1000, -12, 2) == "CC interest rate cannot be negative."
    print("--Should reject a negative CC interest rate input--")

def test_negative_months():
    assert BankFunctions.cc_payoff(1000, 12, -2) == "Desired months to payoff cannot be negative."
    print("--Should reject a negative desired months to payoff input-- ")

def test_NaN_ccBalance():
    assert BankFunctions.cc_payoff("test", 12, 2) == "CC balance input value must be numeric."
    print("--Should reject a CC balance that is not a number--")

def test_NaN_ccInterestRate():
    assert BankFunctions.cc_payoff(1, "test", 2) == "CC interest rate input value must be numeric."
    print("--Should reject a CC interest rate that is not a number--")

def test_NaN_months():
    assert BankFunctions.cc_payoff(1, 12, "test") == "Desired months to payoff input value must be numeric."
    print("--Should reject a desired months to payoff that is not a number--")

# Website used as reference https://www.bankrate.com/calculators/credit-cards/credit-card-payoff-calculator.aspx returns output as integer but doc said to output to 2 decimal places so output on reference is not exactly equal to output from program
def test_integer_calculation():
    d = dict()
    d['Monthly Payment'] = 223.15
    d['Total Principal Paid'] = 1542.00
    d['Total Interest Paid'] = 20.07
    assert BankFunctions.cc_payoff(1542.00, 5.2, 7) == d
    print("--Should accurately calculate the monthly payment, the total principal paid, and the total interest paid based on inputs--")