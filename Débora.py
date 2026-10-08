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

   elif digitado == "2":
      print("esta pessoa ficará com Exibir")

   elif digitado == "3":
      print("esta pessoa ficará com Editar")

   elif digitado == "4":
      nome_deletar = input("Digite o nome do paciente que deseja deletar: ")

      encontrado = False

      #Abrir o arquivo dados.json para carregar os usuarios existentes e salvar na lista inventário
      with open("dados.json", "r", encoding="utf-8") as arquivo:
          inventário = json.load(arquivo)

      for paciente in inventário:
         if paciente["nome"].lower() == nome_deletar.lower():
               confirmacao = input("Tem certeza que deseja deletar? (S/N): ").strip().upper()

               if confirmacao == "S":
                  inventário.remove(paciente)
                  print("Paciente deletado com sucesso!")

                  #salvar novamente o arquivo json com a lista atualizada
                  with open("dados.json", "w", encoding="utf-8") as arquivo:
                      json.dump(inventário, arquivo, ensure_ascii=False, indent=4)

               else:
                  print("Operação cancelada.")

               encontrado = True
               break

    if not encontrado:
        print("Paciente não encontrado.")

   elif digitado == "5":
      print("\n pesquisar paciente")

      nome_pesquisar = input("Digite o nome do paciente que deseja pesquisar: ")
      encontrado = False

      #Abrir o arquivo dados.json para carregar os usuarios existentes e salvar na lista dados
      with open("dados.json", "r", encoding="utf-8") as arquivo:
          dados = json.load(arquivo)

      for paciente in dados:
         if paciente["nome"].lower() == nome_pesquisar.lower():
            print("\nPaciente encontrado!")
            print("Nome:", paciente["nome"])
            print("CPF:", paciente["cpf"])
            print("Data de nascimento:", paciente["data_de_nascimento"])
            print("Sexo:", paciente["sexo"])
            print("Endereço:", paciente["endereço"])
            print("Telefone:", paciente["telefone"])
            print("Sintomas:", paciente["sintomas"])

            encontrado = True
            break


      if not encontrado:
         print("Paciente não encontrado.")


   elif digitado == "6":
      print("esta pessoa ficará com Gerar Relatório")

   if digitado == "0":
      break
   
>>>>>>> Stashed changes
