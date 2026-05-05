import os 

from dataclasses import dataclass

os.system("cls")


@dataclass

class Aluno:
    nome:str
    idade:str
    nota1:int
    nota2:int

    def condicao(self):

        print("")
        print("")
        print(f"Nome: {self.nome}")
        print(f"idade: {self.idade}")
        print(f"nota1: {self.nota1}")
        print(f"nota2: {self.nota2}")
        media=(self.nota1 + self.nota2) / 2
        print(f"media:{media}")
        print("")
        print("")
        if media >=7:
            print("Aprovado")

        else:
            print("Reprovado")

        



lista_De_notas_dos_alunos=[]


while  True:

    aluno=Aluno(
        nome=input("Digite seu nome =").strip(),
        idade=input("Digite sua idade= "),
        nota1=float(input("Digite sua nota =")),
        nota2=float(input("Digite sua segunda nota= "))
    )

    lista_De_notas_dos_alunos.append(aluno)

    opcao=str(input("Deseja continaur ? s ou n ? ")).strip()

    if opcao =="n":
        break


print("")
print("EXIBINDO DADOS DO ALUNO")
print("")

for aluno in lista_De_notas_dos_alunos:

    aluno.condicao()