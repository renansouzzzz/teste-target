# valores
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

# valor total
totalValor = sp + rj + mg + es + outros

# percentual
sp_percent = sp * 0.12
rj_percent = rj * 0.12
mg_percent = mg * 0.07
es_percent = es * 0.12
out_percent = outros * 0.10

#total percentual
totalPercent = sp_percent + rj_percent + mg_percent + es_percent + out_percent

# total + percentual
total = totalValor - totalPercent

print(f'O valor abatido de percentual no valor total de {totalValor} é de: {total}')


