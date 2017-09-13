
def print_details(name, age, username):
    statement = "Your name is {}, you are {} years old and your username is {}"
    print(statement.format(name, age, username))

if __name__ == '__main__':
    name = input("Name >> ")
    age = int(input("Age >> "))
    username = input("Username >> ")

    print_details(name, age, username)
