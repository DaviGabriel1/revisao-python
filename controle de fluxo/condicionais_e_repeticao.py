############## IF ##############
valor = 7
if valor > 7:
    print("maior que 7")
elif valor < 7:
    print("menor que 7")
else:
    print("igual a 7")     


############## FOR ################
for animal in ["cachorro","gato","rato"]:
    print("{} é um animal".format(animal))   

for i in range(5):
    print(i)  

print("==================================")
for i in range(5,8):
    print(i)   

print("==================================")
for i in range (0,11,2): # (inicio,fim, passos)
    print(i)

print("==================================")

animais = ["cachorro","gato","rato"]
for i,value in enumerate(animais):
    print(i,value)

print("==================================")
x = 0
while x<11:
    print(x)
    x+=1    

########### TRATAMENTO DE EXCEÇÃO ####################
#
#       TODO
#

############ Iterator #################


um_dict = {"one": 1,"two":2,"three":3,"four":4}

indices = um_dict.keys()
iterator = iter(indices)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) ERRO
# for i in iterator:
#    print(i)

print(list(iterator))

ite = iter(indices)
for i in ite:
    print(i)

print(list(ite))

for i in indices:
    print(i)

print(indices)    
