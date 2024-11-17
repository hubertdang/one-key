from one_key.Credential import Credential

class User:
    def __init__(self, name: str, key: str):
        self._name = name
        self._key = key
        self._credentials = {}

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name

    def get_key(self):
        return self._key

    def set_key(self, key: str):
        self._key = key

    def add_credential(self, credential: Credential):
        self._credentials[credential.get_website] = credential

    def remove_credential(self, website: str):
        del self._credentials[website]

    def get_credential(self, website: str, key: str):
        if self._key == key:
            return self._credentials[website]
