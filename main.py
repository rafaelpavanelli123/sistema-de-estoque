nomes = []
quantidades = []
precos = []

def adicionar_produto():
    print("\n--- Adicionar Produto ---")
    nome = input("Nome do produto: ").strip()

    if nome == "":
        print("Nome inválido! Operação cancelada.")
        return

    for n in nomes:
        if n.lower() == nome.lower():
            print(f"O produto '{nome}' já está cadastrado.")
            return

    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço (R$): "))

    if quantidade < 0 or preco < 0:
        print("Quantidade e preço não podem ser negativos.")
        return

    nomes.append(nome)
    quantidades.append(quantidade)
    precos.append(preco)

    print(f"Produto '{nome}' cadastrado com sucesso!")

def listar_produtos():
    print("\n--- Lista de Produtos ---")
    if len(nomes) == 0:
        print("Estoque vazio.")
        return

    print(f"{'#':<4}{'Produto':<20}{'Qtd':<8}{'Preço':<12}{'Subtotal':<12}")
    print("-" * 56)

    valor_total = 0
    for i in range(len(nomes)):
        subtotal = quantidades[i] * precos[i]
        valor_total += subtotal
        print(f"{i+1:<4}{nomes[i]:<20}{quantidades[i]:<8}R$ {precos[i]:<8.2f}R$ {subtotal:<8.2f}")

    print("-" * 56)
    print(f"Valor total em estoque: R$ {valor_total:.2f}")
    print(f"Total de itens (tipos): {len(nomes)}")

def atualizar_quantidade():
    print("\n--- Atualizar Quantidade ---")
    if len(nomes) == 0:
        print("Estoque vazio.")
        return

    nome = input("Nome do produto: ").strip()

    for i in range(len(nomes)):
        if nomes[i].lower() == nome.lower():
            print(f"Quantidade atual de '{nomes[i]}': {quantidades[i]}")
            print("1 - Definir nova quantidade")
            print("2 - Adicionar (entrada)")
            print("3 - Subtrair (saída)")
            opcao = int(input("Opção: "))

            if opcao == 1:
                nova = int(input("Nova quantidade: "))
                if nova < 0:
                    print("Quantidade não pode ser negativa.")
                    return
                quantidades[i] = nova
            elif opcao == 2:
                entrada = int(input("Entrada de quantas unidades? "))
                quantidades[i] += entrada
            elif opcao == 3:
                saida = int(input("Saída de quantas unidades? "))
                if saida > quantidades[i]:
                    print("Saída maior que o estoque atual!")
                    return
                quantidades[i] -= saida
            else:
                print("Opção inválida.")
                return

            print(f"Nova quantidade: {quantidades[i]}")
            return

    print(f"Produto '{nome}' não encontrado.")

def remover_produto():
    print("\n--- Remover Produto ---")
    if len(nomes) == 0:
        print("Estoque vazio.")
        return

    nome = input("Nome do produto: ").strip()

    for i in range(len(nomes)):
        if nomes[i].lower() == nome.lower():
            confirma = input(f"Tem certeza que deseja remover '{nomes[i]}'? (s/n): ").lower()
            if confirma == "s":
                nomes.pop(i)
                quantidades.pop(i)
                precos.pop(i)
                print("Produto removido.")
            else:
                print("Operação cancelada.")
            return

    print(f"Produto '{nome}' não encontrado.")

def buscar_produto():
    print("\n--- Buscar Produto ---")
    if len(nomes) == 0:
        print("Estoque vazio.")
        return

    termo = input("Digite parte do nome: ").strip().lower()
    encontrados = 0

    print()
    for i in range(len(nomes)):
        if termo in nomes[i].lower():
            print(f"-> {nomes[i]} | Qtd: {quantidades[i]} | R$ {precos[i]:.2f}")
            encontrados += 1

    if encontrados == 0:
        print("Nenhum produto encontrado com esse termo.")
    else:
        print(f"\n{encontrados} produto(s) encontrado(s).")

def alerta_estoque_baixo():
    print("\n--- Alerta de Estoque Baixo ---")
    limite = int(input("Mostrar produtos com quantidade abaixo de: "))
    encontrados = 0
    for i in range(len(nomes)):
        if quantidades[i] < limite:
            print(f"!! {nomes[i]} - apenas {quantidades[i]} unidade(s)")
            encontrados += 1
    if encontrados == 0:
        print("Nenhum produto abaixo do limite. Estoque saudável!")

def menu():
    print("\n========================================")
    print("    SISTEMA DE CONTROLE DE ESTOQUE")
    print("========================================")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar quantidade")
    print("4 - Remover produto")
    print("5 - Buscar produto")
    print("6 - Alerta de estoque baixo")
    print("0 - Sair")
    print("========================================")

opcao = -1
while opcao != 0:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        adicionar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        atualizar_quantidade()
    elif opcao == 4:
        remover_produto()
    elif opcao == 5:
        buscar_produto()
    elif opcao == 6:
        alerta_estoque_baixo()
    elif opcao == 0:
        print("\nSaindo do sistema. Até logo!")
    else:
        print("Opção inválida. Tente novamente.")