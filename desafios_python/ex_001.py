# 011 - faça um programa que peça a largura e altura de uma párede em metros, calcule sua area e a 
# quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta
#  uma area de 2M / Quadrado


largura = float(input('Informe a Largura da parede: '))
altura = float(input('Informe a Altura da parede: '))

area = largura * altura     # pega os dados das variaveis calcula e atribui a area 
print(f'sua parede possui {largura} x {altura} com a area total de {area}, metros')

tinta = area / 2     # area dividido por 2 saberemos a qtdde de tinta que precisaremos de fato
print(f'Uma parede com essa medida {area}, iremos precisar desta qdtte de tinta {tinta} !')

# utilizei este desafio fazendo um push, para meu repositório.