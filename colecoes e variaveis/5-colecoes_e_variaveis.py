result = input("digite um valor:")
print(result)

# não há declarações no python, apenas atribuições

print("ola" if 1<0 else "mundo")

li = []
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.pop() # retirou o ultimo item (4)
li.append(4)

print(li[2]) # retorna 2
print(li[-1]) # retorna o ultimo item
print(len(li))
print(li[0:2])
print(li[1:])
print(li[:3])
print(li[::2]) # lê valores de casas pares
print(li[::-1]) # lê na ordem inversa

li2 = li[:] # li2 recebe os valores de li,mas li2 is li é falso
del li[3] # indica a posição que deve ser deletada
print(li)
li.append(4)
print(li)
li.remove(3) #indica o VALOR que deve ser deletado
print(li)
li.insert(2,3) #(indice,valor) que deve ser inserido
print(li)
print(li.index(3)) # index() retorna o primeiro indice com o valor no parametro

print(1 in li) # verdadeiro se tiver o valor 1 na lista

other_li = [5,6,7,8,9]
# li += other_li
print(li)
li.extend(other_li) # mais eficiente que a soma de listas, já que não é necessário criar uma nova lista
print(li)
tup = (1,2,3) # tuples são como listas mas imutavéis
# tup[0] = 1 é erro
print(type((1,2)))

print(len(tup))       # => 3
tup = tup + (4, 5, 6)  # é possivel adicionar mais elementos no tuples
print(tup[:2])         
print(2 in tup)
print(tup,"\n")
a,b,c = (1,2,3) # é possivel desenpacotar tuples em variaveis 
print(f"a: {a},b: {b},c: {c}")
a,*b,c = (1,2,3,4,5)
print(f"a: {a},b: {b},c: {c}")
d,e,f = 4,5,6
print(f"d: {d},e: {e},f: {f}")
d,e = e,d
print(f"d: {d},e: {e},f: {f}\n")
dict_vazio = {}
dict_cheia = {"one":1,"two":2,"three":3}
dict_valida = {(1,2,3):[1,2,3]}
print(dict_cheia["one"])
print(list(dict_cheia.keys()))
print(dict_cheia.keys())
print(list(dict_cheia.values()))

print("one" in dict_cheia) # buscar apenas as chaves, não valores
print(1 in dict_cheia)

print(dict_cheia.get("one"))
print(dict_cheia.get("one", 4)) #suporta um argumento para retorno caso a chave não exista
print(dict_cheia.get("four", 4))
print(dict_cheia)
print(dict_cheia.setdefault("three",7))
print(dict_cheia.setdefault("four",5)) #setdefault, se existir essa chave, retorna o valor relacionado, caso contrário, criará a chave com o valor do segundo parametro
print(dict_cheia)

# adicionar no dicionario (2 formas)
dict_cheia.update({"four":4}) 
dict_cheia["four"] = 4

""" formas de desempacotar dicionarios em dicionarios
{"a": 1, **{"b": 2}}  # => {'a': 1, 'b': 2}
{"a": 1, **{"a": 2}}  # => {'a': 2}
"""

set_vazio = set()
algum_set = {1,1,2,2,3,4} #sem elemento repetido
print(algum_set)
outro_set = algum_set
outro_set.add(5)
print(outro_set)

inter_set = {3,4,5,6}

#interseccao de sets
print(outro_set & inter_set)

#uniao de sets
print(outro_set | inter_set)

#diferença entre dicionarios
print({1,2,3,4,5} - {3,4,5})

# mostra termos que não estão nas 2 listas ao mesmo tempo
print({1,3,5,7} ^ {1,2,3,4,5,6,7})

# verifica se o set de comparação está contido ou se é igual ao outro
print({1,2,3} >= {1,2}) # true
print({1,2,3} <= {1,2}) # false

#verifica a existencia de um item no set
print(2 in outro_set) # true
print(10 in outro_set)#false

#copia o set em outro, mas o is verifica falso
copia_set = outro_set.copy()
print(copia_set is outro_set)