from random import randrange


class Pet:
    hungerCap = 1200
    joyCap = 1200
    joyRestore = 10
    hungerRestore = 20

    def __init__(self, givenName):
        self.name = givenName
        self.hunger = randrange(self.hungerCap // 2, self.hungerCap)
        self.joy = randrange(self.joyCap // 2, self.joyCap)

    async def tick(self):
        while self.state() != "dead":
            self.hunger -= 3
            self.joy -= 2
        # TODO: study async stuff and make it tick every second
        # I honestly tried but i need sleep rn

    def state(self):
        if self.hunger <= 0 or self.joy <= 0:
            return "dead"
        if self.hunger <= self.hungerCap // 3:
            return "hungry"
        if self.joy <= self.joyCap // 3:
            return "bored"
        return "alright"

    def reduceHunger(self, val=hungerRestore):
        self.hunger = min(self.hungerCap,
                          self.hunger + randrange(val // 2, val))

    def reduceBoredom(self, val=joyRestore):
        self.joy = min(self.joyCap, self.joy + randrange(val // 2, val))

    def feed(self):
        if self.state() == "dead":
            return
        self.reduceHunger()
        print(name + " is fed!")

    def play(self):
        if self.state() == "dead":
            return
        self.reduceBoredom()
        print(name + " is happy to play!")

    def printStatus(self):
        return f"{self.name} is {self.state()}: \n" \
               f"Hunger level: {self.hunger} \n" \
               f"Joy level: {self.joy} "


name = input("Name your pet: ")
p = Pet(name)

while True:
    cmd = input("What to do? ")
    if cmd == "help":
        print("You can use commands such as help, feed, play, status or exit")
    elif cmd == "feed":
        p.feed()
    elif cmd == "play":
        p.play()
    elif cmd == "status":
        print(p.printStatus())
    elif cmd == "exit":
        exit()
    else:
        print("Incorrect command. How about you type \"help\"?")
