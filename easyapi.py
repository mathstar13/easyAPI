import urllib.request
import json
def api(url,location=''):
	global end
	response = urllib.request.urlopen(url)
	result = json.loads(response.read())
	end = result
	if location != '':
		exec(f'''global data 
data = {location}''')
api('https://ultimatefreegames.000webhostapp.com/data.json','end["hello"]')
print(data)