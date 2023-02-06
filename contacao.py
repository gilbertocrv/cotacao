import requests

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,DOGE-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    cotacao_doge = requisicao_dic['DOGEBRL']['bid']
    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    DOGE: {cotacao_doge}
    BTC: {cotacao_btc}'''

    print(texto)

pegar_cotacoes()