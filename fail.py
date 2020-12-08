import gerador_fail, consulta_fail, ler_json_fail
import datetime
print("""
_/﹋\_
(҂`_´)
<,︻╦╤─ ҉ - -
_/﹋\_
▓▒░ ►▬ WELCOME ▬◄ ░▒▓""")
data = datetime.datetime.now()
datetim = data.strftime("%d/%m/%Y %H:%M")
print(datetim)
print('\n1 = Consultas \n2 = Geradores de dados')
escolha = input('Escolha uma das opções: ')
def banner():
    print("""
╔═╗╔═╗╔═╗╔══════╗╔════╗
║ ║║ ║║ ║╚═╗  ╔═╝║  ══╣
║ ╚╝ ╚╝ ║  ║  ║  ║  ╔═╝
╚═══════╝  ╚══╝  ╚══╝

""")
def banner_2():
    print("""
░▄▀▀▀▀▄░░▄▄
█░░░░░░▀▀░░█░░░░░░▄░▄
█░║░░░░██░████████████
█░░░░░░▄▄░░█░░░░░░▀░▀
░▀▄▄▄▄▀░░▀▀
""")
def consultas():
    banner()
    print('1 = Consulta CEP \n2 = Consulta Ip\n3 = Consulta cnpj ')
    opcao = input('Escolha uma opção: ')
    if opcao == '1' or opcao == '01':
        banner_2()
        consulta_fail.Consulta_Cep()
    elif opcao == '2' or opcao == '02':
        banner_2()
        consulta_fail.Consulta_IP()
    elif opcao == '3' or opcao == '03':
        banner_2()
        consulta_fail.Consulta_CNPJ()
    else:
        print('Opção inválida')
def geradores():
    banner()
    print('1 = Gerador de cpf\n2 = Gerador de cnpj\n3 = Gerador de conta bancaria\n4 = Gerador de números do cartão')
    opc = input('Escolha uma dessas opções: ')
    if opc == '1' or opc == '01':
        banner_2()
        gerador_fail.gerador_de_cpf()
    elif opc == '2' or opc == '02':
        banner_2()
        gerador_fail.gerador_de_cnpj()
    elif opc == '3' or opc == '03':
        ler_json_fail.ler_conta_bancaria()
        banner_2()
    elif opc == '4' or opc == '04':
        banner_2()
        ler_json_fail.ler_numero_cartao()
    else:
        print('Opção inválida')
if escolha == '1' or escolha == '01':
    consultas()
elif escolha == '2' or escolha == '02':
    geradores()
else:
    print('Opção errada')
