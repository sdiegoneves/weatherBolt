import json, requests
city_name = "Rio de janeiro"
country_code = "Bg"

listdata = []
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

json_data = json.dumps(listdata)
print(json_data)

file = open("database.json","w+")
file.write(json_data)
content = file.read()

#content = json.loads(content)
print(type(content))