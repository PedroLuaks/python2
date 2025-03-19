def exibir_menu():
    print("Bem vindo ao Menu de Cadastro")
    print("1 - Novo Cadastro")
    print("2 - Ver Cadastro")
    print("3 - Sair") 
    print("-----------------------------------") 

def cadastrar_pessoa (cadastros):    
    nome = input("Nome:")
    idade = input ("Idade:")
    turma = input ("Turma:")
    curso = input ("Curso:")
    cadastros.append({ "Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso})
    print("Cadastro realizado com sucesso!")

def ver_cadastros (cadastros):
    if not cadastros:
        print ("Nenhum cadastro no sistema")
    else:
        print("\n ------ LISTA DE CADASTROS ------")
        
        for i, pessoa in enumerate (cadastros, 1):
          print(f"{i} . nome: {pessoa['Nome']}, idade:  {pessoa['Idade']}, turma: {pessoa['Turma']}, curso: {pessoa['Curso']}")

def main():
    cadastros = []
    while True:
        exibir_menu ()
        opção = input("escolha uma opcção:")
        if opção == "1": 
            cadastrar_pessoa (cadastros)
        elif opção == "2":
            ver_cadastros (cadastros)    
        elif opção == "3":
            print ("Obrigado por utilizar o sistema")
            break

        else:
            print("Opção inexistente, tente novamente")    

if __name__ == "_main_":
    main()            
