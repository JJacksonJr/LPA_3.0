import os


from dataclasses import dataclass

os.system("cls")


@dataclass

class Funcionario:
    nome:str
    cargo:str 
    salario:float

    def mostrando_dados(self):
        print("")
        print(f"Nome do funcionario:{self.nome}")
        print(f"cargo do funcionario: {self.cargo}")
        print(f"salario do funcionario:{self.salario}")
        print("")

        aumento= self.salario * 0.10

        salario_com_aumento= self.salario + aumento
        print("")
        print(f"Aumento:{aumento}")
        print(f"Salario com aumento:{salario_com_aumento}")
        print("")




lista_De_funcionario=[]


while True:

    funcionario=Funcionario(
        nome=input("Digite seu nome= ").strip(),
        cargo=input("Digite seu cargo =").strip(),
        salario=float(input("Digite seu salário ="))
    )

    lista_De_funcionario.append(funcionario)

    opcao=str(input("Deseja continuar ? s ou n ?")).strip().lower()

    if opcao=="n":
        break

print("")
print("EXIBINDO DADOS DO FUNCIONARIO")
print("")
for funcionario in lista_De_funcionario:

    funcionario.mostrando_dados()