def exibir_menu(): 
    sumario = """
    ============= MENU =============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Novo Usuário
    [c] Nova Conta
    [l] Listar Contas
    [f] Finalizar
    ================================
    => """
    return input(sumario).strip()
    

def depositar(saldo, extrato, /):
    
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"\n✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\n❌ Valor inválido!")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, saques, limite_saques):

    if valor > saldo:
        print("\n❌ Saldo insuficiente.")

    elif valor > limite:
        print("\n❌ O valor para saque excede o limite de R$500,00.")

    elif saques >= limite_saques:
        print(f"\n❌ Você já realizou o número máximo de {limite_saques} saques.")

    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques += 1
        print("\n✅ Saque realizado com sucesso!")

    else:
        print("\n❌ Valor inválido. Por favor, tente novamente.")

    return(saldo, extrato, saques)



def exibir_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO ===============")
    if extrato:
        for item in extrato:
            print(item)
    else:
        print("Nenhuma movimentação registrada.")
    print(f"Saldo: R$ {saldo:.2f}")
    print("=======================================")



def criar_usuario(usuarios):
    cpf = input("Por favor, informe seu CPF (somente números): ").strip()

    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("\n❌ Já existe um usuário com esse CPF!")
        return
    
    nome = input("Nome Completo: ").strip()
    data_nascimento = input("Data de Nascimento (dd/mm/AAAA): ").strip()
    logradouro = input("Logradouro: ").strip()
    numero = input("Número: ").strip()
    bairro = input("Bairro: ").strip()
    cidade_estado = input("Cidade/Sigla do Estado: ").strip()

    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereço": f"{logradouro}, {numero} - {bairro} - {cidade_estado}"
    })

    print(f"\n✅ Usuário {nome} cadastrado com sucesso, seja bem vinda(o)!")



def criar_conta(usuarios, contas, agencia, numero_conta):

    cpf = input("Informe o CPF (apenas números) do titular da conta: ").strip()

    usuario = None
    for novo_usuario in usuarios:
        if novo_usuario ["cpf"] == cpf:
            usuario = novo_usuario
            break

    if usuario:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
        print("\n✅ Conta criada com sucesso!")
        return numero_conta + 1
    
    else:
        print("\n❌ Usuário não encontrado. Por favor, cadastre-se no nosso sistema.")
        return numero_conta
        


def listar_contas(contas):
    print("\n================ CONTAS ================")
    for conta in contas:
        print(f"Titular: {conta['usuario']['nome']} \n Agência: {conta['agencia']} | Conta: {conta['numero_conta']}\n")
    print("========================================")


def main():
    saldo = 0
    limite = 500
    extrato = []
    saques = 0
    limite_saques = 3

    agencia = "0001"
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
            

        elif opcao == "s":
            valor = float(input("Por favor, informe o valor para saque: "))
           
            saldo, extrato, saques = sacar(
                saldo = saldo, 
                valor = valor,
                extrato = extrato, 
                limite = limite, 
                saques = saques, 
                limite_saques = limite_saques,
            )
                                
        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = criar_conta(usuarios, contas, agencia, numero_conta)
            
        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "f":
            print("\n✅ Serviço finalizado. Obrigado por usar o sistema!")
            break

        else:
            print("\n❌ Opção inválida!")

main()
