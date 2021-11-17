import pytest
import requests
import app
import json
import flask
import responses
import unittest
import soundex
from configparser import ConfigParser

from requests_mock_flask import add_flask_app_to_mock
from app import app
app.testing = True
url = 'http://127.0.0.1:5000' # The root url of the flask app
apiKey = '3d065b67-f166-4630-b1c9-cb5fff86ab30'

#These initial tests are the unit tests and test doubles for the http responses for each endpoint.
#All of the functions are tested for, as well as the API revoke endpoint and the API get endpoint.


#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_index_page():
    with app.test_client() as client:
        response = client.get(url+'/')
        assert response.status_code == 200
        print("Mock test to test see if the flask app is running")


#The reason for creating a fake test double was to ensure the properly functionality of the Bank Functions themselves, by creating fake
#data and replicating a fake POST request, we are able to simulate the expected functionality of each of the functions, and evaluate the 
#expected output.
#fake
#happy-path
#This happy path test case demonstrates what an ideal test case and result would be, with the expected input and output that one would
#expect in a normal and properly functioning use case.
def test_fake_cc_payoff_implementation():
    s = soundex.getInstance()
    dict2 = {
                "CC Balance": 1542.00,
                "CC Interest Rate": 5.2,
                "Months": 7
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    resDict = dict()
    resDict['Monthly Payment'] = 223.15
    resDict['Total Principal Paid'] = 1542.0
    resDict['Total Interest Paid'] = 20.07


    with app.test_client() as client:
            # send data as POST form to endpoint
            response = client.post(url+'/cc_payoff', data=sendJson, content_type='application/json', headers=headers)
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

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_mock_cc_payoff_connection():
    s = soundex.getInstance()
    dict2 = {
                "CC Balance": 1542.00,
                "CC Interest Rate": 5.2,
                "Months": 7
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    with app.test_client() as client:
        response = client.post(url+'/cc_payoff',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 200
        print("Mock test to test the connection and response code for the CC Payoff endpoint")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_cc_payoff_invalid_request():
    s = soundex.getInstance()
    dict2 = {
                "CC Balance": 1542.00,
                "CC Interest Rate": 5.2,
                "Months": 7
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    with app.test_client() as client:
        response = client.put(url+'/cc_payoff',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 405
        print("Mock test invalid request for CC Payoff")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_cc_payoff_no_key():
    s = soundex.getInstance()
    dict2 = {
                "CC Balance": 1542.00,
                "CC Interest Rate": 5.2,
                "Months": 7
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json'}
    with app.test_client() as client:
        try:
            response = client.post(url+'/cc_payoff',  data=sendJson, content_type='application/json', headers=headers)
            assert False
        except KeyError:
            assert True
        print("Mock test no API key for CC Payoff")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_cc_payoff_invalid_key():
    s = soundex.getInstance()
    dict2 = {
                "CC Balance": 1542.00,
                "CC Interest Rate": 5.2,
                "Months": 7
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json', 'apiKey': 'invalid'}
    with app.test_client() as client:
        response = client.post(url+'/cc_payoff',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 401
        print("Mock test invalid API key for CC Payoff")

#The reason for creating a fake test double was to ensure the properly functionality of the Bank Functions themselves, by creating fake
#data and replicating a fake POST request, we are able to simulate the expected functionality of each of the functions, and evaluate the 
#expected output.
#This happy path test case demonstrates what an ideal test case and result would be, with the expected input and output that one would
#expect in a normal and properly functioning use case.
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
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    resDict = dict()
    resDict['Total Savings balance'] = 3020.00   
    resDict['Total Contributions'] = 1800.0
    resDict['Interest Earned'] = 220.0


    with app.test_client() as client:
            # send data as POST form to endpoint
            response = client.post(url+'/simple_savings_calc',  data=sendJson, content_type='application/json', headers=headers)
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

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_mock_simple_savings_calc_connection():
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    s = soundex.getInstance()
    dict2 = {
                "Initial Deposit": 1000,
                "Monthly Contribution": 100,
                "Time Period": 1.5,
                "Interest Rate": 10
            }
    sendJson = json.dumps(dict2)
    with app.test_client() as client:
        response = client.post(url+'/simple_savings_calc',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 200
        print("Mock test to test the connection and response code for the Simple Savings Calc endpoint")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_simple_savings_calc_invalid_request():
    s = soundex.getInstance()
    dict2 = {
                "Initial Deposit": 1000,
                "Monthly Contribution": 100,
                "Time Period": 1.5,
                "Interest Rate": 10
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    with app.test_client() as client:
        response = client.put(url+'/simple_savings_calc',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 405
        print("Mock test invalid request for Simple Savings Calc")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_simple_savings_calc_no_key():
    s = soundex.getInstance()
    dict2 = {
                "Initial Deposit": 1000,
                "Monthly Contribution": 100,
                "Time Period": 1.5,
                "Interest Rate": 10
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json'}
    with app.test_client() as client:
        try:
            response = client.post(url+'/simple_savings_calc',  data=sendJson, content_type='application/json', headers=headers)
            assert False
        except KeyError:
            assert True
        print("Mock test no API key for Simple Savings Calc")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_simple_savings_calc_invalid_key():
    s = soundex.getInstance()
    dict2 = {
                "Initial Deposit": 1000,
                "Monthly Contribution": 100,
                "Time Period": 1.5,
                "Interest Rate": 10
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json', 'apiKey': 'invalid'}
    with app.test_client() as client:
        response = client.post(url+'/simple_savings_calc',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 401
        print("Mock test invalid API key for Simple Savings Calc")

#The reason for creating a fake test double was to ensure the properly functionality of the Bank Functions themselves, by creating fake
#data and replicating a fake POST request, we are able to simulate the expected functionality of each of the functions, and evaluate the 
#expected output.
#This happy path test case demonstrates what an ideal test case and result would be, with the expected input and output that one would
#expect in a normal and properly functioning use case.
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
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    resDict = dict()
    resDict['Monthly Payment'] = 450.00   
    resDict['Months'] = 49
    resDict['Total Payment'] = 5289.53


    with app.test_client() as client:
            # send data as POST form to endpoint
            response = client.post(url+'/cc_min_payment_calc',  data=sendJson, content_type='application/json', headers=headers)
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

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_mock_cc_min_payment_calc_connection():
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    s = soundex.getInstance()
    dict2 = {
                "CC Balance": 5000,
                "CC Interest Rate": 6,
                "Minimum Payment Percent": 9
            }
    sendJson = json.dumps(dict2)
    with app.test_client() as client:
        response = client.post(url+'/cc_min_payment_calc',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 200
        print("Mock test to test the connection and response code for the CC Min Payment Calc endpoint")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_cc_min_payment_calc_invalid_request():
    s = soundex.getInstance()
    dict2 = {
                "CC Balance": 5000,
                "CC Interest Rate": 6,
                "Minimum Payment Percent": 9
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    with app.test_client() as client:
        response = client.put(url+'/cc_min_payment_calc',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 405
        print("Mock test invalid request for CC Min Payment Calc")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_cc_min_payment_calc_no_key():
    s = soundex.getInstance()
    dict2 = {
                "CC Balance": 5000,
                "CC Interest Rate": 6,
                "Minimum Payment Percent": 9
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json'}
    with app.test_client() as client:
        try:
            response = client.post(url+'/cc_min_payment_calc',  data=sendJson, content_type='application/json', headers=headers)
            assert False
        except KeyError:
            assert True
        print("Mock test no API key for CC Min Payment Calc")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_cc_min_payment_calc_invalid_key():
    s = soundex.getInstance()
    dict2 = {
                "CC Balance": 5000,
                "CC Interest Rate": 6,
                "Minimum Payment Percent": 9
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json', 'apiKey': 'invalid'}
    with app.test_client() as client:
        response = client.post(url+'/cc_min_payment_calc',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 401
        print("Mock test invalid API key for CC Min Payment Calc")

#The reason for creating a fake test double was to ensure the properly functionality of the Bank Functions themselves, by creating fake
#data and replicating a fake POST request, we are able to simulate the expected functionality of each of the functions, and evaluate the 
#expected output.
#This happy path test case demonstrates what an ideal test case and result would be, with the expected input and output that one would
#expect in a normal and properly functioning use case.
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
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    resDict = dict()
    resDict['Monthly Payment'] = 2106.17
    resDict['Amount Paid in Interest'] = 518221.84
    resDict['Amount Paid in Principle'] = 240000.00
    resDict['Total Amount Paid'] = 758221.84


    with app.test_client() as client:
            # send data as POST form to endpoint
            response = client.post(url+'/mortgage_calc',  data=sendJson, content_type='application/json', headers=headers)
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

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_mock_mortgage_calc_connection():
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    s = soundex.getInstance()
    dict2 = {
                "Home Price": 480000,
                "Down Payment":  50,
                "Loan Length": 30,
                "Interest Rate": 10
            }
    sendJson = json.dumps(dict2)
    with app.test_client() as client:
        response = client.post(url+'/mortgage_calc',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 200
        print("Mock test to test the connection and response code for the Mortgage Calc endpoint")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_mortgage_calc_invalid_request():
    s = soundex.getInstance()
    dict2 = {
                "Home Price": 480000,
                "Down Payment":  50,
                "Loan Length": 30,
                "Interest Rate": 10
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    with app.test_client() as client:
        response = client.put(url+'/mortgage_calc',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 405
        print("Mock test invalid request for Mortgage Calc")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_mortgage_calc_no_key():
    s = soundex.getInstance()
    dict2 = {
                "Home Price": 480000,
                "Down Payment":  50,
                "Loan Length": 30,
                "Interest Rate": 10
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json'}
    with app.test_client() as client:
        try:
            response = client.post(url+'/mortgage_calc',  data=sendJson, content_type='application/json', headers=headers)
            assert False
        except KeyError:
            assert True
        print("Mock test no API key for Mortgage Calc")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_mortgage_calc_invalid_key():
    s = soundex.getInstance()
    dict2 = {
                "Home Price": 480000,
                "Down Payment":  50,
                "Loan Length": 30,
                "Interest Rate": 10
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json', 'apiKey': 'invalid'}
    with app.test_client() as client:
        response = client.post(url+'/mortgage_calc',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 401
        print("Mock test invalid API key for Mortgage Calc")

#The reason for creating a fake test double was to ensure the properly functionality of the Bank Functions themselves, by creating fake
#data and replicating a fake POST request, we are able to simulate the expected functionality of each of the functions, and evaluate the 
#expected output.
#This happy path test case demonstrates what an ideal test case and result would be, with the expected input and output that one would
#expect in a normal and properly functioning use case.
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
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    resDict = dict()
    resDict['Total Balance'] = 2819.88
    resDict['Total Interest'] = 319.88


    with app.test_client() as client:
            # send data as POST form to endpoint
            response = client.post(url+'/cdCalc',  data=sendJson, content_type='application/json', headers=headers)
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

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_mock_cdCalc_connection():
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    s = soundex.getInstance()
    dict2 = {
                "Init Deposit": 2500,
                "Year Period": 3.5,
                "Interest Rate": 3.5
            }
    sendJson = json.dumps(dict2)
    with app.test_client() as client:
        response = client.post(url+'/cdCalc',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 200
        print("Mock test to test the connection and response code for the CD Calc endpoint")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_cdCalc_invalid_request():
    s = soundex.getInstance()
    dict2 = {
                "Init Deposit": 2500,
                "Year Period": 3.5,
                "Interest Rate": 3.5
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json', 'apiKey': apiKey}
    with app.test_client() as client:
        response = client.put(url+'/cdCalc',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 405
        print("Mock test invalid request for CD Calc")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_cdCalc_no_key():
    s = soundex.getInstance()
    dict2 = {
                "Init Deposit": 2500,
                "Year Period": 3.5,
                "Interest Rate": 3.5
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json'}
    with app.test_client() as client:
        try:
            response = client.post(url+'/cdCalc',  data=sendJson, content_type='application/json', headers=headers)
            assert False
        except KeyError:
            assert True
        print("Mock test no API key for CD Calc")

#The reason for creating a mock was to ensure the correct code implementation for HTTP requests was done properly and to ensure
#that the test did not rely on an existing connection, and would be able to be run on a mock connection.
#mock
def test_cdCalc_invalid_key():
    s = soundex.getInstance()
    dict2 = {
                "Init Deposit": 2500,
                "Year Period": 3.5,
                "Interest Rate": 3.5
            }
    sendJson = json.dumps(dict2)
    headers = {'Content-type': 'application/json', 'apiKey': 'invalid'}
    with app.test_client() as client:
        response = client.post(url+'/cdCalc',  data=sendJson, content_type='application/json', headers=headers)
        assert response.status_code == 401
        print("Mock test invalid API key for CD Calc")

# mock
def test_api_key_and_revoke_key():
    s = soundex.getInstance()
    dict2 = {
                'orgName': 'name',
                'industry': 'industry',
                'fullName': 'bing bong',
                'email': 'email',
                'ip': '127.0.0.1'
            }
    sendJson = json.dumps(dict2)
    with app.test_client() as client:
        response = client.post(url+'/getApiKey', data=sendJson, content_type='application/json')
        assert response.status_code == 200
        key = str(response.data.decode('UTF-8').replace("\\",""))
        dict3 = { 'apiKey': key }
        sendJson2 = json.dumps(dict3)
        revokeResponse = client.post(url+'/revoke', data=sendJson2, content_type='application/json')
        assert revokeResponse.status_code == 200
        print("Mock test API Key generation and revoke")

