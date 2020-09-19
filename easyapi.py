import urllib.request
import json
def api(url):
	response = urllib.request.urlopen(url)
	result = json.loads(response.read())
	end = result
	return end
