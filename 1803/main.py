def exibir_menu():
    print("Bem vindo ao menu de Cadastro")
    print("1 - Novo Cadastro")
    print("2 - Ver Cadastro")
    print("3 - Sair") 
    print("-----------------------------------") 
def cadastrar_pessoa (cadastros):    
    nome = input("nome:")
    idade = input ("idade:")
    turma = input ("turma:")
    curso = input ("curso:")
    cadastros.append({"Nome": nome, "idade": idade, "turma": turma, "curso": curso})
    print("Cadastro realizado com sucesso!")
