from ast import List
from entities.training import Training
from entities.user import User

class CommonUser(User):
    def __init__(self, id, name, age, cpf, birth_date, entry_date, username, email):
        super().__init__(id, name, age, cpf, birth_date, entry_date, username, email)
        self.treinos: List[Training] = []

    def adicionar_treino(self, treino): #def add set
        if self.logged_in:
            self.treinos.append(treino)
            print(f"Treino '{treino.name}' adicionado ao usuário comum {self.name}.") # transaltes to: Set (exercises) added to common user
        else:
            print("Faça o login primeiro.") # Login First

    def realizar_treino(self): #def perform training (set of exercises)
        if self.logged_in:
            print(f"Realizando treino para o usuário comum {self.name}...") # performing set for common user
            # Lógica para realizar um treino
        else:
            print("Faça o login primeiro.") # Login first

    def iniciar_analise_de_treino_por_ia(self): #def initialize AI training (a tool that keeps an eye on your execution technique whilst you're doing an exercise)
        if self.logged_in:
            print(f"Iniciando análise de treino por IA para o usuário comum {self.name}...") # Initializing the AI Training Analysis for common user
            # Lógica para iniciar a análise de treino por IA - Logic to initialize the AI support
        else:
            print("Faça o login primeiro.") # Login First
