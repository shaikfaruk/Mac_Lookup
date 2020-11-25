# Mac_Lookup
### A containerized application, which takes the MAC address as input from the command line and queries the https://macaddress.io/ MAC address lookup API and gets the company name associated with it.
# Requirements
1. **Docker**  
If you don't have docker, follow the steps in this link https://docs.docker.com/engine/install/ubuntu/ to install docker.  
2. **Git**  
Follow to below steps to install Git in your linux machine.  
`sudo apt update`  
`sudo apt install git`  
# How to use..  
1. **Clone it from github**  
Run the following command in your terminal to clone it.  
`git clone https://github.com/shaikfaruk/Mac_Lookup.git`  
2. **Build the docker image**  
Follow the below commands to build the docker image.  
`cd Mac_Lookup/`  
`docker build . -t mac_lookup`  
3. **Run the container**  
Run command:  
`docker run -it mac_lookup -mac <mac_address> -apikey <api_key_value>`  
apikey is optional.  
Example:
`docker run -it mac_lookup -mac 00:00:48:00:00:ad`  
Below command runs the container with help argument, which says what are things are need to be passed as input.  
`docker run -it mac_lookup -h`  
```  
root@shasd:/home/shasd/Mac_Lookup# docker run -it mac_lookup -h  
usage: rest_api.py [-h] [-mac MAC] [-apikey APIKEY]  
Take MAC Address as input, API Key as well if required  
optional arguments:  
  -h, --help      show this help message and exit  
  -mac MAC        Please provide a valid MAC address  
  -apikey APIKEY  Please provide a valid API Key  
  ```  
 # About this application.  
 * It checks for **HTTP Error**, **Connection Error**, and **Timeout Error**.  
 * It checks for whether the entered MAC address is of proper format.  
 * It checks whether the MAC address is present in the database of https://macaddress.io/.  
##### **shasd@cisco.com**
