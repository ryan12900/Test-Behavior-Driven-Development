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