import unittest
import requests
import logging

#Catch logs for all kinds of exceptions
logger = logging.Logger('catch_all')

#Check availability of Home-Page
def test_get_homepage(url):
    response = requests.get(url)
    try:
        assert(response.status_code==200)
    except AssertionError:
        logger.error("Failed to connect to given URL")

#Check availability of /ping
def test_get_ping(url):
    response = requests.get(url)
    try:
        assert(response.status_code==200)
    except AssertionError:
        logger.error("Failed to connect to given URL")

#Check availability of /system
def test_get_systeminfo(url):
    response = requests.get(url)
    try:
        assert(response.status_code==200)
    except AssertionError:
        logger.error("Failed to connect to given URL")


#Check availability of /mediainfo/<id>
def test_get_mediainfo(url):
    response = requests.get(url)
    try:
        assert(response.status_code==200)
    except AssertionError:
        logger.error("Failed to connect to given URL")

#Test Cases

#Test Case 1: Correct URL for home-page
print("Running Test Case 1: Correct URL for home-page")
test_get_homepage('http://127.0.0.1:5000/')

#Test Case 2: Incorrect URL for home-page
print("Running Test Case 2: Incorrect URL for home-page")
test_get_homepage('http://127.0.0.1:5000/homepage')

#Test Case 3: Correct URL for /ping
print("Running Test Case 3: Correct URL for /ping")
test_get_homepage('http://127.0.0.1:5000/ping')

#Test Case 4: Incorrect URL for /ping
print("Running Test Case 4: Incorrect URL for /ping")
test_get_homepage('http://127.0.0.1:5000/pin')

#Test Case 5: Correct URL for /system
print("Running Test Case 5: Correct URL for /system")
test_get_homepage('http://127.0.0.1:5000/system')

#Test Case 6: Incorrect URL for /system
print("Running Test Case 6: Incorrect URL for /system")
test_get_homepage('http://127.0.0.1:5000/sys')

# #Test Case 7: Correct URL for /mediainfo/<id>
print("Running Test Case 7: Correct URL for /mediainfo/<id>")
test_get_homepage('http://127.0.0.1:5000/mediainfo/11497188')

#Test Case 8: Incorrect URL for /mediainfo/<id>
print("Running Test Case 8: Inorrect URL for /mediainfo/<id>")
test_get_homepage('http://127.0.0.1:5000/mediainfo/114971')