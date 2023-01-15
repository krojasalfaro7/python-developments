# import requests module
import requests
from requests.exceptions import HTTPError
from requests.exceptions import Timeout

# Making a get request
url = 'https://api.github.com/a'

try:
    response = requests.get(url, timeout=0.2)

    # If the response was successful, no Exception will be raised
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}, {http_err}')  # Python 3.6
except Timeout:
    print('The request timed out')
except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6
else:
    print('Success!')

# # ping an incorrect url
# response = requests.get('https://geeksforgeeks.org / naveen/')
#
# # print check if an error has occurred
# print(response.raise_for_status())