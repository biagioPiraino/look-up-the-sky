import requests as rq
from datetime import datetime
from ParameterReader import ParameterReader
from DataFormatter import DataFormatter

class ApiRequester:
	def __init__(self) -> None:
		pass

	def RetrieveSatellitePosition(self) -> dict:
		param_reader = ParameterReader()
		api_endpoint = param_reader.RetrieveSatelliteEndpoint()
		response = rq.get(api_endpoint)
		response.raise_for_status()
		data_formatter = DataFormatter()
		return data_formatter.FormatSatellitePositionData(response.json())

	def RetrieveSunsetInformation(self) -> datetime:
		param_reader = ParameterReader()
		api_endpoint = param_reader.RetrieveSunsetInfoEndpoint()
		current_position = param_reader.RetrieveCurrentPosition()
		response = rq.get(api_endpoint, params=current_position)
		response.raise_for_status()
		data_formatter = DataFormatter()
		return data_formatter.FormatSunsetInfoData(response.json())