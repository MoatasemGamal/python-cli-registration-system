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
    email = input("Enter Your Email:").strip()
    password = input("Enter Your Password").strip()
    u= Auth.login(email=email, password=password)
    if u:
        print(pyfiglet.figlet_format("Hello "+u.name))
    else:
        print(pyfiglet.figlet_format("Failed To login"))
elif n == 2:
    pass
else:
    print("You Should enter 1 or 2")