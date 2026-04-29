import os 

os.system("cls")



def calculo_do_volume_esfera(raio):

    formula_do_volume_esfera= 4/3 * (3.14 * (raio**3))

    return formula_do_volume_esfera










raio=int(input("Digite o valor do raio de uma esfera = "))

reposta_do_volume=calculo_do_volume_esfera(raio)

print(f"O VOLUME DA ESFERA É DE: {reposta_do_volume}")