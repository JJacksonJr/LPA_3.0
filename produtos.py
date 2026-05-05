import os

from dataclasses import dataclass

os.system("cls")

@dataclass#evita variavel se repetir


class Produto:
    nome:str
    preco:float
    quantidade:int


    def mostrar_dados(self):
        print("")
        print(f"Nome do produto:{self.nome}")
        print(f"Preço do produto:{self.preco}")
        print(f"Quantidade do produto:{self.quantidade}")
        valor_total=self.preco * self.quantidade
        print(f"valor total: {valor_total}")
        print("")


lista_De_produtos=[]

while True:

    produto=Produto(
        nome=input("Digite o nome do produto =").strip(),
        preco=float(input("Digite o valor do produto =")),
        quantidade=int(input("Digite a quantidade de produto ="))
    )

    lista_De_produtos.append(produto)

    opcao=str(input("Deseja continuar ? s ou n ? ")).strip()

    if opcao =="n":
        break

print("")
print("EXIBINDO DADOS")
print("")


for produto in lista_De_produtos:

    produto.mostrar_dados()