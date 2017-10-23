import urllib2
import json
req = urllib2.Request('http://www.baidu.com')
response =  None
data1 = {'error':'404'}
d2 = json.dumps(data1)
# response = urllib2.urlopen(req).read().decode('utf-8')
# the_page = response.read().decode('utf-8')
# s = json.loads(response.read().decode('utf-8'))

print d2
print data1
print json.loads(d2)