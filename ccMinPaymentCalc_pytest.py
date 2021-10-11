import BankFunctions

def test_negative_ccBalance():
    assert BankFunctions.ccMinPaymentCalc(-1, 12, 2) == "CC balance cannot be negative."
    print("--Should reject a negative CC balance input--")

def test_negative_ccInterestRate():
    assert BankFunctions.ccMinPaymentCalc(1, -12, 2) == "CC interest rate cannot be negative."
    print("--Should reject a negative CC interest rate input--")

def test_negative_minPaymentPercent():
    assert BankFunctions.ccMinPaymentCalc(1, 12, -2) == "Minimum payment percent cannot be negative."
    print("--Should reject a negative minimum payment percent input-- ")

def test_NaN_ccBalance():
    assert BankFunctions.ccMinPaymentCalc("test", 12, 2) == "CC balance input value must be numeric."
    print("--Should reject a CC balance that is not a number--")

def test_NaN_ccInterestRate():
    assert BankFunctions.ccMinPaymentCalc(1, "test", 2) == "CC interest rate input value must be numeric."
    print("--Should reject a CC interest rate that is not a number--")

def test_NaN_minPaymentPercent():
    assert BankFunctions.ccMinPaymentCalc(1, 12, "test") == "Minimum payment percent input value must be numeric."
    print("--Should reject a minimum payment percent that is not a number--")

#Website used as a reference https://www.bankrate.com/calculators/credit-cards/credit-card-minimum-payment.aspx does not allow minimument payment percents greater than 20%
def test_invalid_minPaymentPercent():
    assert BankFunctions.ccMinPaymentCalc(1, 12, 20.01) == "Minimum payment percent input value should not be greater than 20%."
    print("--Should reject a minimum payment percent that is greater than 20%--")

def test_integer_calculation1():
    d = dict()
    d['Monthly Payment'] = 450.00   
    d['Months'] = 49
    d['Total Payment'] = 5289.53
    assert BankFunctions.ccMinPaymentCalc(5000,6,9) == d
    print("--Should accurately calculate the monthly payment, the number of months, and the total payment based on inputs--")

def test_integer_calculation2():
    d = dict()
    d['Monthly Payment'] = 151.85  
    d['Months'] = 27
    d['Total Payment'] = 1341.72
    assert BankFunctions.ccMinPaymentCalc(1234.56, 12.3, 12.3) == d
    print("--Should accurately calculate the monthly payment, the number of months, and the total payment based on inputs--")

def test_integer_calculation3():
    d = dict()
    d['Monthly Payment'] = 30.37       
    d['Months'] = 12
    d['Total Payment'] = 221.25
    assert BankFunctions.ccMinPaymentCalc(206.6, 14.7, 14.7) == d
    print("--Should accurately calculate the monthly payment, the number of months, and the total payment based on inputs--")