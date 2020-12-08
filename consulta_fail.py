"""
API DE CONSULTAS CEP, IP, CNPJ
"""
import requests
#consulta cep
def Consulta_Cep():
    cep = input('Cep a consultar: ')
    if len(cep) != 8:
        print('Quantidade de digitos errado')
        exit(0)
    url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    api = url.json()
    if 'erro' not in api:
        print('Cep: {}'.format(api['cep']))
        print('Logradouro: {}'.format(api['logradouro']))
        print(f'Complemento: {api["complemento"]}')
        print(f'Bairro: {api["bairro"]}')
        print(f'Cidade: {api["localidade"]}')
        print(f'UF: {api["uf"]}')
        print(f'População: {api["ibge"]}')
        print(f'Gia: {api["gia"]}\nDDD: {api["ddd"]}\nSiafi: {api["siafi"]}')
    else:
        print(f'{cep} Cep não encontrado')
#consulta ip
def Consulta_IP():
    ip = input('Ip para consultar: ')
    if len(ip) <= 5:
        print('Quantidade de digitos de um ip está errado')
        exit()
    url = requests.get(f'http://ip-api.com/json/{ip}')
    api = url.json()
    if 'message' not in api:
        print(f'\nStatus: {api["status"]}\nIP: {api["query"]}')
        print(f'País: {api["country"]}\nUf País: {api["countryCode"]}\Estado: {api["regionName"]}\nEStado uf: {api["region"]}\nCidade: {api["city"]}\nCódico Postal: {api["zip"]}')
        print(f'Lat: {api["lat"]}\nLon: {api["lon"]}\nFuso horário: {api["timezone"]}\nProvedor: {api["org"]}\n ')
    else:
        print(f'{ip} IP invalído')
#Consulta cnpj
def Consulta_CNPJ():
    cnpj = input('CNPJ a consultar: ')
    if len(cnpj) != 14:
        print("Quantidade de digitos errada")
    url = requests.get('https://www.receitaws.com.br/v1/cnpj/02558157000162')
    api = url.json()
    if 'message' not in api:
        print(f'CNPJ: {api["cnpj"]}\nSituação: {api["situacao"]}\nData da situação: {api["data_situacao"]}\nAbertura: {api["abertura"]}')
        print(f'Nome: {api["nome"]}\nTipo: {api["tipo"]}\nCapital Social: {api["capital_social"]}')
        print(f'Telefone: {api["telefone"]}\nEmail: {api["email"]}\nBairro: {api["bairro"]}, Logradouro: {api["logradouro"]}')
        print(f'Número: {api["numero"]}\nCep: {api["cep"]}\nCidade: {api["municipio"]}\nNatureza Juridica: {api["natureza_juridica"]}')
    else:
        print(f'{cnpj} CNPJ não encontrado')
        exit(0)
#Fim
