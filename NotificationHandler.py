from MessageOriginator import MessageOriginator
from MessageSender import MessageSender

class NotificationHandler:
	def __init__(self) -> None:
		pass

	def RaiseNotification(self) -> None:
		message_originator = MessageOriginator()
		sender = MessageSender()
		sender.SendMessage(message_originator.GenerateMessage())