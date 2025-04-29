from colorama import Back, Fore, Style


class BaseModel:
    """The model is responsible managing external services (database, API, libraries, etc),"""

    testing: bool = False

    def __init__(self, **kwargs):
        testing = kwargs.get("testing")
        if testing:
            print(f"     {Fore.RED}{Back.WHITE} TEST MODE IS ON {Style.RESET_ALL}")
            self.testing = testing
