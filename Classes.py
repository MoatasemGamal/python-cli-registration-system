class User:
    def __init__(self, name, email, password):
        self.name=name
        self.email=email
        self.password=password

class UsersContainerSingleton:
    __singleton = None

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
            name     = line[0]
            email    = line[1]
            password = line[2]
            self.__users.append(User(name, email, password))
        file.close()