import re
class User:
    def __init__(self, name, email, password):
        self.name=name
        self.email=email
        self.password=password

class UsersContainerSingleton:
    __singleton = None
    __number_of_users = 0

    def __init__(self):
        if UsersContainerSingleton.__singleton != None:
            raise Exception("This singleton instantiated before !")
        self.__users = []
        UsersContainerSingleton.__singleton=self
    @classmethod
    def get_instance(cls):
        if cls.__singleton==None:
            UsersContainerSingleton()
        return cls.__singleton

    def create_user(self, name, email, password):
        user = User(name, email, password)
        self.__users.append(user)
        UsersContainerSingleton.__number_of_users+=1

    def store_users(self):
        file = open("./users.txt", "w")
        lines=[]
        for user in self.__users:
            line = "|".join([user.name, user.email, user.password])
            lines.append(line+"\n")
        file.writelines(lines)
        file.close()

    def load_users(self):
        file = open("./users.txt")
        for line in file:
            line=line.strip("\n")
            line = line.split("|")
            if len(line) == 3:
                name     = line[0]
                email    = line[1]
                password = line[2]
                self.__users.append(User(name, email, password))
                UsersContainerSingleton.__number_of_users+=1
        file.close()

    def get_users(self):
        return self.__users

    @classmethod
    def get_num_of_users(cls):
        return cls.__number_of_users

class Auth:
    @staticmethod
    def login(email, password):
        user = Auth.__search_in_users(email)
        if user and user.password == password:
            return user
        else:
            return False

    @staticmethod
    def register(name, email, password):
        email_pattern = "^[a-zA-Z0-9_\.]+@[a-zA-Z0-9_.]+\.[a-z]{1,3}$"
        user=Auth.__search_in_users(email)
        if not user and re.match(email_pattern, email):
            UsersContainerSingleton.get_instance().create_user(name, email, password)
            UsersContainerSingleton.get_instance().store_users()
            return True
        return False

    @staticmethod
    def __search_in_users(email):
        users = UsersContainerSingleton.get_instance().get_users()
        for u in users:
            if u.email == email:
                return u
        return False