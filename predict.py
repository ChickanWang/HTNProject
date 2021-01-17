import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

# allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# data = {
#     "Inputs": {
#           "WebServiceInput0":
#           [
#               {
#                     'Datetime': "2021-01-11T14:30:00Z",
#                     'Open': "218.25",
#                     'High': "218.25",
#                     'Low': "218.25",
#                     'Close': "218.25",
#               },
#           ],
#     },
#     "GlobalParameters":  {
#     }
# }

# body = str.encode(json.dumps(data))

# url = 'http://52.152.136.80:80/api/v1/service/test/score'
# api_key = 'fx4RuN9BGkIQhJ4XichTGgaEjVmsIb11' # Replace this with the API key for the web service
# headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

# req = urllib.request.Request(url, body, headers)

# try:
#     response = urllib.request.urlopen(req)

#     result = response.read()
#     print(result)
# except urllib.error.HTTPError as error:
#     print("The request failed with status code: " + str(error.code))

#     # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
#     print(error.info())
#     print(json.loads(error.read().decode("utf8", 'ignore')))