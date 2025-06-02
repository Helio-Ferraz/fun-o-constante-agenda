


print("Lista de contatos:")

lista = ["Guilherme" , "Analise" , "Caio", "Danilo", "luan", "Pedro"]
Ações = 5 
while Ações != 0:
    Ações = int(input("O que você quer fazer? \n [1] - Cadastrar pessoas \n [2] - Listar pessoas \n [3] - Excluir_pessoas \n [0] - Sair \n"))
    
    if Ações == 1:
        Adicionamento = input("Qual contato você quer adicionar?")
        lista.append(Adicionamento)
        print("Contato adicionado com sucesso!")       
    elif Ações == 2:
        print(lista)       
    elif Ações == 3:
        Removimento = input("Qual contato você quer remover?")
        lista.remove(Removimento)
        print("Contato removido com sucesso!")
    elif Ações == 0:
        print("Fechado com Sucesso!")
