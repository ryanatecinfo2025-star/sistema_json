import json
inventário = []
digitado = 0

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
        cpf_busca = input("Digite o CPF do paciente que deseja editar: ").strip()
       
        #buscar o paciente no arquivo json baseado no cpdf_busca
        #o que o arquivo encontrar, salvar em dados

        for paciente in dados:
            if paciente["cpf"] == cpf_busca:

                novo_nome = input(f"Novo nome ({paciente['nome']}): ").strip()
                novo_cpf = input(f"Novo CPF ({paciente['cpf']}): ").strip()
                nova_data = input(f"Nova data de nascimento ({paciente['data_de_nascimento']}): ").strip()
                novo_sexo = input(f"Novo sexo ({paciente['sexo']}): ").strip()
                novo_endereco = input(f"Novo endereço ({paciente['endereço']}): ").strip()
                novo_telefone = input(f"Novo telefone ({paciente['telefone']}): ").strip()
                novos_sintomas = input(f"Novos sintomas ({paciente['sintomas']}): ").strip()

                if novo_nome:
                    paciente['nome'] = novo_nome
                if novo_cpf:
                    paciente['cpf'] = novo_cpf
                if nova_data:
                    paciente['data_de_nascimento'] = nova_data
                if novo_sexo:
                    paciente['sexo'] = novo_sexo
                if novo_endereco:
                    paciente['endereço'] = novo_endereco
                if novo_telefone:
                    paciente['telefone'] = novo_telefone
                if novos_sintomas:
                    paciente['sintomas'] = novos_sintomas

                #salvar as alterações no arquivo json
                print("Dados do paciente atualizados com sucesso!")
        
                print("Paciente não encontrado!")

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
        print("\n PESQUISAR PACIENTE ")
if digitado == "6":
    print("\n===== RELATÓRIO DE PACIENTES =====")

    if len(inventário) == 0:
        print("Nenhum paciente cadastrado.")
    else:
        print(f"Total de pacientes cadastrados: {len(inventário)}")

        for i, paciente in enumerate(inventário, start=1):
            print(f"\n--- Paciente {i} ---")
            print(f"Nome: {paciente['nome']}")
            print(f"CPF: {paciente['cpf']}")
            print(f"Data de nascimento: {paciente['data_de_nascimento']}")
            print(f"Sexo: {paciente['sexo']}")
            print(f"Endereço: {paciente['endereço']}")
            print(f"Telefone: {paciente['telefone']}")
            print(f"Sintomas: {paciente['sintomas']}")
    