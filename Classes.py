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