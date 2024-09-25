import sys
def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def divisao(a,b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError as zero_error:
        print("erro ao dividir por zero: ", zero_error.__class__)
        return 0
    else:      
        return result     
    
def multiplicacao(a,b):
    return a * b        

def exponenciacao(a,b):
    return a ** b

def radiciacao(a , b):
    return "{:.2f}".format(a ** (1/b))

def leia_int(msg):
    try:
        valor = int(input(msg)) 
    except ValueError as erro_valor:
        print("o usuario não digitou nenhum numero: ",erro_valor.__class__)    
        sys.exit(0)
    else:
        return valor 
    finally:
        print("função finalizada")       





