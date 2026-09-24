inventário = []
digitado = ""

while digitado != "0":
    print("\n--- Menu ---")
    print("1 - Cadastrar")
    print("2 - Exibir")
    print("3 - Editar")
    print("4 - Deletar")
    print("5 - Pesquisar")
    print("6 - Gerar Relatório")
    print("0 - Sair")

    digitado = input("Escolha alguma opção: ")

    if digitado == "1":
<<<<<<< Updated upstream
        nome = input("Digite o nome completo do paciente: ")
        cpf = input("Digite o CPF do paciente: ")
        data_de_nascimento = input("Digite a data de nascimento do paciente: ")
        while True:
            sexo = input("Digite o sexo do paciente (M ou F): ").strip().upper()
            if sexo in ["M", "F"]:
                break  
            print("Por favor, digite apenas 'M' para Masculino ou 'F' para Feminino.")
        endereço = input("Digite o endereço do paciente: ")
        telefone = input("Digite o telefone do paciente: ")
        sintomas = input("Digite os sintomas do paciente: ")
        
        paciente = {
            "nome": nome,
            "cpf": cpf,
            "data_de_nascimento": data_de_nascimento,
            "sexo": sexo,
            "endereço": endereço,
            "telefone": telefone,
            "sintomas": sintomas
        }
        
        inventário.append(paciente)
        print(f"\n Paciente {nome} cadastrado com sucesso!")
        
=======
       print("Digite o nome completo do paciente: ")
       print("Digite o CPF do paciente: ")
       print("Digite a data de nascimento do paciente: ")
       print("Digite o sexo do paciente: ")
       print("Digite o endereço do paciente: ")
       print("Digite telefone para contato: ")
       print("Digite os sintomas do paciente: ")

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
   
>>>>>>> Stashed changes
