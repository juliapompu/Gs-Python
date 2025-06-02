# --------------------------------------------------------------
# Nome: Julia Souza Pompeu - RM: 561955
# Nome: Giovana Rosatti Parreira - RM: 562275
# Projeto: S.O.S Enchentes- Sistema de Monitoramento e Alerta de Enchentes
# --------------------------------------------------------------

# Dados imaginarios para o programa funcionar
regioes = ["Centro", "Norte", "Sul", "Leste", "Oeste"]
nivel_rios = [2.5, 3.0, 4.2, 1.8, 3.5] 
chuvas = [50, 80, 120, 40, 100] 

# Exibe o menu principal
def exibir_menu():
    print("\n----S.O.S Enchentes aqui para te ajudar!----")
    print("\n----Sistema de Monitoramento de Enchentes---")
    print("1 - Verificar situação de uma região")
    print("2 - Atualizar dados de uma região")
    print("3 - Relatório geral de risco")
    print("4 - Sair")

# Função para calcular o nível de risco baseado em rio e chuva
def calcular_risco(nivel_rio, chuva):
    if nivel_rio >= 4 or chuva >= 100:
        return "ALTO"
    elif nivel_rio >= 3 or chuva >= 70:
        return "MÉDIO"
    else:
        return "BAIXO"

# Função para exibir situação de uma região
def verificar_regiao():
    print("\nRegiões disponíveis:")
    for i, r in enumerate(regioes):
        print(f"{i + 1} - {r}")
    try:
        escolha = int(input("Escolha a região (número): "))
        if 1 <= escolha <= len(regioes):
            indice = escolha - 1
            risco = calcular_risco(nivel_rios[indice], chuvas[indice])
            print(f"\nRegião: {regioes[indice]}")
            print(f"Nível do Rio: {nivel_rios[indice]} metros")
            print(f"Chuva nas últimas 24h: {chuvas[indice]} mm")
            print(f"** Nível de Risco: {risco} **")
        else:
            print("Opção inválida! Região não existe.")
    except ValueError:
        print("Entrada inválida! Digite um número.")

# Função que atualiza os dados quando você atualiza
def atualizar_dados():
    print("\nRegiões disponíveis para atualizar:")
    for i, r in enumerate(regioes):
        print(f"{i + 1} - {r}")
    try:
        escolha = int(input("Escolha a região (número): "))
        if 1 <= escolha <= len(regioes):
            indice = escolha - 1
            novo_nivel = float(input("Informe o novo nível do rio (em metros): "))
            nova_chuva = float(input("Informe a quantidade de chuva nas últimas 24h (em mm): "))
          
            if novo_nivel < 0 or nova_chuva < 0:
                print("Valores inválidos! Não podem ser negativos.")
                return
            
            nivel_rios[indice] = novo_nivel
            chuvas[indice] = nova_chuva
            print("Dados atualizados com sucesso!")
        else:
            print("Opção inválida! Região não existe.")
    except ValueError:
        print("Entrada inválida! Utilize apenas números.")

# Função para mostra o relatorio geral
def relatorio_geral():
    print("\n===== Relatório Geral de Risco =====")
    for i in range(len(regioes)):
        risco = calcular_risco(nivel_rios[i], chuvas[i])
        print(f"Região: {regioes[i]}")
        print(f"  -> Nível do Rio: {nivel_rios[i]} metros")
        print(f"  -> Chuva: {chuvas[i]} mm")
        print(f"  -> Nível de Risco: {risco}\n")

# Programa principal
def main():
    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                verificar_regiao()
            elif opcao == 2:
                atualizar_dados()
            elif opcao == 3:
                relatorio_geral()
            elif opcao == 4:
                print("Saindo do sistema. Fique seguro!")
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número.")

main()
