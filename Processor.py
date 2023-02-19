from ApiRequester import ApiRequester
from Checker import Checker
from NotificationHandler import NotificationHandler

class Processor:
	def __init__(self) -> None:
		pass

	def ProcessRequest(self) -> None:
		"""
			The processor checks:
			1) The satellite is nearby the user's specified location
			2) The time is appropriate to see the satellite (after sunset)

			In case the condition are met, an email notification will be send to a recipient
		"""
		api_requester = ApiRequester()
		checker = Checker()
		if (checker.CheckCurrentPosition(api_requester.RetrieveSatellitePosition()) and 
				checker.CheckCurrentDateTime(api_requester.RetrieveSunsetInformation())):
				not_handler = NotificationHandler()
				not_handler.RaiseNotification()