palavra = input("digite uma palavra: ")
letra = input("digite a letra que deseja ver a frequência: ")

i,cont = 0,0
for i in range(len(palavra)):
    if palavra[i] == letra:
        cont+=1

print(f"a palavra tem {len(palavra)} letras, e tem como frequencia a letra '{letra}', {cont} vezes")

