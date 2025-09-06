import json
academico = ""
operacao = ""

# modularização:
def menuprincipal():
    print("\n**** SISTEMA PUC ****\n")
    print(f'''---- MENU PRINCIPAL -----\n
              {[1]} Gerenciar estudantes
              {[2]} Gerenciar professores
              {[3]} Gerenciar disciplinas
              {[4]} Gerenciar turmas
              {[5]} Gerenciar matrículas
              {[6]} Sair\n''')

def menuoperacoes():
    print(f'''\n***** [{academico}] MENU DE OPERAÇÕES: *****
                {[1]} Incluir
                {[2]} Listar
                {[3]} Atualizar
                {[4]} Excluir
                {[5]} Voltar ao menu principal\n''')

def incluir(tipoAcademico):

    if tipoAcademico == "estudantes":
        while True:
            # Validação de dados:
            try:
                codigo = int(input("Digite o código do estudante: "))
                dados = recuperarArquivo("arqEstudantes.json")
                for estudante_existente in dados:
                    if estudante_existente.get("codigo") == codigo:
                        raise ValueError("O código já existe, tente novamente\n")

                nome = input("Digite o nome do estudante: ")
                cpf = str(input("Digite o CPF do estudante: "))
                if len(cpf) != 11:
                    raise ValueError("O CPF deve ter 11 dígitos numéricos, tente novamente!\n")
                estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}

            # Salvar Json:
                dados.append(estudante)
                salvarArquivo(dados, "arqEstudantes.json")
                print("Estudante cadastrado com sucesso!\n")
                if input("Deseja incluir um novo estudante (s/n): ") == "n":
                    break
            except ValueError as e:
                print(f"\nErro: {e}\n")

    elif tipoAcademico == "professores":
        while True:
            # Validação de dados - verificar se o código do professor já existe:
            try:
                codigo = int(input("Digite o código do professor: "))
                dados = recuperarArquivo("arqProfessores.json")
                for professor_existente in dados:
                    if professor_existente.get("codigo") == codigo:
                        raise ValueError("O código já existe, tente novamente\n")

                nome = input("Digite o nome do professor: ")
                cpf = str(input("Digite o CPF do professor: "))
                if len(cpf) != 11:
                    raise ValueError("O CPF deve ter 11 dígitos numéricos, tente novamente!\n")
                professor = {"codigo": codigo, "nome": nome, "cpf": cpf}

                # Salvar Json:
                dados.append(professor)
                salvarArquivo(dados, "arqProfessores.json")
                print("Professor cadastrado com sucesso!\n")
                if input("Deseja incluir um novo professor (s/n): ") == "n":
                    break
            except ValueError as e:
                print(f"\nErro: {e}\n")

    elif tipoAcademico == "disciplinas":
        while True:
            # validação de dados - verificar se o código da disciplina já existe:
            try:
                codigo = int(input("Digite o código da disciplina: "))
                dados = recuperarArquivo("arqDisciplinas.json")
                for disciplina_existente in dados:
                    if disciplina_existente.get("codigo") == codigo:
                        raise ValueError("O código já existe, tente novamente\n")

                nome = input("Digite o nome da disciplina: ")

                disciplina = {"codigo": codigo, "nome": nome}

                # salvar no json
                dados.append(disciplina)
                salvarArquivo(dados, "arqDisciplinas.json")
                print("Disciplina cadastrada com sucesso!\n")
                if input("Deseja incluir uma nova disciplina (s/n): ") == "n":
                    break
            except ValueError as e:
                print(f"\nErro: {e}\n")

    elif tipoAcademico == "turmas":
        while True:
            # Validação de dados - verificar se o código da turma já existe:
            try:
                codigo = int(input("Digite o código da turma: "))
                dados = recuperarArquivo("arqTurmas.json")
                for turma_existente in dados:
                    if turma_existente.get("codigo") == codigo:
                        raise ValueError("O código já existe, tente novamente\n")

                else:
                    professor = int(input("Digite o código do professor: "))
                    professores = recuperarArquivo("arqProfessores.json")
                    if professor not in [p.get("codigo") for p in professores]:
                        print("\nO professor não está cadastrado no sistema\n")
                        continue

                    disciplina = int(input("Digite o código da disciplina: "))
                    disciplinas = recuperarArquivo("arqDisciplinas.json")
                    if disciplina not in [d.get("codigo") for d in disciplinas]:
                        print("\nA disciplina não está cadastrada no sistema\n")
                        continue

                    turma = {"codigo": codigo, "disciplina": disciplina, "professor": professor}
                    # salvar no json
                    dados.append(turma)
                    salvarArquivo(dados, "arqTurmas.json")
                    print("\nTurma cadastrada com sucesso!\n")
                    if input("Deseja incluir uma nova turma (s/n): ") == "n":
                        break
            except ValueError as e:
                print(f"\nErro: {e}\n")

    elif tipoAcademico == "matriculas":
        while True:
            # Validação de dados - verificar se o código da matrícula já existe:
            try:
                codigo = int(input("Digite o código da matrícula: "))
                dados = recuperarArquivo("arqMatriculas.json")
                for matricula_existente in dados:
                    if matricula_existente.get("codigo") == codigo:
                        raise ValueError("O código já existe, tente novamente\n")
                else:
                    turma = int(input("Digite o código da turma: "))
                    turmas = recuperarArquivo("arqTurmas.json")
                    if turma not in [t.get("codigo") for t in turmas]:
                        print("\nA turma não está cadastrada no sistema\n")
                        continue

                    estudante = int(input("Digite o código do estudante: "))
                    estudantes = recuperarArquivo("arqEstudantes.json")
                    if estudante not in [e.get("codigo") for e in estudantes]:
                        print("\nO estudantes não está cadastrado no sistema\n")
                        continue

                matricula = {"codigo": codigo, "turma": turma, "estudante": estudante}

                # salvar no json
                matriculas = recuperarArquivo("arqMatriculas.json")
                matriculas.append(matricula)
                salvarArquivo(matriculas, "arqMatriculas.json")
                print("Matrícula cadastrada com sucesso!\n")
                if input("Deseja incluir uma nova matrícula (s/n): ") == "n":
                    break
            except ValueError as e:
                print(f"\nErro: {e}\n")

def listar(tipoAcademico):

    if tipoAcademico == "estudantes":
        dados = recuperarArquivo("arqEstudantes.json")
        if len(dados) < 1:
            print("Não há estudantes cadastrados\n")
        else:
            for estudante in dados:
                print("Código: {} / Estudante: {} / CPF: {}\n".format(estudante["codigo"], estudante["nome"], estudante["cpf"]))

    elif tipoAcademico == "professores":
        dados = recuperarArquivo("arqProfessores.json")
        if len(dados) < 1:
            print("Não há professores cadastrados\n")
        else:
            for professor in dados:
                print("Código: {} / Professor: {} / CPF: {}\n".format(professor["codigo"], professor["nome"], professor["cpf"]))

    elif tipoAcademico == "disciplinas":
        dados = recuperarArquivo("arqDisciplinas.json")
        if len(dados) < 1:
            print("Não há disciplinas cadastradas\n")
        else:
            for disciplina in dados:
                print("Código: {} / Disciplina: {}\n".format(disciplina["codigo"], disciplina["nome"]))

    elif tipoAcademico == "turmas":
        dados = recuperarArquivo("arqTurmas.json")
        if len(dados) < 1:
            print("Não há turmas cadastradas\n")
        else:
            for turma in dados:
                print("Código: {} / Disciplina: {} / Professor: {}\n".format(turma["codigo"], turma["disciplina"], turma["professor"]))

    elif tipoAcademico == "matriculas":
        dados = recuperarArquivo("arqMatriculas.json")
        if len(dados) < 1:
            print("Não há matrículas cadastradas\n")
        else:
            for matricula in dados:
                print("Código: {} / Turma: {} / Estudante: {}\n".format(matricula["codigo"], matricula["turma"], matricula["estudante"]))
def atualizar(tipoAcademico):

    if tipoAcademico == "estudantes":
        try:
            dados = recuperarArquivo("arqEstudantes.json")
            entradacod = int(input("Digite o código do estudante para atualização: "))
            achou = False 
            for estudante in dados:
                if estudante["codigo"] == entradacod:
                    print("\nEstudante encontrado! Atualize os dados:\n")
                    codigo = int(input("Digite o código do estudante: "))
                    nome = input("Digite o nome do estudante: ")
                    cpf = str(input("Digite o CPF do estudante: "))
                    if len(cpf) != 11:
                        raise ValueError("O CPF deve ter 11 dígitos numéricos, tente novamente!\n")
                    # editar:
                    estudante["codigo"] = codigo
                    estudante["nome"] = nome
                    estudante["cpf"] = cpf
                    print(f"\nDados do estudante {nome} atualizados com sucesso!")
                    achou = True
                    break
            if not achou:
                print("\n* Estudante não encontrado, informe o código correto *\n")
            else:
                salvarArquivo(dados, "arqEstudantes.json")
        except ValueError as e:
            print(f"{e}")

    elif tipoAcademico == "professores":
        try:
            dados = recuperarArquivo("arqProfessores.json")
            entradacod = int(input("Digite o código do professor para atualização: "))
            achou = False 
            for professor in dados:
                if professor["codigo"] == entradacod:
                    print("\nProfessor encontrado! Atualize os dados:\n")
                    codigo = int(input("Digite o código do professor: "))
                    nome = input("Digite o nome do professor: ")
                    cpf = str(input("Digite o CPF do professor: "))
                    if len(cpf) != 11:
                        raise ValueError("O CPF deve ter 11 dígitos numéricos, tente novamente!\n")
                    # editar:
                    professor["codigo"] = codigo
                    professor["nome"] = nome
                    professor["cpf"] = cpf
                    print(f"\nDados do professor {nome} atualizados com sucesso!")
                    achou = True
                    break
            if not achou:
                print("\n* Professor não encontrado, informe o código correto *\n")
            else:
                salvarArquivo(dados, "arqProfessores.json")
        except ValueError as e:
            print(f"{e}")

    elif tipoAcademico == "disciplinas":
        try:
            dados = recuperarArquivo("arqDisciplinas.json")
            entradacod = int(input("Digite o código da disciplina para atualização: "))
            achou = False
            for disciplina in dados:
                if disciplina["codigo"] == entradacod:
                    print("\nDisciplina encontrada! Atualize os dados:\n")
                    codigo = int(input("Digite o código da disciplina: "))
                    nome = input("Digite o nome da disciplina: ")
                    # editar:
                    disciplina["codigo"] = codigo
                    disciplina["nome"] = nome
                    print(f"\nDados da disciplina {nome} atualizados com sucesso!")
                    achou = True
                    break
            if not achou:
                print("\n* Disciplina não encontrada, informe o código correto *\n")
            else:
                salvarArquivo(dados, "arqDisciplinas.json")
        except ValueError as e:
            print(f"{e}")

    elif tipoAcademico == "turmas":
        try:
            dados = recuperarArquivo("arqTurmas.json")
            entradacodigo = int(input("Digite o código da turma para atualização: "))
            achou = False
            for turma in dados:
                if turma["codigo"] == entradacodigo:
                    print("\nTurma encontrada! Atualize os dados:\n")

                    codigo = int(input("Digite o código da turma: "))

                    # validação de dados para disciplina e professor:
                    disciplina = int(input("Digite o código da disciplina ministrada: "))
                    disciplinas = recuperarArquivo("arqDisciplinas.json")
                    if disciplina not in [d.get("codigo") for d in disciplinas]:
                        print("\nA disciplina não está cadastrada no sistema\n")
                        continue

                    professor = int(input("Digite o código do professor responsável: "))
                    professores = recuperarArquivo("arqProfessores.json")
                    if professor not in [p.get("codigo") for p in professores]:
                        print("\nO professor não está cadastrado no sistema\n")
                        continue

                    # editar:
                    turma["codigo"] = codigo
                    turma["disciplina"] = disciplina
                    turma["professor"] = professor
                    print(f"\nDados da turma {codigo} atualizados com sucesso!")
                    achou = True
                    break
            if not achou:
                print("\n* Turma não encontrada, informe o código correto *\n")
            else:
                salvarArquivo(dados, "arqTurmas.json")
        except ValueError as e:
            print(f"{e}")

    elif tipoAcademico == "matriculas":
        try:
            dados = recuperarArquivo("arqMatriculas.json")
            entradacodigo = int(input("Digite o código da matrícula para atualização: "))
            achou = False  # método flag
            for matricula in dados:
                if matricula["codigo"] == entradacodigo:
                    print("\nMatrícula encontrada! Atualize os dados:\n")

                    codigo = int(input("Digite o código da matricula: "))

                    # validação de dados para turma e estudante:
                    turma = int(input("Digite o código da turma: "))
                    turmas = recuperarArquivo("arqTurmas.json")
                    if turma not in [t.get("codigo") for t in turmas]:
                        print("\nA turma não está cadastrada no sistema\n")
                        continue

                    estudante = int(input("Digite o código do estudante: "))
                    estudantes = recuperarArquivo("arqEstudantes.json")
                    if estudante not in [e.get("codigo") for e in estudantes]:
                        print("\nO estudante não está cadastrado no sistema\n")
                        continue

                    # editar:
                    matricula["codigo"] = codigo
                    matricula["turma"] = turma
                    matricula["estudante"] = estudante
                    print(f"\nDados da matrícula {codigo} atualizados com sucesso!")
                    achou = True
                    break
            if not achou:
                print("\n* Matrícula não encontrada, informe o código correto *\n")
            else:
                salvarArquivo(dados, "arqMatriculas.json")
        except ValueError as e:
            print(f"{e}")

def excluir(tipoAcademico):

    if tipoAcademico == "estudantes":
        try:
            dados = recuperarArquivo("arqEstudantes.json")
            entradacod = int(input("Digite o código do estudante para exclusão: "))
            achou = False
            for estudante in dados:
                if estudante["codigo"] == entradacod:
                    print("\nEstudante encontrado! Excluindo...\n")
                    dados.remove(estudante)
                    achou = True
                    break
            if not achou:
                print("\n* Estudante não encontrado, informe o código correto para exclusão *\n")
            else:
                salvarArquivo(dados, "arqEstudantes.json")
        except ValueError as e:
            print(f"{e}")

    elif tipoAcademico == "professores":
        try:
            dados = recuperarArquivo("arqProfessores.json")
            entradacod = int(input("Digite o código do professor para exclusão: "))
            achou = False  # método flag
            for professor in dados:
                if professor["codigo"] == entradacod:
                    print("\nProfessor encontrado! Excluindo...\n")
                    dados.remove(professor)
                    achou = True
                    break
            if not achou:
                print("\n* Professor não encontrado, informe o código correto para exclusão *\n")
            else:
                salvarArquivo(dados, "arqProfessores.json")
        except ValueError as e:
            print(f"{e}")

    elif tipoAcademico == "disciplinas":
        try:
            dados = recuperarArquivo("arqDisciplinas.json")
            entradacod = int(input("Digite o código da disciplina para exclusão: "))
            achou = False 
            for disciplina in dados:
                if disciplina["codigo"] == entradacod:
                    print("\nDisciplina encontrada! Excluindo...\n")
                    dados.remove(disciplina)
                    achou = True
                    break
            if not achou:
                print("\n* Disciplina não encontrada, informe o código correto para exclusão *\n")
            else:
                salvarArquivo(dados, "arqDisciplinas.json")
        except ValueError as e:
            print(f"{e}")

    elif tipoAcademico == "turmas":
        try:
            dados = recuperarArquivo("arqTurmas.json")
            entradacod = int(input("Digite o código da turma para exclusão: "))
            achou = False
            for turma in dados:
                if turma["codigo"] == entradacod:
                    print("\nTurma encontrada! Excluindo...\n")
                    dados.remove(turma)
                    achou = True
                    break
            if not achou:
                print("\n* Turma não encontrada, informe o código correto para exclusão *\n")
            else:
                salvarArquivo(dados, "arqTurmas.json")
        except ValueError as e:
            print(f"{e}")

    elif tipoAcademico == "matriculas":
        try:
            dados = recuperarArquivo("arqMatriculas.json")
            entradacod = int(input("Digite o código da matrícula para exclusão: "))
            achou = False 
            for matricula in dados:
                if matricula["codigo"] == entradacod:
                    print("\nMatrícula encontrada! Excluindo...\n")
                    dados.remove(matricula)
                    achou = True
                    break
            if not achou:
                print("\n* Matrícula não encontrada, informe o código correto para exclusão *\n")
            else:
                salvarArquivo(dados, "arqMatriculas.json")
        except ValueError as e:
            print(f"{e}")

# recuperação e salvamento de arquivos:

def recuperarArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = []
    return dados

def salvarArquivo(dados, nomeArquivo):
    with open(nomeArquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False)
        arquivo.close()

# --- INÍCIO DA APLICAÇÃO ---
# definição das opções de dados acadêmicos (ac) no menu principal (MP)
ac = 0

# loop do MP:
while ac != 6:
    try:
        # mostrar MP, pedir ac
        menuprincipal()
        ac = int(input("Informe a ação desejada: "))

        # encerrar aplicação
        if ac == 6:
            print("Finalizando aplicação...")
            break

        # personalizar menu de operações (MO)
        elif ac == 1:
            academico = "ESTUDANTES"
        elif ac == 2:
            academico = "PROFESSORES"
        elif ac == 3:
            academico = "DISCIPLINAS"
        elif ac == 4:
            academico = "TURMAS"
        elif ac == 5:
            academico = "MATRÍCULAS"

        else:
            print("\nDigite uma entrada válida!\n")
            continue

        # mostrar / interagir com o MO
        while True:
            menuoperacoes()
            op = int(input("Informe a operação desejada: "))

            # INCLUIR
            if op == 1:
                operacao = "INCLUSÃO"
                print(f"\n===== {operacao} =====\n")

                # chamar função INCLUIR
                if ac == 1:
                    incluir("estudantes")

                elif ac == 2:
                    incluir("professores")

                elif ac == 3:
                    incluir("disciplinas")

                elif ac == 4:
                    incluir("turmas")

                elif ac == 5:
                    incluir("matriculas")
                continue

            # LISTAR
            elif op == 2:
                operacao = "LISTAR"
                print(f"\n===== {operacao} =====\n")

                # chamar função LISTAR
                if ac == 1:
                    listar("estudantes")

                elif ac == 2:
                    listar("professores")

                elif ac == 3:
                    listar("disciplinas")

                elif ac == 4:
                    listar("turmas")

                elif ac == 5:
                    listar("matriculas")
                continue

            # ATUALIZAR
            elif op == 3:
                operacao = "ATUALIZAÇÃO"
                print(F"\n===== {operacao} =====\n")

                # chamar função ATUALIZAR
                if ac == 1:
                    atualizar("estudantes")

                elif ac == 2:
                    atualizar("professores")

                elif ac == 3:
                    atualizar("disciplinas")

                elif ac == 4:
                    atualizar("turmas")

                elif ac == 5:
                    atualizar("matriculas")
                continue

            # EXCLUIR
            elif op == 4:
                operacao = "EXCLUSÃO"
                print(F"\n===== {operacao} =====\n")

                # chamar função EXCLUIR
                if ac == 1:
                    excluir("estudantes")

                elif ac == 2:
                    excluir("professores")

                elif ac == 3:
                    excluir("disciplinas")

                elif ac == 4:
                    excluir("turmas")

                elif ac == 5:
                    excluir("matriculas")
                continue

            # VOLTAR AO MP
            else:
                if op == 5:
                    break

    except ValueError:
        print("\nDigite uma entrada válida!\n")