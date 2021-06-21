import random
from operator import eq

class Lottery:

    def __init__(self, min=1, max=49):
        self.min = min
        self.max = max
        self.picked_numbers = []
        self.possible_choices = list(range(max+1))
        self.prizes = [0, 0, 20.00, 100.50, 2384.00, 8584.00, 10000000.00]

    def show_choices(self):
        for i, choice in enumerate(self.possible_choices):
            if i % 10 == 0:
                print()
            else:
                print(choice, "\t", end="")

    def play(self, picked):
        winning_combo = random.sample(range(self.min, self.max), 6)
        # winning_combo = [1, 2, 3, 4, 5 ,6]
        print("Winning combo is", winning_combo)

        res = sum(map(eq, picked, winning_combo))

        print("There were", res, "numbers in common!")
        print("You win R", self.prizes[res])
        # https://www.geeksforgeeks.org/python-count-of-common-elements-in-the-lists/

    def gather_choices(self):
        while len(self.picked_numbers) < 6:
            self.show_choices() # starting at 2 for some reason

            user_choice = int(input("Pick one of these numbers: "))

            if self.valid_pick(self.picked_numbers, user_choice):
                self.picked_numbers.append(user_choice)
                self.possible_choices.remove(user_choice)
            else:
                print("Invalid option, try again!")        
            
        print(self.picked_numbers, "were the picked numbers")
        self.play(self.picked_numbers)

    def valid_pick(self, picked_numbers, user_choice):
        has_picked = (user_choice in picked_numbers)
        valid_range = user_choice >= self.min and user_choice <= self.max
        if not has_picked and valid_range:
            return True
        else:
            return False
