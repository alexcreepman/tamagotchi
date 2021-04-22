from random import randrange


class Pet:
    chonkCap = 1200
    # rewriting logic because of a bad variable name
    # sounds weird so here's a meme: https://imgur.com/sNqNi9E
    joyCap = 1200
    joyRestore = 10
    chonkIncrease = 20
    petPic = [list("      /\\\\ /\\\\                         ___  "),
              list("   = o_o =_______          \\   \\ "),
              list("    __^              __(     \\.__)  )"),
              list("  <_____>__(_____)____/")]
    eye = "o"

    def __init__(self, givenName):
        self.name = givenName
        self.chonkiness = randrange(2 * self.chonkCap // 3, self.chonkCap)
        self.joy = randrange(self.joyCap // 2, self.joyCap)

    def tick(self):
        if self.state() != "dead":
            self.chonkiness -= 3
            self.joy -= 2

    def state(self):
        if self.chonkiness <= 0 or self.joy <= 0:
            return "dead"
        if self.chonkiness <= self.chonkCap // 3:
            return "hungry"
        if self.joy <= self.joyCap // 3:
            return "bored"
        return "happy"

    def reduceChonk(self, val=chonkIncrease):
        self.chonkiness = min(self.chonkCap,
                              self.chonkiness + randrange(val // 2, val))

    def reduceBoredom(self, val=joyRestore):
        self.joy = min(self.joyCap, self.joy + randrange(val // 2, val))

    def feed(self):
        if self.state() == "dead":
            return
        self.reduceChonk()
        # print(self.name + " is fed!")

    def play(self):
        if self.state() == "dead":
            return
        self.reduceBoredom()
        # print(self.name + " is happy to play!")

    def getStatus(self):
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
        status[2] += " Current chonkiness: " + str(self.chonkiness)
        status[3] += " " + self.name + " is " + self.state() + "!"
        lines = [''.join(line) for line in status]
        return lines
