def somar_numeros(x,y):
    return x+y

    # def somar_numeros(x=4,y=3): outra forma de fazer
    # return x+y

z = somar_numeros(3,7)
print(z)


def varios_argumentos(*varargs):
    return varargs

print(varios_argumentos(1,1,1,2,3,4,5,6))

def exibir_dicts(**kwargs): # permite passar argumentos chave e valor como dicionarios
    for chave,valor in kwargs.items(): # iteração desses argumentos
        print(f'{chave} : {valor}')

exibir_dicts(nome='davi',idade=19,altura=1.82)

dict_itens = {}
def args_dicts(*varargs,**kwargs):
    print(varargs)
    for chave,valor in kwargs.items():
        dict_itens.setdefault(chave,valor)

args_dicts(1,2,3,4,5,nome='davi',idade=19,altura=1.82)
print(dict_itens)



def args_dicts_print(*varargs,**kwargs):
    print(varargs)
    print(kwargs)

args = (1,2,3,4,5)
kwargs = {"Pais":"Brasil","Estado":"São Paulo","Cidade":"Itapevi"}

args_dicts_print(*args,**kwargs) #é necessários desenpacotar o args e o kwargs, no args usasse o metodo do turples, e o kwargs é do dicionario


def criar_hello_world(nome): # função de primeira classe
    def hello_world():
        return f"{nome}, está dizendo hello world!"
    return hello_world    

ola = criar_hello_world("Davi") # atribuindo a função hello_world() ao objeto
print(ola())      

def criar_media():
    total = 0
    cont = 0
    def media(n):
        nonlocal total, cont
        total+=n
        cont+=1
        return total/cont
    return media

med = criar_media()
print(med(2))
print(med(8))
print(med(3))
print(med(5))

print((lambda x: x>=5)(5)) #true
print((lambda x,y: x**2+y*2)(1,2)) # 5

print(list(filter(lambda x: x>2,[1,2,3,4,5]))) #[3,4,5]

