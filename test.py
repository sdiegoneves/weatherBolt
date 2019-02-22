import json, requests, time, datetime

#print(time.time())
#day = datetime.datetime.today() + datetime.timedelta(1)
#print(day.strftime("%s"))
city_name = "Rio de janeiro"
country_code = "Br"

api_key = "1069338b53130cb70404de749808bdaa"


forcast = []

for x in range(0, 1):
	url = "http://api.openweathermap.org/data/2.5/weather?q=%s,%s&APPID=%s"
	url += "&DATE=%s"

	datetime_format = datetime.date.today() + datetime.timedelta(x)
	datetime_unix = datetime_format.strftime("%s")

	url = url % (city_name, country_code, api_key, datetime_unix)
	response = requests.get(url)
	data = json.loads(response.content)
	
	items = {"weather" : data['weather'], "main" :  data['main']}
	forcast.append(items)
print(forcast)

"""listdata = []
data = {}
data['key'] = 1
data['city'] = city_name
data['country_code'] = country_code
listdata.append(data)

data = {}
data['key'] = 2
data['city'] = city_name
data['country_code'] = country_code
listdata.append(data)

#json_data = json.dumps(listdata)
#print(json_data)

#file = open("database.json","w+")
#file.write(json_data)
#content = file.read()
with open('database.json', 'w') as outfile:  
    json.dump(listdata, outfile)


with open('database.json') as json_file:  
    data = json.load(json_file)
    print(data)
#content = json.loads(content)
#content = json.loads(content)

#print(type(content))"""
