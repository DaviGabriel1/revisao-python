import manager as m


flag = True

while flag:
    opcao = int(input("digite uma opcao: \n[1]LER ARQUIVO\n[2]ADICIONAR USUARIO\n[3]SAIR"))
    if opcao == 1:
        m.listar_usuarios()
    elif opcao == 2:
        nome = input("digite o nome do usuario: ")
        idade = input("digite a idade do usuario: ")
        m.cadastrar_usuario(nome,idade)
    elif opcao == 3:
        flag = False 
    else:
        print('opção invalida! tente novamente')    


