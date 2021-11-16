import pytest
import requests
import app
import json
import connexion
import flask
import responses
import unittest
import soundex
from configparser import ConfigParser

from requests_mock_flask import add_flask_app_to_mock
from app import app
app.testing = True
url = 'http://127.0.0.1:5000' # The root url of the flask app


#mock
def test_index_page():
    with app.test_client() as client:
        response = client.get(url+'/')
        assert response.status_code == 200
        print("Mock test to test see if the flask app is running")


#fake
#happy-path
def test_fake_cc_payoff_implementation():
    s = soundex.getInstance()
    dict2 = {
                "CC Balance": 1542.00,
                "CC Interest Rate": 5.2,
                "Months": 7
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json'}
    resDict = dict()
    resDict['Monthly Payment'] = 223.15
    resDict['Total Principal Paid'] = 1542.0
    resDict['Total Interest Paid'] = 20.07


    with app.test_client() as client:
            # send data as POST form to endpoint
            response = client.post(url+'/cc_payoff', data=sendJson, content_type='application/json')
            # response = client.post(
            #     url+'/cc_payoff',
            #     json=dict2,
            # )
            # check result from server with expected data
            #print(response.data)
            # print(response.data.decode('UTF-8').replace("\\",""))
            # print("k")
            # print(json.dumps(resDict))
            str2 = str(response.data.decode('UTF-8').replace("\\",""))
            assert str2[1:-1] == json.dumps(resDict)
            print("Fake test to see if proper output is displayed from CC Payoff API")
            #assert response.status_code == 200 and s.soundex(str(response.data.decode('UTF-8'))) == s.soundex(str(json.dumps(resDict)))

#mock
def test_mock_cc_payoff_connection():
    s = soundex.getInstance()
    dict2 = {
                "CC Balance": 1542.00,
                "CC Interest Rate": 5.2,
                "Months": 7
            }
    sendJson = json.dumps(dict2)
    with app.test_client() as client:
        response = client.post(url+'/cc_payoff', data=sendJson, content_type='application/json')
        assert response.status_code == 200
        print("Mock test to test the connection and response code for the CC Payoff endpoint")

#fake
#happy-path
def test_fake_simple_savings_calc_implementation():
    s = soundex.getInstance()
    dict2 = {
                "Initial Deposit": 1000,
                "Monthly Contribution": 100,
                "Time Period": 1.5,
                "Interest Rate": 10
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json'}
    resDict = dict()
    resDict['Total Savings balance'] = 3020.00   
    resDict['Total Contributions'] = 1800.0
    resDict['Interest Earned'] = 220.0


    with app.test_client() as client:
            # send data as POST form to endpoint
            response = client.post(url+'/simple_savings_calc', data=sendJson, content_type='application/json')
            # response = client.post(
            #     url+'/cc_payoff',
            #     json=dict2,
            # )
            # check result from server with expected data
            #print(response.data)
            # print(response.data.decode('UTF-8').replace("\\",""))
            # print("k")
            # print(json.dumps(resDict))
            str2 = str(response.data.decode('UTF-8').replace("\\",""))
            assert str2[1:-1] == json.dumps(resDict)
            print("Fake test to see if proper output is displayed from Simple Savings Calc API")
            #assert response.status_code == 200 and s.soundex(str(response.data.decode('UTF-8'))) == s.soundex(str(json.dumps(resDict)))

#mock
def test_mock_simple_savings_calc_connection():
    s = soundex.getInstance()
    dict2 = {
                "Initial Deposit": 1000,
                "Monthly Contribution": 100,
                "Time Period": 1.5,
                "Interest Rate": 10
            }
    sendJson = json.dumps(dict2)
    with app.test_client() as client:
        response = client.post(url+'/simple_savings_calc', data=sendJson, content_type='application/json')
        assert response.status_code == 200
        print("Mock test to test the connection and response code for the Simple Savings Calc endpoint")

#fake
#happy-path
def test_fake_cc_min_payment_calc_implementation():
    s = soundex.getInstance()
    dict2 = {
                "CC Balance": 5000,
                "CC Interest Rate": 6,
                "Minimum Payment Percent": 9
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json'}
    resDict = dict()
    resDict['Monthly Payment'] = 450.00   
    resDict['Months'] = 49
    resDict['Total Payment'] = 5289.53


    with app.test_client() as client:
            # send data as POST form to endpoint
            response = client.post(url+'/cc_min_payment_calc', data=sendJson, content_type='application/json')
            # response = client.post(
            #     url+'/cc_payoff',
            #     json=dict2,
            # )
            # check result from server with expected data
            #print(response.data)
            # print(response.data.decode('UTF-8').replace("\\",""))
            # print("k")
            # print(json.dumps(resDict))
            str2 = str(response.data.decode('UTF-8').replace("\\",""))
            assert str2[1:-1] == json.dumps(resDict)
            print("Fake test to see if proper output is displayed from CC Min Payment Calc API")
            #assert response.status_code == 200 and s.soundex(str(response.data.decode('UTF-8'))) == s.soundex(str(json.dumps(resDict)))

#mock
def test_mock_cc_min_payment_calc_connection():
    s = soundex.getInstance()
    dict2 = {
                "CC Balance": 5000,
                "CC Interest Rate": 6,
                "Minimum Payment Percent": 9
            }
    sendJson = json.dumps(dict2)
    with app.test_client() as client:
        response = client.post(url+'/cc_min_payment_calc', data=sendJson, content_type='application/json')
        assert response.status_code == 200
        print("Mock test to test the connection and response code for the CC Min Payment Calc endpoint")

#fake
#happy-path
def test_fake_mortgage_calc_implementation():
    s = soundex.getInstance()
    dict2 = {
                "Home Price": 480000,
                "Down Payment":  50,
                "Loan Length": 30,
                "Interest Rate": 10
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json'}
    resDict = dict()
    resDict['Monthly Payment'] = 2106.17
    resDict['Amount Paid in Interest'] = 518221.84
    resDict['Amount Paid in Principle'] = 240000.00
    resDict['Total Amount Paid'] = 758221.84


    with app.test_client() as client:
            # send data as POST form to endpoint
            response = client.post(url+'/mortgage_calc', data=sendJson, content_type='application/json')
            # response = client.post(
            #     url+'/cc_payoff',
            #     json=dict2,
            # )
            # check result from server with expected data
            #print(response.data)
            # print(response.data.decode('UTF-8').replace("\\",""))
            # print("k")
            # print(json.dumps(resDict))
            str2 = str(response.data.decode('UTF-8').replace("\\",""))
            assert str2[1:-1] == json.dumps(resDict)
            print("Fake test to see if proper output is displayed from Mortgage Calc API")
            #assert response.status_code == 200 and s.soundex(str(response.data.decode('UTF-8'))) == s.soundex(str(json.dumps(resDict)))

#mock
def test_mock_mortgage_calc_connection():
    s = soundex.getInstance()
    dict2 = {
                "Home Price": 480000,
                "Down Payment":  50,
                "Loan Length": 30,
                "Interest Rate": 10
            }
    sendJson = json.dumps(dict2)
    with app.test_client() as client:
        response = client.post(url+'/mortgage_calc', data=sendJson, content_type='application/json')
        assert response.status_code == 200
        print("Mock test to test the connection and response code for the Mortgage Calc endpoint")

#fake
#happy-path
def test_fake_cdCalc_implementation():
    s = soundex.getInstance()
    dict2 = {
                "Init Deposit": 2500,
                "Year Period": 3.5,
                "Interest Rate": 3.5
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json'}
    resDict = dict()
    resDict['Total Balance'] = 2819.88
    resDict['Total Interest'] = 319.88


    with app.test_client() as client:
            # send data as POST form to endpoint
            response = client.post(url+'/cdCalc', data=sendJson, content_type='application/json')
            # response = client.post(
            #     url+'/cc_payoff',
            #     json=dict2,
            # )
            # check result from server with expected data
            #print(response.data)
            # print(response.data.decode('UTF-8').replace("\\",""))
            # print("k")
            # print(json.dumps(resDict))
            str2 = str(response.data.decode('UTF-8').replace("\\",""))
            assert str2[1:-1] == json.dumps(resDict)
            print("Fake test to see if proper output is displayed from CD Calc API")
            #assert response.status_code == 200 and s.soundex(str(response.data.decode('UTF-8'))) == s.soundex(str(json.dumps(resDict)))

#mock
def test_mock_cdCalc_connection():
    s = soundex.getInstance()
    dict2 = {
                "Init Deposit": 2500,
                "Year Period": 3.5,
                "Interest Rate": 3.5
            }
    sendJson = json.dumps(dict2)
    with app.test_client() as client:
        response = client.post(url+'/cdCalc', data=sendJson, content_type='application/json')
        assert response.status_code == 200
        print("Mock test to test the connection and response code for the CD Calc endpoint")