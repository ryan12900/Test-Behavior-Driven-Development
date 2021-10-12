import BankFunctions

def test_negative_initDeposit():
    assert BankFunctions.cdCalc(-100, 2.5, 2) == "Initial deposit cannot be negative."
    print("--Should reject a negative initial deposit input--")

def test_negative_yearPeriod():
    assert BankFunctions.cdCalc(1000, -2.5, 2) == "Period in years cannot be negative."
    print("--Should reject a negative period in years input--")

def test_negative_interestRates():
    assert BankFunctions.cdCalc(1000, 2.5, -2) == "Interest rate cannot be negative."
    print("--Should reject a negative interest rate input-- ")

def test_NaN_initDeposit():
    assert BankFunctions.cdCalc("test", 2.5, 2) == "Initial deposit input value must be numeric."
    print("--Should reject a initial deposit input that is not a number--")

def test_NaN_yearPeriod():
    assert BankFunctions.cdCalc(1000, "test", 2) == "Period in years input value must be numeric."
    print("--Should reject a period in years input that is not a number--")

def test_NaN_interestRates():
    assert BankFunctions.cdCalc(1000, 2.5, "test") == "Interest rate input value must be numeric."
    print("--Should reject a interest rate input that is not a number--")

def test_calc1():
    d = dict()
    d['Total Balance'] = 1269.06 
    d['Total Interest'] = 269.06
    assert BankFunctions.cdCalc(1000,2.5,10) == d
    print("--Should accurately calculate the total balance and total interest based on inputs--")

def test_calc2():
    d = dict()
    d['Total Balance'] = 2819.88
    d['Total Interest'] = 319.88
    assert BankFunctions.cdCalc(2500,3.5,3.5) == d
    print("--Should accurately calculate the total balance and total interest based on inputs--")

def test_calc3():
    d = dict()
    d['Total Balance'] = 6600.15 
    d['Total Interest'] = 1550.15
    assert BankFunctions.cdCalc(5050,5,5.5) == d
    print("--Should accurately calculate the total balance and total interest based on inputs--")

def test_calc4():
    d = dict()
    d['Total Balance'] = 1121.50 
    d['Total Interest'] = 121.50
    assert BankFunctions.cdCalc(1000,3.4,3.5) == d
    print("--Should accurately calculate the total balance and total interest based on inputs--")