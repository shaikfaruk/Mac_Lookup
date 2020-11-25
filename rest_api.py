import argparse
import re
import requests
import sys
import json
parser = argparse.ArgumentParser()

parser.add_argument("-mac", type=str, action="store", dest="mac", help="Enter a valid MAC address")
parser.add_argument("-apikey", type=str, action="store", dest="apikey", default='at_5KCCwxRxbucCOKt2M4WyLX9KRzAdK', help="Enter a valid API Key")

results = parser.parse_args()
mac = results.mac
api_key = results.apikey
url = "https://api.macaddress.io/v1?apiKey="+api_key+"&output=json&search="
regex = re.search("^[a-fA-F0-9:]{17}|[a-fA-F0-9]{12}$", mac)
if (regex):
    url = url+mac
else:
    print("Please enter a proper MAC address!!!")
    sys.exit()  
payload = {}
headers= {}
try:
    response = requests.get( url, headers=headers, data = payload,timeout = 4)    
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print ("Http Error!, Status code: ",response.status_code)
    sys.exit()
except requests.exceptions.ConnectionError:
    print ("Connection Error..!!")
    sys.exit()
except requests.exceptions.Timeout:
    print ("Timeout Error..!!")
    sys.exit()
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else : ",err)
    sys.exit()
res = json.loads(response.text.encode('utf8'))
if (res["vendorDetails"]["companyName"] == ""):
    print("Sorry can't find the commany name, Please check the MAC address..!")
else:
    print("Company Name: ", res["vendorDetails"]["companyName"])
