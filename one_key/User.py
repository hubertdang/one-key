from one_key.Credential import Credential

class User:
    def __init__(self, name: str, key: str):
        self.__name = name
        self.__key = key
        self.__credentials = {}

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_key(self):
        return self.__key

    def set__key(self, key: str):
        self.__key = key

    def add_credential(self, credential: Credential):
        self.__credentials[credential.get_website] = credential

    def remove_credential(self, website: str):
        del self.__credentials[website]

    def get_credential(self, website: str, key: str):
        if self.__key == key:
            return self.__credentials[website]
