import urllib2.request
import json

url = 'https://www.googleapis.com/language/translate/v2?key={0}&q={1}&source={2}&target={3}'

def translate(api_key, text, sourcelang, targetlang):
	request = urllib2.Request(url.format(api_key.encode('utf-8'), text.encode('utf-8'), sourcelang.encode('utf-8'), targetlang.encode('utf-8')))
	response = urllib2.urlopen(request).read()
	data = json.loads(response)
	return data['data']['translations'][0]['translatedText'].encode('utf-8')

print (translate('API-KEY', 'Hello World', 'en', 'ja'))
