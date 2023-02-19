import requests as rq
from datetime import datetime
from ParameterReader import ParameterReader
from DataFormatter import DataFormatter

class ApiRequester:
	def __init__(self) -> None:
		pass

	def RetrieveSatellitePosition(self) -> dict:
		"""
			This method will return a dictionary containing the 
			latitude and longitude position of the satellite at current time.
			
			The dictionary returned will have the following format:
			dict {
				"lat" : float(),
				"lgn" : float()
			}
		"""
		param_reader = ParameterReader()
		api_endpoint = param_reader.RetrieveSatelliteEndpoint()
		response = rq.get(api_endpoint)
		response.raise_for_status()
		data_formatter = DataFormatter()
		return data_formatter.FormatSatellitePositionData(response.json())

	def RetrieveSunsetInformation(self) -> datetime:
		"""
			This method will return the current sunset time according 
			to latitude and longitude specified in the parameters.
			The parameters will also contain a "formatted" attribute
			that specify whether or not the data retrieved from the API 
			will be formatted (refer to the api for further info.)
			The DataFormatter behaviour will follow along (current is 0).
		"""
		param_reader = ParameterReader()
		api_endpoint = param_reader.RetrieveSunsetInfoEndpoint()
		current_position = param_reader.RetrieveCurrentPosition()
		response = rq.get(api_endpoint, params=current_position)
		response.raise_for_status()
		data_formatter = DataFormatter()
		return data_formatter.FormatSunsetInfoData(response.json())