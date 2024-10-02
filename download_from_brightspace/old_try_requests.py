import requests
from bs4 import BeautifulSoup

# Constants for the URLs
BRIGHTSPACE_URL = "https://brightspace.tudelft.nl/"
LOGIN_URL = "https://login.tudelft.nl/sso/module.php/core/loginuserpass.php"

# Your login credentials
USERNAME = "#ToDo"
PASSWORD = "#ToDo"

# Create a session object to persist cookies across requests
session = requests.Session()

# Step 1: GET request to Brightspace URL to store cookies
response = session.get(BRIGHTSPACE_URL)
response.raise_for_status()  # Check for HTTP errors

# Step 2: Parse the HTML to find the AuthState value
soup = BeautifulSoup(response.text, 'html.parser')
# Assuming the AuthState is found in a hidden input field; adjust selector as needed
authstate_input = soup.find('input', {'name': 'AuthState'})
if authstate_input:
    authstate_value = authstate_input['value']
else:
    raise ValueError("AuthState not found in the response")

# Step 3: Prepare and send the POST request to the login URL
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": LOGIN_URL,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

data = {
    "username": USERNAME,
    "password": PASSWORD,
    "AuthState": authstate_value
}

login_response = session.post(LOGIN_URL, headers=headers, data=data)
login_response.raise_for_status()  # Check for HTTP errors

# Check if login was successful
if "logout" in login_response.text.lower():
    print("Login successful!")
else:
    print("Login failed. Check your credentials or AuthState.")

# Optional: print the response or do something with the logged-in session
print(login_response.text)


# curl -c cookies.txt -L "https://brightspace.tudelft.nl/"

"""
curl -b cookies.txt -L -X POST "https://login.tudelft.nl/sso/module.php/core/loginuserpass.php" \
-H "Content-Type: application/x-www-form-urlencoded" \
-H "Referer: https://login.tudelft.nl/sso/module.php/core/loginuserpass.php?AuthState=#ToDo%3Ahttps%3A%2F%2Flogin.tudelft.nl%2Fsso%2Fsaml2%2Fidp%2FSSOService.php%3Fspentityid%3Dhttps%253A%252F%252Fengine.surfconext.nl%252Fauthentication%252Fsp%252Fmetadata%26cookieTime%#ToDo" \
-H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36" \
--data-urlencode "username=#ToDo" \
--data-urlencode "password=#ToDo" \
--data-urlencode "AuthState=#ToDo"
"""

# curl https://brightspace.tudelft.nl/
# curl https://brightspace.tudelft.nl/Shibboleth.sso/Login?entityID=https://engine.surfconext.nl/authentication/idp/metadata&target=https%3A%2F%2Fbrightspace.tudelft.nl%2Fd2l%2FshibbolethSSO%2Flogin.d2l