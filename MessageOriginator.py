import random
from datetime import datetime

class MessageOriginator:
	def __init__(self) -> None:
		self.__double_line = "\n\n"
    
	def GenerateMessage(self) -> str:
		subject = self.__retrieve_subject()
		message = self.__retrieve_message()
		return f"{subject}{message}"

	def __retrieve_subject(self) -> str:
		return f"Subject:Look Up The Sky!{self.__double_line}"

	def __retrieve_message(self) -> str:
		return f"Look up! A satellite is passing over your head!{self.__double_line}Python"