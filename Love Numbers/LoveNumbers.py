# ------------------------------
# ❤️ LOVE NUMBERS
# Programa de planejamento financeiro para casais
# ------------------------------

# A palavra-chave "def" serve para DEFINIR uma função
# "cabecalho" é o NOME da função
# Os parênteses () indicam que a função NÃO recebe parâmetros
def cabecalho():
    # print é uma FUNÇÃO que mostra algo na tela
    # "\n" pula uma linha antes do texto
    # O texto entre aspas é exatamente o que será exibido
    print("\n❤️ LOVE NUMBERS - Planejamento Financeiro para Casais\n")


# "def" cria outra função
# "dados_pessoa" é o nome da função
# "numero" é um PARÂMETRO que recebe um valor quando a função é chamada
def dados_pessoa(numero):
    # input pausa o programa e espera o usuário digitar algo
    # f"" permite colocar variáveis dentro do texto usando {}
    nome = input(f"Nome da pessoa {numero}: ")

    # float converte o texto digitado em NÚMERO COM CASA DECIMAL
    # input novamente pede um valor ao usuário
    valor = float(input(f"Quanto {nome} deposita por mês? R$ "))

    # return DEVOLVE um valor para quem chamou a função
    # aqui estamos devolvendo o valor mensal dessa pessoa
    return valor


# Função que pergunta se o casal já tem dinheiro guardado
def perguntar_valor_inicial():
    # input pede uma resposta do usuário
    # .lower() transforma tudo em letra minúscula
    resposta = input("O casal já tem dinheiro guardado? (s/n): ").lower()

    # if significa "SE"
    # verifica se a resposta foi igual a "s"
    if resposta == "s":
        # pede o valor já guardado
        valor = float(input("Quanto o casal já tem guardado? R$ "))
        # retorna esse valor
        return valor

    # else significa "SENÃO"
    else:
        # se não tiver nada guardado, retorna 0
        return 0


# Função para pedir uma data ao usuário
def obter_data(texto):
    # print mostra um texto explicativo
    print(texto)

    # int converte o texto digitado em número inteiro
    ano = int(input("Ano: "))

    # pede o mês como número
    mes = int(input("Mês (1 a 12): "))

    # return devolve uma TUPLA com (ano, mês)
    return ano, mes


# Função que calcula quantos meses existem entre duas datas
def meses_entre(data_inicio, data_fim):
    # data_inicio[0] é o ANO da data inicial
    # data_fim[0] é o ANO da data final
    # multiplicamos por 12 para converter anos em meses
    # data_fim[1] - data_inicio[1] calcula a diferença de meses
    return (data_fim[0] - data_inicio[0]) * 12 + (data_fim[1] - data_inicio[1])


# Função que mostra o menu de opções
def menu():
    # print mostra cada opção disponível
    print("\n1 - Ver saldo mensal")
    print("2 - Ver projeção futura")
    print("3 - Sair")

    # input pede a escolha do usuário
    return input("Opção: ")


# Função principal do programa
def main():
    # chama a função cabecalho
    cabecalho()

    # chama dados_pessoa passando o número 1
    # o valor retornado é guardado em v1
    v1 = dados_pessoa(1)

    # chama dados_pessoa passando o número 2
    # o valor retornado é guardado em v2
    v2 = dados_pessoa(2)

    # soma os valores mensais das duas pessoas
    mensal = v1 + v2

    # pergunta se já existe dinheiro guardado
    valor_guardado = perguntar_valor_inicial()

    # pede a data atual
    data_atual = obter_data("\n📅 Data atual")

    # while True cria um LOOP INFINITO
    # o programa só sai quando usamos "break"
    while True:
        # chama o menu e guarda a opção escolhida
        opcao = menu()

        # SE a opção for "1"
        if opcao == "1":
            # mostra o valor mensal do casal
            print(f"\n💰 Saldo mensal do casal: R$ {mensal:.2f}")
            # mostra o valor já guardado
            print(f"📦 Valor já guardado: R$ {valor_guardado:.2f}")
            # soma tudo para mostrar o TOTAL
            print(f"🧮 Total atual do casal: R$ {mensal + valor_guardado:.2f}")

        # SENÃO SE a opção for "2"
        elif opcao == "2":
            # pede a data futura
            data_futura = obter_data("\n📅 Data futura")

            # calcula quantos meses existem entre as datas
            meses = meses_entre(data_atual, data_futura)

            # verifica se a data é inválida
            if meses <= 0:
                print("\n❌ Data inválida.")

            # se a data for válida
            else:
                # calcula o valor futuro somando o valor guardado
                total_futuro = valor_guardado + (mensal * meses)

                # mostra o resultado
                print(f"\n📊 Em {meses} meses o casal terá: R$ {total_futuro:.2f}")

        # SE a opção for "3"
        elif opcao == "3":
            # mensagem de saída
            print("\n❤️ Até mais!")
            # break encerra o loop
            break

        # SE o usuário digitar algo inválido
        else:
            print("\n❌ Opção inválida.")


# Chamada da função principal
# Sem isso, o programa NÃO EXECUTA
main()
