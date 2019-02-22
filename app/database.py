class Database:
	file = 'database.json'

	def insert(self, listdata):
		if listdata == None:
			return False

		with open(file, 'w') as outfile:  
			json.dump(listdata, outfile)

	def read(self):
		with open(file) as json_file:  
			data = json.load(json_file)
    		return data