
import random


class Study(object):
    def __init__(self):
        self.words = {
            "Arm Curl":"biceps",
            "Ab crunches":"rectus abs",
            "Shoulder Press":"deltoids, triceps",
            "Abductor machine":"abductors,hip flexors",
            "Adductor machine":"adductors",
            "Leg press":"quads",
            "Leg curls":"hamstring",
            "Heel Raises":"calf",
            "Back Extension":"erector spinae,glutes",
            "Squats":"quads,glutes",
            "Lat Pull Down":"lats,biceps",
            "Seated Row":"traps,biceps",
            "Pull Ups":"biceps,lats",
            "Toe Raises":"tibs",
            "Step Ups":"quads,glutes,calf",
            "Lunges":"quads,glutes,calf",
            "Dips":"triceps,lats",
            "Chest Flies":"delts,pecs",
            "Lateral Raises":"delts",
            "Push Ups":"triceps,pecs",
            "Bench Press":"triceps,pecs",
            "calf":"tibs",
            "tibs":"calf",
            "erector spinae":"rectus ab",
            "trot":"trote",
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
