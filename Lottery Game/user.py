import uuid
from datetime import date
from lottery import Lottery

class User:
    def __init__(self, name, email, address, id_num):
        self.name = name
        self.email = email
        self.address = address
        self.id_num = id_num
        self.player_id = uuid.uuid4() # creating a random UUID

    def validate(self):
        todays_date = date.today()
        digits = int(self.id_num[:2])
        age = todays_date.year - digits

        if age >= 18:
            return "Let's Play", True
        else:
            return f"Come back in {18 - age} years", False
        

    def write_to_file(self):
        with open('user.csv', "a+") as user_file:
            user_file.write(self.__str__())

    def __str__(self):
        return f"{self.name}, {self.email}, {self.address}, {self.id_num}, {self.player_id}\n"

def register():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    id_num = input("Enter your id_num: ")

    user = User(name, email, address, id_num)
    user.validate()
    user.write_to_file()

    return user


def menu():
    user = register()
    game = Lottery()
    game.gather_choices()

menu()