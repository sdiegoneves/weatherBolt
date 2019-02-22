
from fastapi import FastAPI
from pydantic import BaseModel

#from database import Database
#from weather import Weather

app = FastAPI()

class City(BaseModel):
    name: str
    country_code: str


@app.get("/")
def read_root():
	return {"Hello": "World"}

@app.get("/city/{city_id}")
def read_item(city_id: int):
    return {"city_id": city_id}

@app.post("/create")
def create_item(city: City):
	#city_dict = {}
	#city_dict['key'] = len(Database.read) + 1
	#city_dict['name'] = city.name
	#city_dict['country_code'] = city.country_code

	#Database.insert(city_dict)

	return {"success": "true"}

@app.get("/cities")
def list_cities() :
	return {"Sao Paulo", "Br", "Rio de Janeiro", "Rj"}

@app.get("/validate/{city_name}/{country_code}")
def validade_city(city_name:str, country_code: str ):
	url = "http://api.openweathermap.org/data/2.5/weather?q={},{}}&APPID=1069338b53130cb70404de749808bdaa".format(city_name, country_code)
	response = requests.get(url)

	if response.status_code != 200:
		return False