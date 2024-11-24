from one_key.User import User
from one_key.Credential import Credential

class PasswordManager:
    def __init__(self):
        self.__users = {}

    def add_user(self, user: User):
        username = user.get_username()
        if username in self.__users:
            return False
        self.__users[username] = user
        return True

    def remove_user(self, username: str):
        if username not in self.__users:
            return False
        del self.__users[username]
        return True

    def is_valid_user(self, username: str):
        if __get_user(username) is None:
            return False
        return True

    def __get_user(self, username: str):
        return self.__users.get(username)

    def sign_in(self, username: str, key: str):
        return user.sign_in(key)

    def sign_out(self, username: str):
        user.sign_out()

    def is_signed_in(self, username: str):
        return self.__get_user(username).is_signed_in()

    def get_key(self, username: str):
        return self.__get_user(username).get_key()

    def set_key(self, username: str, key: str):
        return self.__get_user(username).set_key(key)

    def get_username(self, username: str):
        return self.__get_user(username).get_username()

    def set_username(self, old_username: str, new_username: str):
        result = self.__get_user(old_username).set_username(new_username)
        if result:
            self.__users[new_username] = self.__users.pop(old_username)
        return result 

    def add_credential(self, username: str, credential: Credential):
        return self.__get_user(username).add_credential(credential)

    def remove_credential(self, username: str, website: str):
        return self.__get_user(username).remove_credential(website)

    def get_credential(self, username: str, website: str):
        return self.__get_user(username).get_credential(website)

