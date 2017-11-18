
def print_details(name, age, username):
    statement = "Your name is {}, you are {} years old and your username is {}"
    print(statement.format(name, age, username))

if __name__ == '__main__':
    name = input("Name >> ")
    age = int(input("Age >> "))
    username = input("Username >> ")

    print_details(name, age, username)


class MyClass(object):
    def __int__(self, name, owner, uid, breed, animal_type, likes_cats):
        self.name = name
        self.owner = owner
        self.uid = uid
        self.breed = breed
        self.animal_type = animal_type
        self.likes_cats = likes_cats
