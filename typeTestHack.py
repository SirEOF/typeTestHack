import requests
myCPM = '999'

data = {}
data['typing-speed-test.aoeu.eu'] = '%s CPM' % myCPM
data['tst-internal/details'] = {
   'cpm':myCPM,
   'rawcpm':myCPM,
   'wrong':0,
   'words':0,
   'keys':0,
   'chars':myCPM,
   'cheater':0,
   'iphone':0,
   'enterused':0
}

headers = {
	'Origin': 'http://typing-speed-test.aoeu.eu',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}


while True:
	r = requests.post('http://stats.aoeu.eu/mqtt', data=data, headers=headers)
	print (r.text)

