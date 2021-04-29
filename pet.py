from random import randrange


class Pet:
    chonk_cap = 1200
    # rewriting logic because of a bad variable name
    # sounds weird so here's a meme: https://imgur.com/sNqNi9E
    joy_cap = 1200
    joy_restore = 10
    chonk_increase = 20

    def __init__(self, given_name):
        self.name = given_name
        self.chonkiness = randrange(self.chonk_cap // 3, self.chonk_cap)
        self.joy = randrange(self.joy_cap // 3, self.joy_cap)

    def tick(self):
        if self.state() != "dead":
            self.chonkiness -= 3
            self.joy -= 2
        else:
            self.chonkiness = max(0, self.chonkiness)
            self.joy = max(0, self.joy)

    def state(self):
        if self.chonkiness <= 0 or self.joy <= 0:
            return "dead"
        if self.chonkiness <= self.chonk_cap // 3:
            return "hungry"
        if self.joy <= self.joy_cap // 3:
            return "bored"
        return "happy"

    def reduce_chonk(self, val=chonk_increase):
        self.chonkiness = min(self.chonk_cap,
                              self.chonkiness + randrange(val // 2, val))

    def reduce_boredom(self, val=joy_restore):
        self.joy = min(self.joy_cap, self.joy + randrange(val // 2, val))

    def feed(self):
        if self.state() == "dead":
            return
        self.reduce_chonk()

    def play(self):
        if self.state() == "dead":
            return
        self.reduce_boredom()

    def get_status(self):
        st = self.state()
        return "graphics/" + st + ".png"

    def is_dead(self):
        return " is dead :(" if self.state() == "dead" else ""
