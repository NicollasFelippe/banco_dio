saldo = 0.00
extrato = []
numero_de_depositos = 0
numero_de_saques = 0
opcao = ["D","E","S",'X']


while True:
  menu = input("""
    Usuário informe a opção que você deseja utilizar:
          [D] - Deposito
          [S] - Saque
          [E] - Extrato
          [X] - Sair \n
            """).upper()

  if menu not in opcao:
    print("Opcao invalida")
    menu = input("""
    Usuário informe a opção que você deseja utilizar:
          [D] - Deposito
          [S] - Saque
          [E] - Extrato
          [X] - Sair \n
            """).upper()

  if menu == 'D':
    valor_deposito = float(input("Informe o valor que deseja depositar:"))
    if valor_deposito <= 0:
      valor_deposito = float(input("Você não pode informar um valor negativo\n Informe o valor que deseja depositar:\n"))
    else:
      numero_de_depositos += 1
      extrato.append (f'deposito de numero {numero_de_depositos} - R${valor_deposito}\n')
      saldo += valor_deposito
      print(f'deposito de numero {numero_de_depositos} - R${valor_deposito} efetuado com sucesso\n')

  if menu == 'S':
    saque = float(input('Informe o valor que deseja sacar:\n '))
    if numero_de_saques >= 3:
      print('Você já excedeu o numeros de saques diários. \n Opreção encerrada')
    elif saque > saldo:
      print(f'Não será possível sacar este valor R${saque}, pois seu saldo insuficiente. \n Valor do saldo R$:{saldo}')
    elif saque > 500:
      print(f'Você só pode sacar até R$ 500,00 \n operação encerrada')
    else:
      saldo -= saque
      numero_de_saques += 1
      extrato.append(f'Saque de numero {numero_de_saques} no valor de R$: {saque}\n')
      print(f'Saque no valor de R$:{saque} efetuado com sucesso')

  if menu == "E":
    print('========== EXTRATO ==========')
    for item in extrato:
      print(item)
    print(f'Saldo Atual R$:{saldo:.2f}')
    print('=============================')

  if menu == "X":
    break