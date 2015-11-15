import httplib, urllib
import time
temp = 39
params = urllib.urlencode({'field1': temp, 'key':'ZP1PZO62773HXWVU'})
#headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = httplib.HTTPConnection("api.thingspeak.com:80") 
#conn.request("POST", "/update", params, headers)
conn.request("POST", "/update", params)
response = conn.getresponse()
print temp

print response.status, response.reason

data = response.read()
conn.close()

time.sleep(16)


