import json
import gerador_fail
def ler_conta_bancaria():
    gerador_fail.conta_bancaria()
    with open('api_conta-fail.json', 'r', encoding='UTF-8') as json_file:
        json_api = json.load(json_file)
    print(f'Conta: {json_api["Conta"]}')
    print(f'Agencia: {json_api["Agencia"]}\nBanco: {json_api["Banco"]}\nCidade: {json_api["Cidade"]}\nEstado: {json_api["Estado"]}')
def ler_numero_cartao():
    gerador_fail.numero_cartao()
    with open('api_cartao-fail.json', 'r', encoding='UTF-8') as json_cartao:
        json_api = json.load(json_cartao)
    print(f'Número do Cartão: {json_api["Numero do Cartao"]}\nData de Validade: {json_api["Data de Validade"]}\nCódico de Segurança(CVV): {json_api["Codico de Seguranca(CVV)"]}')
