class AccessLevelException(Exception):
    pass


class SiteUser:
    def __init__(self, name, email, access_level):
        self._name = name
        self._email = email
        self._access_level = access_level
        self._logcount = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    def access_level(self, value):
        if value not in ("admin", "moderator", "user"):
            raise AccessLevelException
        self._access_level = value

    @property
    def logcount(self):
        return self._logcount

    def increase_logcount(self):
        self._logcount += 1

    def __str__(self):
        return f"User: {self.name}, Email: {self.email}, Access Level: {self.access_level}, Log Count: {self.logcount}"

    def __eq__(self, other):
        return self.access_level == other.access_level


user1 = SiteUser("Oleg Petrov", "oleg.petrov@test.com", "user")
user2 = SiteUser("Ira Bila", "ira.bila@test.com", "admin")
user3 = SiteUser("Inna Tyma", "inna.tyma@test.com", "moderator")

print(user1)
print(user2)
print(user3)

user1.increase_logcount()
print(f"Log Count for {user1.name}: {user1.logcount}")

# Порівняння за рівнем доступу
if user1 == user2:
    print("Users have the same access level.")
else:
    print("Users have different access levels.")