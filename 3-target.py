import json

# buscando dados json
with open('dados.json', encoding='utf-8') as dados_json:
    dados = json.load(dados_json)

# verificando o menor valor
for i in dados:
    if i['valor'] < 400:
        if i['valor'] > 1:
            print('Menor valor = ', i['valor'], ', no dia: ', i['dia'])

# verificando o valor maior
for i in dados:
    if i['valor'] > 48000:
        print('Maior valor = ', i['valor'], ', no dia: ', i['dia'])

# verificando total + média
total = sum(x['valor'] for x in dados)
media = total / 30
print('A média é de : ', media)

# faturamento mensal
for i in dados:
    if i['valor'] > 14605:
        print('Os dias', i['dia'],'com o valor de:', i['valor'], 'são superiores à média!')
