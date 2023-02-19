import requests as rq
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

	def RetrieveSunsetInformation(self) -> dict:
		pass

if __name__ == "__main__":
	ApiRequester.RetrieveSatellitePosition()