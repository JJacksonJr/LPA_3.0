import os 

from dataclasses import dataclass

os.system("cls")


@dataclass

class Filme:
    nome:str
    nome_do_filme:str
    classificao:int
    duracao:str
    idade:int


    def mostrar_dados(self):
        print("")
        print("")
        print(f"Nome:{self.nome}")
        print(f"Nome do filme:{self.nome_do_filme}")
        print(f"Duração:{self.duracao}")
        print(f"idade:{self.idade}")


        if self.classificao > self.idade:

            print("Esse Filme é para Maiores de 18 anos")


        else:

            print("Classificação Adequada")





lista_de_informaco_filme=[]


while True:

    cliente=Filme(
        nome=input("Digite seu nome = "),
        nome_do_filme=input("Digite o nome do Filme ="),
        classificao=int(input("Digite a Classificação do filme =")),
        duracao=input("Qual é a duração do filme ? ="),
        idade=int(input("Digite sua idade = "))
                        
    )

    lista_de_informaco_filme.append(cliente)

    opcao=str(input("Deseja continuar adicionando ? s ou n ? =")).strip().lower()

    if opcao =="n":
        break


opcao_2=str(input("Deseja Salvar o Arquivo ? s ou n= ")).strip().lower()

if opcao_2=="s":

    with open("Lista_de_informações.csv","a", encoding="utf-8") as arquivo_de_informacao:

        for cliente in lista_de_informaco_filme:

            arquivo_de_informacao.write(f"{cliente.nome}|{cliente.nome_do_filme}|{cliente.classificao}|{cliente.duracao}|{cliente.idade}\n")

        print("Arquivo Salvo !!!")



opcao_3=str(input("Deseja Exibir os dados ? s ou n ?= ")).strip().lower()

if opcao_3=="s":

    print("")
    print("Exibindo Dados !!!")
    print("")

    for cliente in lista_de_informaco_filme:

        cliente.mostrar_dados()
    