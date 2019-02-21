
from fastapi import FastAPI
import json, requests

app = FastAPI()
file = open("database.json","w+")

class Item(BaseModel):
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
    return {"name": city.name, "country_code": city.country_code}

@app.get("/cities")
def list_cities() :
	return {"Sao Paulo", "Br", "Rio de Janeiro", "Rj"}

@app.get("/validate/{city_name}/{country_code}")
def validade_city(city_name:str, country_code: str ):
	url = "http://api.openweathermap.org/data/2.5/weather?q={},{}}&APPID=1069338b53130cb70404de749808bdaa".format(city_name, country_code)
	response = requests.get(url)

	if response.status_code != 200:
		return False

def forecast(city_id) :
	content_file = open_database_file()

def read_database():
	return json.load(file.read())