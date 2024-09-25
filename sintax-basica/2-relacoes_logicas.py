print(True+True)
print(False+True)
print(not False+ (not False))
print(True+True)
print(not True+(not True))
print(True*8)
print(6//4) # arredonda

boo = True and False
or_boo = True or False # _ é snake case

print(boo)
print(boo or or_boo)
print("----------")
#bool() --> 0 vazio ou nenhum valor será falso, o resto é verdadeiro
print(bool())
print(bool([]))
print(bool(0))
print(bool(-6))
print(-5 or 0) # retorna o valor verdadeiro, diferente do bool q retorna v ou f

print(1 == 2)
print(1<=2)
print(1<2 and 2<3)
print(1<2<3)# diferente do java, é possivel colocar mais de um valor na condicional