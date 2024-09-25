def cadastrar_usuario(nome,idade):
    with open("menu.txt","a") as arquivo:
        arquivo.write(nome)
        arquivo.write(",")
        arquivo.write(idade)
        arquivo.write("\n")
        arquivo.close()
        print(f"usuario {nome},cadastrado com sucesso!")

def listar_usuarios(): 
    try:
        with open("menu.txt","r") as arquivo:
            lista = arquivo.readlines()
            for item in lista:
                item = item.split(",")
                item[1] = item[1].replace("\n","")
                print(f"{item[0]:<30}{item[1]:>3} anos")
    except FileNotFoundError as file_error:
        print("arquivo não encontrado! ",file_error.__class__)          
    finally:
        arquivo.close()          

