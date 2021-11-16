import pytest
import requests
import app
import json

url = 'http://127.0.0.1:5000' # The root url of the flask app

def test_index_page():
    r = requests.get(url+'/')
    assert r.status_code == 200 
    print("Test to see if the flask app is running")

def test_cc_payoff():
    dict2 = {
                "CC Balance": 1542.00,
                "CC Interest Rate": 5.2,
                "Months": 7
            }
    response = requests.post(url+'/cc_payoff', json=dict2)
    resDict = dict()
    resDict['Monthly Payment'] = 223.15
    resDict['Total Principal Paid'] = 1542.0
    resDict['Total Interest Paid'] = 20.07
    assert response.status_code == 200 and response.json() == json.dumps(resDict)
    print("Test to see if CC Payoff API is working properly and returns correct response")

def test_simple_savings_calc():
    dict2 = {
                "Initial Deposit": 1000,
                "Monthly Contribution": 100,
                "Time Period": 1.5,
                "Interest Rate": 10
            }
    response = requests.post(url+'/simple_savings_calc', json=dict2)
    resDict = dict()
    resDict['Total Savings balance'] = 3020.00   
    resDict['Total Contributions'] = 1800.0
    resDict['Interest Earned'] = 220.0
    assert response.status_code == 200 and response.json() == json.dumps(resDict)
    print("Test to see if Simple Savings Calc API is working properly and returns correct response")

def test_cc_min_payment_calc():
    dict2 = {
                "CC Balance": 5000,
                "CC Interest Rate": 6,
                "Minimum Payment Percent": 9
            }
    response = requests.post(url+'/cc_min_payment_calc', json=dict2)
    resDict = dict()
    resDict['Monthly Payment'] = 450.00   
    resDict['Months'] = 49
    resDict['Total Payment'] = 5289.53
    assert response.status_code == 200 and response.json() == json.dumps(resDict)
    print("Test to see if CC Min Payment Calc API is working properly and returns correct response")


def test_mortgage_calc():
    dict2 = {
                "Home Price": 480000,
                "Down Payment":  50,
                "Loan Length": 30,
                "Interest Rate": 10
            }
    response = requests.post(url+'/mortgage_calc', json=dict2)
    resDict = dict()
    resDict['Monthly Payment'] = 2106.17
    resDict['Amount Paid in Interest'] = 518221.84
    resDict['Amount Paid in Principle'] = 240000.00
    resDict['Total Amount Paid'] = 758221.84
    assert response.status_code == 200 and response.json() == json.dumps(resDict)
    print("Test to see if Mortgage Calculator API is working properly and returns correct response")

def test_cdCalc():
    dict2 = {
                "Init Deposit": 2500,
                "Year Period": 3.5,
                "Interest Rate": 3.5
            }
    response = requests.post(url+'/cdCalc', json=dict2)
    resDict = dict()
    resDict['Total Balance'] = 2819.88
    resDict['Total Interest'] = 319.88
    
    assert response.status_code == 200 and response.json() == json.dumps(resDict)
    print("Test to see if CD Calculator API is working properly and returns correct response")
