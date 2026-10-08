import json
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

    if digitado == "0":
           break
       
    if digitado == "1":
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
    elif digitado == "2":

        with open("dados.json", "r", encoding="utf-8") as arquivo:
            inventário = json.load(arquivo)

        if not inventário:
            print("Nenhum paciente cadastrado.")
        else:
            print("===== PACIENTES CADASTRADOS =====")

            for paciente in inventário:
                print(f"\nNome: {paciente['nome']}")
                print(f"CPF: {paciente['cpf']}")
                print(f"Data de nascimento: {paciente['data_de_nascimento']}")
                print(f"Sexo: {paciente['sexo']}")
                print(f"Endereço: {paciente['endereço']}")
                print(f"Telefone: {paciente['telefone']}")
                print(f"Sintomas: {paciente['sintomas']}")

    if digitado == "3":
       print("esta pessoa ficará com Editar")

    if digitado == "4":
      nome_deletar = input("Digite o nome do paciente que deseja deletar: ")

      encontrado = False

      for paciente in inventário:
         if paciente["nome"].lower() == nome_deletar.lower():
               confirmacao = input("Tem certeza que deseja deletar? (S/N): ").strip().upper()

               if confirmacao == "S":
                  inventário.remove(paciente)
                  print("Paciente deletado com sucesso!")
               else:
                  print("Operação cancelada.")

               encontrado = True
               break

    if not encontrado:
        print("Paciente não encontrado.")

    if digitado == "5":
       print("esta pessoa ficará com Pesquisar")

    if digitado == "6":
       print("esta pessoa ficará com Gerar Relatório")

    