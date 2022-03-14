"""
This test will preform an authentication abuse on API loggin queries and will test the
responses of the cluster to it. the bruteforce will send authentication queries with
different login credentials:
1. serial
2.random
3.special

the test will expect for a block

"""
import requests


def simple_brtfrc():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response)


def dict():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response)


def rand():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response)
