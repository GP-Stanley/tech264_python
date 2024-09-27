# return info about a particular postcode

import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")     #.get request for this endpoint of the api: "se120nb".


print(f"Status code: {post_codes_req.status_code}")     # getting status code.
print(f"Headers: {post_codes_req.headers}")             # getting the 'headers'
print(f"Content: {post_codes_req.content}")             # getting the 'content'
print(f"JSON: {post_codes_req.json()}")                 # getting 'JSON'
print(f"Data type of JSON: {type(post_codes_req.json())}")      # getting data type: output: Data type of JSON: <class 'dict'>

print("----------------------------------------------------")

data_dict = post_codes_req.json()['result']
print(f"Region: {data_dict['region']}")                         # Output: Region: London


# From Karis: from pprint import pprint
# pprint(post_codes_req.json())


print("----------------------------------------------------")

# send a post request




