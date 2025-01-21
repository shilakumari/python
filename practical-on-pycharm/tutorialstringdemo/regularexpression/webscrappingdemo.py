import re
import urllib.request
# "urllib" allow to hit the url and get html contents of it
# "request" is the class

sites = ["google.com"]

for s in sites:
    print("Searching ",s)
    response = urllib.request.urlopen("http://"+s)
    # read() start reading the response
    text = response.read()
    title = re.findall("<title>.*</title>", str(text), re.I)# "re.I" -> regex case insensitive
    print(title[0])
