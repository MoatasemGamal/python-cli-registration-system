from Classes import User, UsersContainerSingleton, Auth
import pyfiglet

# get the singleton instance from UsersContainerSingleton class
container = UsersContainerSingleton.get_instance()
# load data from the users.txt file
container.load_users()
