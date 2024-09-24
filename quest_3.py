import json

with open("dados.json") as arquivo:
    valor = json.load(arquivo)
dia = 0
maior_valor = 0
menor_valor = 0
soma = 0
dias_contados = 0
media_geral = 0
media_maior = 0

while dia < 3:
    if maior_valor < valor[dia]["valor"]:
        maior_valor = valor[dia]["valor"]  
    if menor_valor == 0:
        menor_valor = valor[dia]["valor"]
    elif valor[dia]["valor"] == 0:
        menor_valor = menor_valor
    elif valor[dia]["valor"] < menor_valor:
        menor_valor = valor[dia]["valor"]
    if valor[dia]["valor"] > 0:
        soma = soma + valor[dia]["valor"]
        dias_contados = dias_contados + 1
        media_geral = soma / dias_contados
    dia = dia + 1

dia = 0

while dia < 3:
    if valor[dia]["valor"] > media_geral:
        media_maior = media_maior + 1
    dia = dia + 1


print(f"""
O maior valor faturado foi de {maior_valor}
O menor valor faturado foi de {menor_valor}
A média faturada foi de {media_geral}, e {media_maior} dias tiveram seu faturamento maior que a média""")








