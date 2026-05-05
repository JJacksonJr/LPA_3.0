import os

from dataclasses import dataclass

os.system("cls")


@dataclass


class Carro:
    nome:str
    modelo:str
    ano:int
    telefone:int
 

    def mostrar_dados(self):
        print(f"Nome do cliente: {self.nome}")
        print(f"modelo do carro do cliente:{self.modelo}")
        print(f"ano do carro do cliente:{self.ano}")
        print(f" Telefone do cliente:{self.telefone}")
        
        
        

lista_De_comprantes=[]



while True:

    pessoa= Carro(
        nome=input("Digite seu nome =").strip(),
        modelo=input("Digite o modelo do seu carro = ").strip(),
        ano=input("Digite o ano do carro = "),
        telefone=input("Digite o seu telefone =")
    )

    lista_De_comprantes.append(pessoa)

    opcao=str(input("Deseja continuar ? s ou n ?")).strip().lower()

    if opcao =="n":
        break


print("")
print("EXIBINDO DADOS DA COMPRA")
print("")

for pessoa in lista_De_comprantes:

    pessoa.mostrar_dados()
