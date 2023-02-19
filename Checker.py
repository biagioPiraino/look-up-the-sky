from datetime import datetime
from ParameterReader import ParameterReader

class Checker:
	def __init__(self) -> None:
		self.__latitude_range  = 5
		self.__longitude_range = 5

	def CheckCurrentPosition(self, satellite_position: dict) -> bool:
		param_reader = ParameterReader()
		current_location = param_reader.RetrieveCurrentPosition()
		satellite_within_range = (self.__check_latitude_range(
			satellite_position["lat"], current_location["lat"]
		)) and (self.__check_longitude_range(
			satellite_position["lgn"], current_location["lgn"]
		))
		return satellite_within_range

	def CheckCurrentDateTime(self, sunset_time: datetime) -> bool:
		return datetime.now().hour >= sunset_time.hour

	def __check_latitude_range(self, satellite_lat: float, personal_lat: float) -> bool:
		return satellite_lat in range(personal_lat - self.__latitude_range, personal_lat + self.__latitude_range) 

	def __check_longitude_range(self, satellite_lgn: float, personal_lgn: float) -> bool:
		return satellite_lgn in range(personal_lgn - self.__longitude_range, personal_lgn + self.__longitude_range)