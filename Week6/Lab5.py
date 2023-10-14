# Lab4
# Author: Frank R. Leotta III

"""_summary_
This lab is designed to get you familiar with Python virtual environments as well as import statments to use external libraries.
# I have added additional code to make it look more readable for myself in the future
"""

# 1. Create a virtual environment called "venv" in the current directory. (#Python3 -m venv venv)
#python3 -m venv venv
# 2. Activate the virtual environment. (#venv\Scripts\activate) Note: its \ not /                                                                                                                                                                                                                                                                                                                                                                                                          te)
#source venv/bin/activate
""" now type it into vs coders terminal"""
# 3. Install the requests library. (#pip install requests) 
""" at this point you youse vs coder, don"t use windows powershell... do not try running in python"""
#pip install requests

""" also pip3 install requests for older versions of python
# install requests[socks]  if you want to use socks no idea what that is, but it's in the instructions if if i need foot coverings for my code /s """

print("space purposefully left blank below to help scroll down in program\n\n\n\n\n\n\n\n\n\n\n\n\n ")
# 4. import requests library here #(import requests)
import requests  #got an error in the terminal and in python, but it still worked.... odd

"""# #from requests import *  is another way to do it
## I think it's because I already installed it in the terminal, so it's already there"""
#
"""# #from requests import get    is another way to do it
# # if you want to  rename it, do this
# import requests as rq 
 then you can use rq.get() instead of requests.get()"""

# 5. Use the requests library to make a GET request to https://api.github.com/events
our_requests = requests.get("https://api.github.com/events")
print(our_requests) #<Response [200]> 200 means it worked, it was sucessful

# 6. Print out the status code of the response.
print("status code below, print get.status_code above this line")
print(our_requests.status_code)
# 7. Print out the content of the response.
print("content below... massive wall of text due to it being an object")
print(our_requests.content)
print("\n\n\n")
# 8. Print out the headers of the response.
print("headers below, content above this line\n")
print(our_requests.headers)
# 9. Deactivate the virtual environment. (#deactivate)
#deactivate

