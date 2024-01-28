from entities.muscle import Muscle


class Exercise:
    def __init__(self, name, muscle_name, muscle_region):
        self.name = name
        self.muscle = Muscle(muscle_name, muscle_region)
