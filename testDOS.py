"""
This test will preform a deniel of serveice attack by sending a big ammount of API request to the
clusters. types of tests:
1. DOS of the same query
2. different queries
3. spoofed IP with each query (DDOS)

the test will expect a block after some amount of time
in addition, response latancy will be recorded and analysed to determine the durability
of the API with such attacks

"""
import random
import socket
import requests


def genIP():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip


def testDOS(spoofIP=False, randomQueries=False):
    ipaddr = socket.gethostbyname(socket.gethostname())
    file1 = open('queries.txt', 'r')
    query_list = file1.readlines()
    query = random.choice(query_list)
    for i in range(5000):
        if spoofIP:
            ipaddr = genIP()

        if randomQueries:
            query = random.choice(query_list)

        # send API query to cluster with given IP and Query


response = requests.get("http://api.open-notify.org/astros.json")
print(response)
