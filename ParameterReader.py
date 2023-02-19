import json

class ParameterReader:
	def __init__(self) -> None:
		pass
	
	def RetrieveSatelliteEndpoint(self) -> str:
		with open(file="parameters.json", mode="r") as file:
			data = json.load(file)
			return data["satellite_endpoint"]

	def RetrieveSunsetInfoEndpoint(self) -> str:
		with open(file="parameters.json", mode="r") as file:
			data = json.load(file)
			return data["sunset_info_endpoint"]

	def RetrieveCurrentPosition(self) -> dict:
		with open(file="parameters.json", mode="r") as file:
			data = json.load(file)
			current_position = {
				"lat"			 : float(data["current_position"]["latitude"]),
				"lng"			 : float(data["current_position"]["longitude"]),
				"formatted": int(data["current_position"]["formatted"])
			}
			return current_position