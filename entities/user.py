from datetime import datetime
from entities.shopping_cart import ShoppingCart

class User:
    def __init__(self, id, name, age, cpf, birth_date, entry_date, username, email):
        self.id = id
        self.name = name
        self.age = age
        self.cpf = cpf
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        self.entry_date = datetime.strptime(entry_date, "%Y-%m-%d")
        self.username = username
        self.email = email
        self.logged_in = False
        self.shopping_cart = ShoppingCart() # Inicializa um carrinho de compras

    def add_produto_ao_carrinho(self, produto): #add_product_to_cart
        if(self.logged_in):
            self.shopping_cart.add_produto(produto)
        else :
            print("Usuário precisa estar logado") # user needs to be logged in

    def remover_produto_do_carrinho(self, produto):  # remove_product_from_cart
        if(self.logged_in):
            self.shopping_cart.remover_produto(produto)
        else :
            print("Usuário precisa estar logado") # user needs to be logged in

    def calcular_preco_total_no_carrinho(self): #calculate_cart_total_price
        if(self.logged_in):
            return self.shopping_cart.calcular_preco_total()
        else :
            print("Usuário precisa estar logado") # user needs to be logged in

    def calcular_frete_do_carrinho(self): # calculate delivery fee
        if(self.logged_in):
            return self.shopping_cart.calcular_frete()
        else :
            print("Usuário precisa estar logado") # user needs to be logged in

    def efetuar_compra(self): #make_purchase
        if(self.logged_in):
            return self.shopping_cart.efetuar_compra()
        else :
            print("Usuário precisa estar logado") # user needs to be logged in

    def login(self, user, password):
        if user == self.username and password == "senha.1234": # senha = password
            self.logged_in = True
            print("Login bem-sucedido.") # Logged in successfully
        else:
            print("Credenciais inválidas. Falha no login.") #Invalid credentials. Failed to Log in

    def logout(self):
        self.logged_in = False
        print("Logout bem-sucedido.") # Log out successfull
