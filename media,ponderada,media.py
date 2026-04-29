import os 

os.system("cls")


def calculando_média_aritmética(notas):

    soma_total=0

    media=0

    soma_total=sum(notas)

    media= soma_total / 3

    return media



def calculando_média_ponderada(notas,pesos):

    soma_total=0

    soma_total=sum(notas)

    pesos_total=sum(pesos)

    media_ponderada= soma_total/ pesos_total

    return media_ponderada








lista_3_notas=[]

peso_notas=[]


for i in range(1,4,1):

    nota_do_aluno=int(input(f"Digite sua {i+0} nota ")) 

    lista_3_notas.append(nota_do_aluno)

    pesos=int(input(f"Digite o peso da {i+0} "))

    peso_notas.append(pesos)

while True:

    opcao_letras=int(input(" Escolha umas das letras 1= A=media ari, 2= P=ponderada ou 3= média harmônica "))


    match opcao_letras:

        case 1:

            print("A")

            reposta_A=calculando_média_aritmética(lista_3_notas)

            print("")

            print(f"A MÉDIA É DE: {reposta_A}")

        case 2:
            print("P")

            reposta_p=calculando_média_ponderada(lista_3_notas,peso_notas)

            print("")

            print(f" A MÉDIA PONDERADA É DE: {reposta_p}")


