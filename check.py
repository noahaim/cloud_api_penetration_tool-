import datetime

from run_class import Run

if __name__ == '__main__':

    data=[{'endpoin port': 'https://github.com/noahaim/cloud_api_penetration_tool-', 'endpoint URL': 'https://www.youtube.com/watch?v=PTgfNfVe2OE&list=PLzXWAguR6f9z7nVObza7gkhva4ieHIQf1&index=4&t=14s', 'github link': 'https://github.com/noahaim/cloud_api_penetration_tool-', 'runs': [{'date': '1/6/2022', 'time': '21:21'}], 'tests': ['Dos', 'XSS']}, {'endpoin port': 'https://github.com/noahaim/cloud_api_penetration_tool-', 'endpoint URL': 'https://www.youtube.com/watch?v=PTgfNfVe2OE&list=PLzXWAguR6f9z7nVObza7gkhva4ieHIQf1&index=4&t=14s', 'github link': 'https://github.com/noahaim/cloud_api_penetration_tool-', 'runs': [{'date': '1/6/2022', 'time': '21:29'}], 'tests': ['Bruteforce', 'Dos', 'XSS', 'JSON injection']}, {'endpoin port': 'https://github.com/noahaim/cloud_api_penetration_tool-', 'endpoint URL': 'https://www.youtube.com/watch?v=PTgfNfVe2OE&list=PLzXWAguR6f9z7nVObza7gkhva4ieHIQf1&index=4&t=14s', 'github link': 'https://github.com/noahaim/cloud_api_penetration_tool-', 'runs': [{'date': '1/6/2022', 'time': '21:58'}], 'tests': ['Dos']}, {'endpoin port': 'https://github.com/noahaim/cloud_api_penetration_tool-', 'endpoint URL': 'https://www.youtube.com/watch?v=PTgfNfVe2OE&list=PLzXWAguR6f9z7nVObza7gkhva4ieHIQf1&index=4&t=14s', 'github link': 'https://github.com/noahaim/cloud_api_penetration_tool-', 'runs': [{'date': '1/6/2022', 'time': '22:0'}], 'tests': ['XSS']}, {'endpoin port': 'https://github.com/noahaim/cloud_api_penetration_tool-', 'endpoint URL': 'http://127.0.0.1:5000/addNewAPI', 'github link': 'https://github.com/noahaim/cloud_api_penetration_tool-', 'runs': [{'date': '1/6/2022', 'time': '22:2'}], 'tests': ['JSON injection']}]
    for item in data:
        print(">>>>>>>")
        for i in item:
            print(i+str(":    ")+str(item[i]))
