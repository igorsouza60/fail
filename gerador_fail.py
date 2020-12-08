import requests ,json
from bs4 import BeautifulSoup
def numero_cartao():
   bandeira = input('Bandeira do cartão: ')
   url = requests.post('https://www.4devs.com.br/ferramentas_online.php',{'acao' : 'gerar_cc', 'pontuacao' : 'S', 'bandeira' : bandeira}).text
   soup = BeautifulSoup(url, 'html.parser')
   numero_do_cartao = soup.find('div', id="cartao_numero").text.strip()
   data_validade = soup.find('div', id="data_validade").text.strip()
   cvv = soup.find('div', id="codigo_seguranca").text.strip()
   cartao = {'Numero do Cartao' : numero_do_cartao, 'Data de Validade' : data_validade, 'Codico de Seguranca(CVV)' : cvv}
   with open('api_cartao-fail.json', 'w', encoding='UTF-8') as json_cartao:
      json.dump(cartao, json_cartao, ensure_ascii=False, indent=3)
def conta_bancaria():
   estado = input('Estado: ')
   url = requests.post('https://www.4devs.com.br/ferramentas_online.php',{'acao' : 'gerar_conta_bancaria', 'estado' : estado, 'banco' : ''}).text
   soup = BeautifulSoup(url, 'html.parser')
   conta = soup.find('div', id="conta_corrente").text
   agencia = soup.find("div", id="agencia").text.strip()
   banco = soup.find("div", id="banco").text.strip()
   cidade = soup.find("div", id="cidade").text.strip()
   estado = soup.find("div", id="estado").text.strip()
   gerar = {'Conta' : conta, 'Agencia' : agencia, 'Banco' : banco, 'Cidade' : cidade, 'Estado' : estado}
   with open('api_conta-fail.json', 'w', encoding='UTF-8') as json_file:
      json.dump(gerar, json_file, ensure_ascii=False, indent=5)
def gerador_de_cpf():
   uf = input('Uf do estado: ')
   quant = int(input('Quantidade de cpf: '))
   for i in range(0,quant):
        url = requests.post('https://www.4devs.com.br/ferramentas_online.php',{'acao' : 'gerar_cpf',  'pontuacao' : 'S', 'cpf_estado' : uf}).text
        print(url)
def gerador_de_cnpj():
   quantidade = int(input('Quantidade de CNPJ: '))
   for cnp in range(0, quantidade):
        url_2 = requests.post('https://www.4devs.com.br/ferramentas_online.php',{'acao' : 'gerar_cnpj', 'pontuacao' : 'S'}).text
        print(url_2)
