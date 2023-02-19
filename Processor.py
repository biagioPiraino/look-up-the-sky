from ApiRequester import ApiRequester
from Checker import Checker
from NotificationHandler import NotificationHandler

class Processor:
	def __init__(self) -> None:
		pass

	def ProcessRequest(self) -> None:
		api_requester = ApiRequester()
		checker = Checker()
		if (checker.CheckCurrentPosition(api_requester.RetrieveSatellitePosition()) and 
				checker.CheckCurrentDateTime(api_requester.RetrieveSunsetInformation())):
				not_handler = NotificationHandler()
				not_handler.RaiseNotification()