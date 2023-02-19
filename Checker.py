from datetime import datetime
from ParameterReader import ParameterReader

class Checker:
	def __init__(self) -> None:
		self.__latitude_range  = 5
		self.__longitude_range = 5

	def CheckCurrentPosition(self, satellite_position: dict) -> bool:
		"""
			This method checks whether the satellite position
			falls within the range specified in the constructor.
			Both latitude and longitude will be checked independently
		"""
		param_reader = ParameterReader()
		current_location = param_reader.RetrieveCurrentPosition()
		satellite_within_range = (self.__check_latitude_range(
			satellite_position["lat"], current_location["lat"]
		)) and (self.__check_longitude_range(
			satellite_position["lgn"], current_location["lgn"]
		))
		return satellite_within_range

	def CheckCurrentDateTime(self, sunset_time: datetime) -> bool:
		"""
			This method checks whether the current hour is greater or equal
			than the sunset hour of the current position retrieved from	the API
		"""
		return datetime.now().hour >= sunset_time.hour

	def __check_latitude_range(self, satellite_lat: float, personal_lat: float) -> bool:
		return (personal_lat - self.__latitude_range) <= satellite_lat <= (personal_lat + self.__latitude_range)

	def __check_longitude_range(self, satellite_lgn: float, personal_lgn: float) -> bool:
		return (personal_lgn - self.__longitude_range) <= satellite_lgn <= (personal_lgn + self.__longitude_range)