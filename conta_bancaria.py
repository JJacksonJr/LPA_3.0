import os 

from dataclasses import dataclass

os.system("cls")

@dataclass

class Bancario:

    titular:str
    saldo:float

    def mostrar_dados(self):

        print("")
        print("")
        print(f"Titular:{self.titular}")
        print(f"Saldo::{self.saldo}")

        if self.saldo <0:

            print("Saldo Negativo")

        else:

            print("Saldo positivo")
    









lsita_de_clientes=[]


while True:

    os.system("cls")

    cliente=Bancario(
        titular=input("Digite o nome do titular = "),
        saldo=float(input("Digite o seu saldo = "))
    )

    lsita_de_clientes.append(cliente)


    opcao_1=str(input("Deseja continuar ? s ou n  w")).strip().lower()

    if opcao_1 =="n":

        break


opcao_2=str(input("Deseja Salvar o Arquivo ? s ou n ? ")).strip().lower()

if opcao_2 =="s":
    
    with open("Lista_de_Cliente.csv","a") as arquivos:
        
        for cliente in lsita_de_clientes:
            
            arquivos.write(f"{cliente.titular}|{cliente.saldo}\n")

            
        print("Arquivo salvo!!")


opcao_3=str(input("Deseja exibir dados ?  s ou n ?")).strip().lower()

if opcao_3=="s":
    
    for cliente in lsita_de_clientes:
        
        cliente.mostrar_dados()