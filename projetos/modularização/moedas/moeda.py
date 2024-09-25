def aumentar(valor,tax,formatado):
    valor += valor * tax
    return verifica_formato(valor,formatado)

def diminuir(valor,tax,formatado):
    valor -= valor * tax
    return verifica_formato(valor,formatado)

def dobro(valor,formatado):
    valor *= 2
    return verifica_formato(valor,formatado)

def metade(valor,formatado):
    valor /=2
    return verifica_formato(valor,formatado)

def moeda(valor):
    return "{:.2f}".format(valor) #retorna 2 casas depois do ponto decimal

def verifica_formato(valor,formatado):
    if formatado:
        return "R$ " + moeda(valor)
    else:
        return valor

def verifica_moeda(valor):
    if valor is not str(valor):
        return str(valor).replace(".","").isnumeric()
    else:
        return False

def receber_valor(msg):
    valor = input(msg)
    return float(valor.replace(",","."))




