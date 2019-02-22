import json, requests, datetime


class Weather:
	api_key = "1069338b53130cb70404de749808bdaa"
	url = "http://api.openweathermap.org/data/2.5/weather?q={},{}&APPID={}"

	def validate_city(self, city_name, country_code):
		call_url = url.format(self.api_key, city_name, country_code)
		response = requests.get(call_url)
		if response.status_code != 200:
			return False

	def getForcast(self, city_name, country_code, qtd_days = 6):
		forcast = []
		for x in range(0, qtd_days):
			call_url = url + "&DATE=%s"

			datetime_format = datetime.date.today() + datetime.timedelta(x)
			datetime_unix = datetime_format.strftime("%s")

			call_url = call_url % (city_name, country_code, api_key, datetime_unix)
			response = requests.get(call_url)
			data = json.loads(response.content)
			
			items = {"weather" : data['weather'], "main" :  data['main']}
			forcast.append(items)

		return forcast