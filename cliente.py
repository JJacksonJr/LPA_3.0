import os 

from dataclasses import dataclass

os.system("cls")


@dataclass

class Cliente:

    nome:str
    idade:str
    telefone:str
    email:str


    def mostrar_dados(self):
        
        print("")
        print(f"Nome do cliente: {self.nome}")
        print(f"idade do cliente: {self.idade}")
        print(f"Telefone do cliente: {self.telefone}")
        print(f"email do cliente: {self.email}")
        print("")





lista_De_clientes=[]


while True:

    clientes=Cliente(

        nome=input("Digite o seu nome ="),

        idade=input("Digite sua idade = "),

        telefone=input("Digite o seu telefone de contado ="),

        email=input("Digite seu email de contato =")
    )

    lista_De_clientes.append(clientes)

    opcao=str(input("Deseja continuar s ou n ?")).strip().lower()

    if opcao =="n":

        break


    


print("EXIBINDO DADOS DOS CLIENTES")
print("")

for clientes in lista_De_clientes:

    clientes.mostrar_dados()