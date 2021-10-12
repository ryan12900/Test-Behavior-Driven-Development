import BankFunctions

def test_negative_initial_deposit():
    assert BankFunctions.simple_savings_calc(-1000, 100, 2, 10) == "Initial deposit cannot be negative."
    print("--Should reject a negative Initial deposit input--")

def test_negative_monthly_contrib():
    assert BankFunctions.simple_savings_calc(1000, -100, 2, 10) == "Monthly contribution cannot be negative."
    print("--Should reject a negative monthly contribution input--")

def test_negative_time_period():
    assert BankFunctions.simple_savings_calc(1000, 100, -2, 10) == "Time period cannot be negative."
    print("--Should reject a negative time period input-- ")

def test_negative_interest_rate():
    assert BankFunctions.simple_savings_calc(1000, 100, 2, -10) == "Interest rate cannot be negative."
    print("--Should reject a negative Interest rate input--")

def test_nan_initial_deposit():
    assert BankFunctions.simple_savings_calc("test", 100, 2, 10) == "Initial deposit value must be numeric."
    print("--Should reject an initial deposit that is not a number--")

def test_nan_monthly_contrib():
    assert BankFunctions.simple_savings_calc(1000, "test", 2, 10) == "Monthly contribution value must be numeric."
    print("--Should reject a monthly contribution that is not a number--")

def test_nan_time_period():
    assert BankFunctions.simple_savings_calc(1000, 100, "test", 10) == "Time period must be numeric, and in year form. e.g: 2.5 (years)"
    print("--Should reject a time period that is not a number--")

def test_nan_interest_rate():
    assert BankFunctions.simple_savings_calc(1000, 100, 2, "test") == "Interest rate value must be numeric."
    print("--Should reject an interest rate that is not a number--")

#Website used as a reference https://www.bankrate.com/calculators/savings/simple-savings-calculator.aspx
#APY implemented as described in project documentation

def test_calculation1():
    d = dict()
    d['Total Savings balance'] = 3020.00   
    d['Total Contributions'] = 1800
    d['Interest Earned'] = 220.0
    assert BankFunctions.simple_savings_calc(1000,100,1.5,10) == d
    print("--should correctly output savings total, total contributions, and interest accumulated based on real calculations--")

def test_calculation2():
    d = dict()
    d['Total Savings balance'] = 4582.00 
    d['Total Contributions'] = 3000.00
    d['Interest Earned'] = 582.00
    assert BankFunctions.simple_savings_calc(1000,100,2.5,10) == d
    print("--should correctly output savings total, total contributions, and interest accumulated based on real calculations--")

def test_calculation3():
    d = dict()
    d['Total Savings balance'] = 6804.00  
    d['Total Contributions'] = 1200.00
    d['Interest Earned'] = 604.00
    assert BankFunctions.simple_savings_calc(5000,50,2,5) == d
    print("--should correctly output savings total, total contributions, and interest accumulated based on real calculations--")
    
def test_calculation4():
    d = dict()
    d['Total Savings balance'] = 4014.69  
    d['Total Contributions'] = 2400.00
    d['Interest Earned'] = 613.69
    assert BankFunctions.simple_savings_calc(1001,100,2,10.52) == d
    print("--should correctly output savings total, total contributions, and interest accumulated based on real calculations--")