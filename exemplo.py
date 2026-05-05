import os 

from dataclasses import dataclass

os.system("cls")


@dataclass

class Fornecedor:
    nome:str
    email:str
    telefone:str
    endereco:str

    def mostrar_dados(self):
        if self.nome =="meuca":
            
            print("oieeee")

print("SOLICITANDO DADOS DO FORNECEDOR")

fornecedor=Fornecedor(

nome=input("Digite seu Nome="),
email=input("Digite seu email ="),
telefone=input("Digite seu telefone="),
endereco=input("Digite seu endereço=")

)


print("EXIBINDO DADOS DO FORNECEDOR")

fornecedor.mostrar_dados()