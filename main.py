import random


class Study(object):
    def __init__(self):
        self.words = {
            "I'll tell you":"contare^",
            "knows":"conocen",
            "the nickname":"el apodo",
            "husband":"marido",
            "says":"dice",
            "don't know":"no se^",
            "every day":"diario",
            "the dances":"los bailes",
            "bottle":"botella",
            "take off":"arranca",
            "the band":"la banda",
            "song":"cancio^n",
            "searches/looks":"busca",
            "dancer":"bailador",
            "the people":"gente",
            "begin":"empieza",
            "yell":"gritar",
            "nobody":"nadie",
            "can":"puede",
            "move":"mueve",
            "better":"mejor",
            "the rythem":"ri^tmo",
            "dances (verb)":"baila",
            "lose":"pierde",
            "trot":"trote",
        }

        self.delete_copy = self.words

        self.wrong = []

    def start(self):
        while len(self.delete_copy) != 0:
            list_copy = list(self.delete_copy)
            rand = random.randint(0, len(list_copy)-1)
            print(rand)
            object_guess = list_copy[rand]
            guess = input(f"{object_guess}: ")
            if guess == self.delete_copy[object_guess]:
                print("Right")
            else:
                print("Wrong")
            del (self.delete_copy[object_guess])

if __name__ == "__main__":
    study = Study()
    study.start()
