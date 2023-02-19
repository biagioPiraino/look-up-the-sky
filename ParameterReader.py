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
				"lgn"			 : float(data["current_position"]["longitude"]),
				"formatted": int(data["current_position"]["formatted"])
			}
			return current_position
	
	def RetrieveConnectionString(self) -> str:
		with open(file="parameters.json", mode="r") as file:
			data = json.load(file)
			return data["smtp_connection_string"]
	
	def RetrieveSenderCredentials(self) -> dict:
		with open(file="parameters.json", mode="r") as file:
			data = json.load(file)
			sender_credentials = {
				"email"			 : data["credentials"]["email"],
				"password"	 : data["credentials"]["password"],
			}
			return sender_credentials

	def RetrieveRecipientEmail(self) -> str:
		with open(file="parameters.json", mode="r") as file:
			data = json.load(file)
			return data["recipient_email"]

if __name__ == "__main__":
	a = ParameterReader()
	print(a.RetrieveConnectionString())
	print(a.RetrieveSenderCredentials())
	print(a.RetrieveRecipientEmail())