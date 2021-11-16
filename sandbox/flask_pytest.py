import pytest
import requests
import app
<<<<<<< HEAD
import json
=======
>>>>>>> 7402c25e4192f4a55c7a435c33cdba835d4375d6

url = 'http://127.0.0.1:5000' # The root url of the flask app

def test_index_page():
    r = requests.get(url+'/')
    assert r.status_code == 200 
    print("Test to see if the flask app is running")

def test_cc_payoff():
<<<<<<< HEAD
    dict2 = {
=======
    dict = {
>>>>>>> 7402c25e4192f4a55c7a435c33cdba835d4375d6
                "CC Balance": 1542.00,
                "CC Interest Rate": 5.2,
                "Months": 7
            }
<<<<<<< HEAD
    response = requests.post(url+'/cc_payoff', json=dict2)
    resDict = dict()
    resDict['Monthly Payment'] = 223.15
    resDict['Total Principal Paid'] = 1542.0
    resDict['Total Interest Paid'] = 20.07
    assert response.status_code == 200 and response.json() == json.dumps(resDict)
=======
    response = requests.post(url+'/cc_payoff', json=dict)
    assert response.status_code == 200 and response.json() == "{\"Total Principal Paid\": 1542.0, \"Monthly Payment\": 223.15, \"Total Interest Paid\": 20.07}"
>>>>>>> 7402c25e4192f4a55c7a435c33cdba835d4375d6
    print("Test to see if CC Payoff API is working properly and returns correct response")