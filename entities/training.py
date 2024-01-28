class Training:
    def __init__(self, name):
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)
        print(f"Exercício '{exercise.name}' adicionado ao treino '{self.name}'.") # Exercise added to set

    def remove_exercise(self, exercise):
        if exercise in self.exercises:
            self.exercises.remove(exercise)
            print(f"Exercício '{exercise.name}' removido do treino '{self.name}'.") # exercise removed from set
        else:
            print(f"Exercício '{exercise.name}' não encontrado no treino '{self.name}'.") # exercise not found in set

