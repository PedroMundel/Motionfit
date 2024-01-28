from entities.user import User

class PersonalTrainer(User):
    def __init__(self, id, name, age, cpf, birth_date, entry_date, username, email, description):
        super().__init__(id, name, age, cpf, birth_date, entry_date, username, email)
        self.description = description
        self.students = []
        self.certificates = []

    def add_user_as_student(self, student):
        self.students.append(student)
        print(f"{student.name} adicionado como aluno ao Personal Trainer {self.name}.") #added as a student of Personal Trainer

    def add_training_to_student(self, student, training):
        if student in self.students:
            student.training = training
            print(f"Treino adicionado a {student.name}.") # Set (of exercises) added to ...
        else:
            print(f"{student.name} não é aluno de {self.name}.") # ... is not a sutend of ...

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"{student.name} removido da lista de alunos do Personal Trainer {self.name}.") #removed from Personal Trainer's student list
        else:
            print(f"{student.name} não é aluno de {self.name}.") # ... is not a student of ...

    def add_certificate(self, certificate):
        self.certificates.append(certificate)
        print(f"Certificado adicionado a {self.name}.") # Certificate added to ...
