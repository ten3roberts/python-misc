import random

users = {}


class User:
    name = ""
    balance = 100

    def __init__(self, name, balance):
        if self.name in users:
            print("[error]: user", self.name, "already exists")
            return
        self.name = name
        self.balance = balance

        users[self.name] = self

    def speak(self):
        print("Hello there")

    def get_balance(self):
        print("Your balance is $" + str(self.balance))

    def work(self):
        earn = random.randint(10, 15)
        print("You earned $" + str(earn))
        self.balance += earn

    def spend(self):
        lose = random.randint(15, 20)
        if self.balance - lose < 0:
            print("Insufficient funds")
            return
        print("You spend $" + str(lose))
        self.balance -= lose


def print_help(dummy):
    print(" -> 'speak' says a random message")
    print(" -> 'balance' displays your current balance")
    print(" -> 'work' earns you a random amount")
    print(" -> 'spend' spends a random amount")
    print(" -> 'help' shows you available commands")


commands = {
    'speak': User.speak,
    'balance': User.get_balance,
    'work': User.work,
    'spend': User.spend,
    'help': print_help
}


# Create users
User("Tim", 100)
User("Emma", 160)


user = None

while True:
    print("login:", end=' ')
    username = input()
    if username in users:
        user = users[username]
        break
    else:
        print("user does not exist")

print("Welcome back", user.name)

while True:
    print(user.name + ":", end=' ')
    cmd = input().lower()

    if cmd in commands:
        commands[cmd](user)
    else:
        print("[error]: invalid command, use 'help' for a list of commands")

    print()
