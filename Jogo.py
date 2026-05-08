import os 

from dataclasses import dataclass

os.system("cls")

@dataclass


class Jogo:
    nome:str
    nome_do_jogo:str
    genero:str
    preco:float


    def mostrar_dados(self):
        print("")
        print(f"Nome:{self.nome}")
        print(f"Nome do jogo:{self.nome_do_jogo}")
        print(f"Gênero do jogo:{self.genero}")
        print(f"Preço do jogo:{self.preco}")


        if self.preco >=200:
            print("Jogo Caro !!")

        else:

            print(f"Jogo Barato!!!")




lista_de_informaco_jogo=[]


while True:

    print("1: CADASTRAR INFORMAÇÕES")
    print("2: SALVAR O ARQUIVO ")
    print("3: MOSTRAR DADOS ")   

    print("")
    opcao=int(input("ESCOLHA A SUA OPÇÃO !! ="))


    match opcao :

        case 1:
            print("")
            print("CADASTRANDO INFORMAÇÕES !! ")

            cliente=Jogo(
                nome=input("Digite Seu Nome = ").strip(),
                nome_do_jogo=input("Digite O Nome do Seu Jogo =").strip(),
                genero=input("Digite o Gênero Do Jogo =").strip(),
                preco=float(input("Digite O Preço do seu jogo ="))

            )

            lista_de_informaco_jogo.append(cliente)

            opcao_1=str(input("Deseja continuar cadastrando ? s ou n ? =")).strip().lower()

            if opcao_1=="n":
                continue

            print("")
            print("INFORMAÇÕES CADASTRADAS !!!")


        case 2:
            print("")
            print("SALVAR ARQUIVO")

            opcao_2=str(input("Deseja Salvar o arquivo do cadastro ? s ou n ? = ")).strip().lower()

            if opcao_2=="s":

                with open("Lista_De_informações_do_jogo.csv","a",encoding="utf-8") as arquivo_de_informacao:

                    for cliente in lista_de_informaco_jogo:

                        arquivo_de_informacao.write(f"Nome do comprador:{cliente.nome}\n Nome do filme:{cliente.nome_do_jogo}\n Gênero do jogo: {cliente.genero}\n Preço do jogo:{cliente.preco}")
                    print("")
                    arquivo_de_informacao.write(f"Nome do comprador:{cliente.nome}\n Nome do filme:{cliente.nome_do_jogo}\n Gênero do jogo: {cliente.genero}\n Preço do jogo:{cliente.preco}")
                    print("ARQUIVO SALVO COM SUCESSO !!!")


        case  3:

            print("")
            print("EXIBIR DADOS ")

            opcao_4=str(input("Deseja Exibir os dados ? s ou n ? =")).strip().lower()

            if opcao_4=="s":

                for cliente in lista_de_informaco_jogo:

                    cliente.mostrar_dados()
            print("")
            print("DADOS COM SUCESSO !!")
            
