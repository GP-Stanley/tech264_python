import requests
# using request library to contact the website and find out its status code.
# get the content from the file: the raw htlm content.

request_bbc = requests.get("https://www.bbc.co.uk/")
print(request_bbc.status_code)
print(request_bbc.content)