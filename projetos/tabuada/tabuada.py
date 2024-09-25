valor = int(input("digite o numero da tabuada: "))
i,j = 1,1
for i in range(1,valor+1):
    print(f"tabuada do {i}\n")
    for j in range(1,11):
        print(f"{i} * {j} = ",(i*j))
    print()    