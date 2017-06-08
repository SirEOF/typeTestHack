
import requests
import time
import json
import uuid
myCPM = '999'

data = {}
data['typing-speed-test.aoeu.eu'] = '%s CPM' % myCPM
data['tst-internal/details'] = json.dumps({
   'cpm':myCPM,
   'rawcpm':myCPM,
   'wrong':0,
   'words':34,
   'ip':uuid.uuid4().hex,
   'keys':224,
   'chars':myCPM,
   'cheater':0,
   'iphone':0,
   'enterused':0
})

headers = {
	'Connection': 'keep-alive',
	'Accept': '*/*',
	'Origin': 'http://typing-speed-test.aoeu.eu',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Referer': 'http://typing-speed-test.aoeu.eu/',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.8,he;q=0.6',
}


while True:
	r = requests.post('http://stats.aoeu.eu/mqtt', data=data, headers=headers)
	print (r.text)
	#time.sleep(0.4)


