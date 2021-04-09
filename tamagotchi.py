from random import randrange
import os


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Pet:
    chonkCap = 1200
    # rewriting logic because of a bad variable name
    # sounds weird so here's a meme: https://imgur.com/sNqNi9E
    joyCap = 1200
    joyRestore = 10
    chonkIncrease = 20
    petPic = [list("    /\\\\/\\\\          ___  "),
              list("   = o_o =_______    \\ \\ "),
              list("    __^      __(  \\.__) )"),
              list("    <_____>__(_____)____/")]
    eye = "o"

    def __init__(self, givenName):
        self.name = givenName
        self.hunger = randrange(self.chonkCap // 2, self.chonkCap)
        self.joy = randrange(self.joyCap // 2, self.joyCap)

    async def tick(self):
        if self.state() != "dead":
            self.hunger -= 3
            self.joy -= 2
        # TODO: study async stuff and make it tick every second
        # still not implemented i'll ask about it on tuesday

    def state(self):
        if self.hunger <= 0 or self.joy <= 0:
            return "dead"
        if self.hunger <= self.chonkCap // 3:
            return "hungry"
        if self.joy <= self.joyCap // 3:
            return "bored"
        return "happy"

    def reduceChonk(self, val=chonkIncrease):
        self.hunger = min(self.chonkCap,
                          self.hunger + randrange(val // 2, val))

    def reduceBoredom(self, val=joyRestore):
        self.joy = min(self.joyCap, self.joy + randrange(val // 2, val))

    def feed(self):
        if self.state() == "dead":
            return
        self.reduceChonk()
        print(name + " is fed!")

    def play(self):
        if self.state() == "dead":
            return
        self.reduceBoredom()
        print(name + " is happy to play!")

    def printStatus(self):
        st = self.state()
        if st == "dead":
            eye = "x"
        elif st == "hungry":
            eye = "o"
        elif st == "bored":
            eye = "-"
        elif st == "happy":
            eye = "^"
        else:
            eye = "?"

        self.petPic[1][5] = eye
        self.petPic[1][7] = eye
        status = [line.copy() for line in self.petPic]
        status[1] += " Current joy:        " + str(self.joy)
        status[2] += " Current chonkiness: " + str(self.hunger)
        status[3] += " " + self.name + " is " + self.state() + "!"
        for line in status:
            print("".join(line))


clearScreen()
name = input("Name your pet: ")
p = Pet(name)

while True:
    cmd = input("What to do? ")
    clearScreen()
    p.printStatus()
    if cmd == "help":
        print("You can use commands such as help, feed, play or exit")
    elif cmd == "feed":
        p.feed()
    elif cmd == "play":
        p.play()
    elif cmd == "exit":
        exit()
    else:
        print("Incorrect command. How about you type \"help\"?")
