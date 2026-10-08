def editar(dados):
    print("\n EDITAR PACIENTE ")

    cpf_busca = input("Digite o CPF do paciente que deseja editar: ").strip()

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

            salvar_dados(dados)
            print("Dados do paciente atualizados com sucesso!")
            return

    print("Paciente não encontrado!")