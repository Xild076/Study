import random


class Study(object):
    def __init__(self):
        self.words = {
            "promise":"prometo",
            "alligence":"fidelidad",
            "the flag":"la bandera",
            "the United States":"los Estados Unidos",
            "the republic":"la repu^blica",
            "nation":"nacio^n",
            "God":"Dio^s",
            "indivisible":"indivisible",
            "with":"con",
            "liberty":"libertad",
            "justice":"justicia",
            "all":"todos"
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