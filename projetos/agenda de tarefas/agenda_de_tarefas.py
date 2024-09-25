lista_tarefas = []


def criar_tarefa(titulo,descricao,data):
    lista = {}
    lista.setdefault("titulo",titulo)
    lista.setdefault("descricao",descricao)
    lista.setdefault("data",data)
    lista_tarefas.append(lista)
    

def ler_tarefa():
    i = 0
    for i in range(len(lista_tarefas)):
        print(i,"- ",lista_tarefas[i])

def atualizar_tarefa(posicao,titulo,descricao,data): 
    lista_tarefas[posicao].update({"titulo":titulo,"descricao":descricao,"data":data})

def deletar_tarefa(index):
        lista_tarefas.pop(index)

flag = False
while not flag:
    opcao = int(input("digite a opcao que deseja: \n[1] CRIAR TAREFA\n[2]ATUALIZAR TAREFA\n[3]LER TAREFA\n[4]DELETAR TAREFA\n[5]SAIR"))
    if opcao == 1:
        titulo = input("digite o titulo da tarefa: ")
        descricao = input("faça uma descrição para a tarefa: ")
        data = input("digite a data de vencimento da tarefa: ")
        criar_tarefa(titulo,descricao,data)
    elif opcao == 2:
        posicao = int(input("digite o id da tarefa que deseja atualizar: "))
        titulo = input("digite o titulo da tarefa: ")
        descricao = input("faça uma descrição para a tarefa: ")
        data = input("digite a data de vencimento da tarefa: ")
        atualizar_tarefa(posicao,titulo,descricao,data)
        print("*atualizado com sucesso*")

    elif opcao == 3:
        ler_tarefa() 
    elif opcao == 4:
        index = int(input("digite o id da tarefa que deseja deletar: "))
        deletar_tarefa(index)
        print("*deletado com sucesso*")
    elif opcao == 5:
        flag = True
        print("*finalizando o sistema*")
    else:
        print("opcao invalida, tente novamente")                   

