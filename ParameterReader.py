import json

class ParameterReader:
	def __init__(self) -> None:
		pass
	
	def RetrieveSatelliteEndpoint(self) -> str:
		with open(file="parameters.json", mode="r") as file:
			data = json.load(file)
			return data["satellite_endpoint"] # Probably worth defining a constant class
