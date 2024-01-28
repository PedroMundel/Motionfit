# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.preco_total = 0.0 #total value
        self.custo_do_frete = 0.0 # delivery fee
        self.produtos = [] # products

    def add_produto(self, produto): #add product
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao carrinho.") #Product ... added to cart

    def remover_produto(self, produto): # def remove product
        if produto in self.produtos:
            self.produtos.remove(produto)
            print(f"Produto '{produto.nome}' removido do carrinho.") #product ... removed from cart
        else:
            print(f"Produto '{produto.nome}' não encontrado no carrinho.") # Product ... not found in cart

    def calcular_preco_total(self): #def calculate total price
        self.preco_total = sum(produto.preco for produto in self.produtos)
        return self.preco_total

    def calcular_frete(self): # calculate delivery fee
        # Lógica para calcular o custo do frete
        # Aqui, uma simplificação: 10% do preço total - simplifying: 10% of total value
        self.custo_do_frete = 0.1 * self.preco_total
        return self.custo_do_frete

    def efetuar_compra(self): # make purchase
        total_com_frete = self.preco_total + self.custo_do_frete
        print(f"Compra efetuada! Total a pagar: R${total_com_frete:.2f}") #Purchase made! Total payable:
        # Lógica adicional, como atualizar o estoque, processar pagamento, etc. - this section is not implemented
        return True
