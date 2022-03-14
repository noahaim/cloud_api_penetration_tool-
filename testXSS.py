"""
this test will check

"""
import requests
fname = "queries.txt"
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
payloads = [x.strip() for x in content]


def raw_input(param):
    pass


raw_input("URL: ")
vuln = []
for payload in payloads:
    payload = payload
    xss_url = "http://api.open-notify.org/astros.json"+payload
    r = requests.get(xss_url)
    if payload.lower() in r.text.lower():
        print("Vulnerable: " + payload)
        if payload not in vuln:
            vuln.append(payload)
    else:
        print ("Not vulnerable!")


def simple_redirect():
    response = requests.get("http://api.open-notify.org/astros.json")
    if response.status_code > 200:
        return "failed"
    return "passed"


def write_data():
    response = requests.get("http://api.open-notify.org/astros.json")
    if response.status_code < 201:
        return "failed"
    return "passed"


def delete_data():
    response = requests.get("http://api.open-notify.org/astros.json")
    if response.status_code < 201:
        return "failed"
    return "passed"
