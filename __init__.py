import json
import urllib.request

def postmanRequest(endpoint):
    request = urllib.request.Request('https://api.covid19api.com/' + endpoint)
    requestData = json.loads(urllib.request.urlopen(request).read().decode("utf-8"))

    return requestData