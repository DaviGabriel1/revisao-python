import prop as p
from moedas import moeda as m
# from prop import fatorial

valor = p.fatorial(5)
print(valor)

valor = m.receber_valor("digite um valor: ")

print(m.dobro(valor,True))
print(m.metade(valor,True))
print(m.aumentar(valor,0.25,False))
print(m.diminuir(valor,0.25,True))
print(m.moeda(valor))
print(m.verifica_moeda(120.9))