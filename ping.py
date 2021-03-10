import os

ip_list = ["8.8.8.8","8.8.4.4","34.75.65.39","34.72.35.23"]

for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"UP {ip} ping Successful")
    else:
        print(f"Down {ip} ping Unsuccessful")