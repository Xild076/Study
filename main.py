
import random


class Study(object):
    def __init__(self):
        self.words = {
            "brother": "hermano",
            "alma": "alma",
            "really": "realmente",
            "road": "camino",
            "journey": "jornada",
            "with me": "conmingo",
            "even though": "aunque",
            "man": "hombre",
            "friendship": "amistad",
            "respect": "respecto",
            "affection": "carin~o",
            "I remeber": "recuerdo",
            "together": "juntos",
            "hard": "duros",
            "moments": "momentos",
            "change": "cambiaste",
            "strong": "fuertes",
            "heart": "corazo^n",
            "doors": "puertas",
            "uncertain": "inciertas",
            "life": "la vida",
            "help": "ayude",
            "find": "encontrar",
            "exit": "salida",
            "word": "palabra",
            "certainly": "certeza",
            "smile": "sonrisa",
            "--": "abrazo",
            "--": "cada",
            "--": "llegada",
            "you say": "dices",
            "necessary": "preciso",
            "feel": "sentir",
            "big": "gran",
        }

        self.delete_copy = self.words

        self.wrong = []

    def start(self):
        while len(self.delete_copy) != 0:
            list_copy = list(self.delete_copy)
            rand = random.randint(0, len(list_copy)-1)
            print("")
            object_guess = list_copy[rand]
            guess = input(f"{object_guess}: ")
            if guess == self.delete_copy[object_guess]:
                print("Right")
            else:
                print("Wrong")
                print(self.delete_copy[object_guess])
            del (self.delete_copy[object_guess])

if __name__ == "__main__":
    study = Study()
    study.start()