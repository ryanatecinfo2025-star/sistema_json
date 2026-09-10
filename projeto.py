
inventário = []
digitado = 0
while digitado !=6:
    print("Menu")
    print("1 - Cadastrar")
    print("2 - Exibir")
    print("3 - Editar")
    print("4 - Deletar")
    print("5 - Pesquisar")
    print("6 - Gerar Relatório")
    print("0 - sair")

    digitado = input("escolha alguma opçâo")

    if digitado == "1":
       print("esta pessoa ficará com cadastro")

    if digitado == "2":
         print("esta pessoa ficará com Exibir")

    if digitado == "3":
       print("esta pessoa ficará com Editar")

    if digitado == "4":
       print("esta pessoa ficará com Deletar")

    if digitado == "5":
       print("esta pessoa ficará com Pesquisar")

    if digitado == "6":
       print("esta pessoa ficará com Gerar Relatório")

    if digitado == "0":
       break
   