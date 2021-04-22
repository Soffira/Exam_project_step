import pytest, 
# import os
import requests
import logging


# @pytest.fixture
# def logger():
# logger = logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
mylogger = logging.getLogger()
    # return logger

def test_data_users():
    r = requests.get('http://127.0.0.1:8080/api/users')
    if r.text == "data: [{'username': 'van', 'email': 'vanbyvan@fmail.ru', 'department': 'production', 'date_joined': '2011-11-11T11:10:09'}, \
        {'username': 'billy', 'email ': 'billyjeans@fmail.ru', 'department': 'pr', 'date_joined': '1983-03-02T12:12:53'},  \
        {'username': 'max', 'email ': 'maximus@fmail.ru', 'department': 'production', 'date_joined': '1999-05-29T14:14:28'},  \
        {'username': 'leonard', 'email ': 'leokapri@fmail.ru', 'department': 'sales', 'date_joined': '1974-12-11T14:45:32'}]":
        mylogger.info('Test 1 is Passed')
    else:
        mylogger.info('Test 1 is Failed')
    assert r.text == "data: [{'username': 'van', 'email': 'vanbyvan@fmail.ru', 'department': 'production', 'date_joined': '2011-11-11T11:10:09'}, \
        {'username': 'billy', 'email': 'billyjeans@fmail.ru', 'department': 'pr', 'date_joined': '1983-03-02T12:12:53'}, \
        {'username': 'max', 'email': 'maximus@fmail.ru', 'department': 'production', 'date_joined': '1999-05-29T14:14:28'}, \
        {'username': 'leonard', 'email': 'leokapri@fmail.ru', 'department': 'sales', 'date_joined': '1974-12-11T14:45:32'}]"

def test_data_deps():
    r = requests.get('http://127.0.0.1:8080/api/department')
    if 'production' in r.text and 'pr' in r.text and 'sales' in r.text:
        mylogger.info('Test 2 is Passed')
    else:
        mylogger.info('Test 2 is Failed')
    assert 'production' in r.text and 'pr' in r.text and 'sales' in r.text

# if __name__ == '__main__':
#     mylogger.info(' Tests start ')
#     pytest.main(args=[os.path.abspath(__file__)])
#     mylogger.info(' Done executing the tests ')
