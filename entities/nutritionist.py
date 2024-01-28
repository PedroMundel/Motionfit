from entities.user import User


class Nutritionist(User):
    def __init__(self, id, name, age, cpf, birth_date, entry_date, username, email, description):
        super().__init__(id, name, age, cpf, birth_date, entry_date, username, email)
        self.description = description
        self.patients = []
        self.certificates = []

    def add_user_as_patient(self, patient):
        self.patients.append(patient)
        print(f"{patient.name} adicionado como paciente à Nutricionista {self.name}.") #added as a patient to the nutritionist

    def add_diet_to_patient(self, patient, diet):
        if patient in self.patients:
            patient.diet = diet
            print(f"Dieta adicionada a {patient.name}.") # diet added to ...
        else:
            print(f"{patient.name} não é paciente de {self.name}.") # is not a patient

    def remove_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
            print(f"{patient.name} removido da lista de pacientes da Nutricionista {self.name}.") #removed from Nutritionist list of patients
        else:
            print(f"{patient.name} não é paciente de {self.name}.") # is not a patient of ...

    def add_certificate(self, certificate):
        self.certificates.append(certificate)
        print(f"Certificado adicionado à Nutricionista {self.name}.") # certificate added to Nutritionist
