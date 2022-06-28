n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1

if (n==1) or (n==2):
    print("Esse número não pertence à sequencia")
else:
    for count in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(f'Esse número pertence à sequência, termo: {termo}')