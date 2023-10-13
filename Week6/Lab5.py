# Lab4
# Author: Frank R. Leotta III

"""_summary_
This lab is designed to get you familiar with Python virtual environments as well as import statments to use external libraries.
"""

# 1. Create a virtual environment called "venv" in the current directory. (Python3 -m venv venv)
#python3 -m venv venv
# 2. Activate the virtual environment. (venv\Scripts\activa                                                                                                                                                                                                                                                                                                                                                                                                         te)
#source venv/bin/activate
# 3. Install the requests library. (py -m pip install requests) 
#pip install requests
# 4. import requests library here
import requests
# 5. Use the requests library to make a GET request to https://api.github.com/events
get = requests.get("https://api.github.com/events")
# 6. Print out the status code of the response.
print(get.status_code)
# 7. Print out the content of the response.
print(get.content)
# 8. Print out the headers of the response.
print(get.headers)
# 9. Deactivate the virtual environment. (Type command here in comments)
#deactivate
