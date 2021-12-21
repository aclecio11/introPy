# 1 - imports/ bibliotecas
import math

# 2 - Classes

# 3 - Métodos(não tem retorno) e funções(tem retorno)
# def - definition = definição

def calcular_area_do_triangulo(B, h):
    return (B * h)/2

def calcular_area_do_retangulo(B, h):
    return B * h

def calcular_area_do_quadrado(l):
    return l**2

def contador_progressivo(fim):
     for numero in range (fim): #repetir o bloco do zero até o numero passado
         print(numero)


def apoiar_candidato(nome, vezes):
    for numero in range(vezes):

         if numero < 9:
             print(f'000{numero+ 1} - {nome}')
         elif numero < 99:
             print(f'00{numero + 1} - {nome}')
         elif numero < 999:
             print(f'0{numero + 1} - {nome}')
         else:
            print(f'{numero+1} - {nome}')

def bricar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
         print('PLIM!')
        else:
             print('{:0>3}'.format(numero))


if __name__ == '__main__':

# chamar a função de calculo do triangulo:
    area = calcular_area_do_triangulo(8, 10)
    print(f'A area do triangulo é: {area} m²')

# chamar a função de calculo do retangulo:
    area = calcular_area_do_retangulo(8, 10)
    print(f'A area do retangulo é: {area} m²')

# chamar a função de calculo do quadrado:
    area = calcular_area_do_quadrado(8)
    print(f'A area do quadrado é: {area} m²')

# chamar a função contagem:
    contador_progressivo(10)

# chamar a função apoiar candidato:
    apoiar_candidato('Fake', 100)

#chamar a função:
    bricar_de_plim(100)


