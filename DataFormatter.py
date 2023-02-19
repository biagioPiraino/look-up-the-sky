from datetime import datetime

class DataFormatter:
	def __init__(self) -> None:
		pass

	def FormatSatellitePositionData(self, data: dict) -> dict:
		satellite_position = {
			"lat": float(data["iss_position"]["latitude"]),
			"lgn": float(data["iss_position"]["longitude"])
		}
		return satellite_position

	def FormatSunsetInfoData(self, data: dict) -> datetime:
		split_day_time = data["results"]["sunset"].split("T")
		day_info  = [int(x) for x in split_day_time[0].split("-")]
		time_info = [int(x) for x in split_day_time[1].split("+")[0].split(":")]
		return datetime(
			day_info[0] , day_info[1] , day_info[2],
			time_info[0], time_info[1], time_info[2])