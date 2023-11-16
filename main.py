from Classes import User, UsersContainerSingleton, Auth
import pyfiglet

# get the singleton instance from UsersContainerSingleton class
container = UsersContainerSingleton.get_instance()
# load data from the users.txt file
container.load_users()


print("Menu:\n1) Login\n2) Register\n")

n = input("chose option: ")
n=int(n)

if n == 1:
    pass
elif n==2:
    pass
else:
    pass