from colorama import Fore, Style, Back


class BaseModel:
	"""Base model class for all models
	(Not database or Pydantic)"""
	testing: bool = False

	def __init__(self, **kwargs):
		testing = kwargs.get('testing')
		if testing:
			print(f"     {Fore.RED}{Back.WHITE} TEST MODE IS ON {Style.RESET_ALL}")
			self.testing = testing
