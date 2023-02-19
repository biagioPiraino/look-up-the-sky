import smtplib as smt
from ParameterReader import ParameterReader

class MessageSender:
	def __init__(self) -> None:
		pass

	def SendMessage(self, message: str) -> None:
		try:
			with self.__connect() as connection:
				parameter_reader = ParameterReader()
				connection.sendmail(
						from_addr=connection.user, to_addrs=parameter_reader.RetrieveRecipientEmail(), msg=message)
		except (smt.SMTPHeloError, smt.SMTPAuthenticationError,
						smt.SMTPConnectError, smt.SMTPException) as error:
			print(error)

	def __connect(self) -> smt.SMTP:
		parameter_reader = ParameterReader()
		smtp_connection = smt.SMTP(parameter_reader.RetrieveConnectionString())
		smtp_connection.starttls()
		credentials = parameter_reader.RetrieveSenderCredentials() 
		smtp_connection.login(user=credentials["email"], password=credentials["password"])
		return smtp_connection