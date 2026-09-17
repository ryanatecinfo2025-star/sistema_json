
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
            nome = input("Digite o nome completo do paciente: ")
            cpf = input("Digite o cpf do paciente: ")
            data_de_nascimento = input("Digite a data de nascimento do paciente: ")
            sexo = input("Digite o sexo do paciente (M ou F): ")
            endereço = input("Digite o endereço do paciente: ")
            telefone = input("Digite os sintomas do paciente: ")
            sintomas = input("Digite os sintomas do paciente: ")
      paciente = {
         "nome": nome,
         "cpf": cpf,
         "data_de_nascimento": data_de_nascimento
         "sexo": sexo
         "endereço": endereço,
         "telefone": telefone,
         "sintomas": sintomas,
      }


      #salvar o paciente no arquivo json
      #verificar erros (se o sexo digitado é M ou F)
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
   