from entities.certificate import Certificate, EducationLevel
from entities.common_user import CommonUser
from entities.exercise import Exercise
from entities.muscle import MuscleRegion
from entities.nutritionist import Nutritionist
from entities.personal_trainer import PersonalTrainer
from entities.product import Product
from entities.training import Training
from entities.user import User


class Main:
    def __init__(self):
        pass

    def executa(self):
        usuario_comum = CommonUser(
            "1",
            "Ana",
            25,
            "123.456.789-00",
            "1998-05-15",
            "2022-01-01",
            "ana123",
            "ana@email.com"
        )

        usuario_comum.login("ana123", "senha.1234")

        # Adicionando treinos ao usuário comum - adding sets to common user
        treino1 = Training("Treino Cardio")  # cardio set
        treino2 = Training("Treino de Força") # strenght set

        usuario_comum.adicionar_treino(treino1)
        usuario_comum.adicionar_treino(treino2)

        # Realizando um treino - performing a set
        usuario_comum.realizar_treino() # common_user.perform_set()

        # Iniciando análise de treino por IA - Initializing AI training analysis
        usuario_comum.iniciar_analise_de_treino_por_ia() # common_user.initialize_ai_training_analysis

        # Exibindo informações - showing info
        print(f"Nome do usuário comum: {usuario_comum.name}") # Common user name:
        print("Treinos do usuário comum:") # Common user set:
        for treino in usuario_comum.treinos:
            print(f"  - {treino.name}")

        # Criando produtos - creating products
        produto1 = Product("1", "Camiseta", 25.0)
        produto2 = Product("2", "Calça Jeans", 50.0)

        # Adicionando produtos ao carrinho do usuário comum - adding products to cart
        usuario_comum.add_produto_ao_carrinho(produto1)
        usuario_comum.add_produto_ao_carrinho(produto2)

        # Exibindo produtos no carrinho - showing products in cart
        print("Produtos no carrinho:")
        for produto in usuario_comum.shopping_cart.produtos:
            print(f"  - {produto.nome} - R${produto.preco:.2f}")

        # Calculando o preço total no carrinho - calculating final price on cart
        total_no_carrinho = usuario_comum.calcular_preco_total_no_carrinho()
        print(f"Preço total no carrinho: R${total_no_carrinho:.2f}") # Cart total price

        # Calculando o frete do carrinho - calculating delivery fee
        frete_do_carrinho = usuario_comum.calcular_frete_do_carrinho()
        print(f"Custo do frete: R${frete_do_carrinho:.2f}") # Delivery fee

        # Efetuando a compra
        usuario_comum.efetuar_compra()

# Executando a classe Main - executing Main class
if __name__ == "__main__":
    main = Main()
    main.executa()
