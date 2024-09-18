import calendar
from datetime import datetime
import requests

dic = {}

def cotar_periodo(data):
  first_date = datetime.strptime(data, "%m/%Y")

  first_date = first_date.replace(day=1)
  last_date = first_date.replace(day=calendar.monthrange(first_date.year, first_date.month)[1])

  data_inicial = first_date.strftime("%m-%d-%Y")
  data_final = last_date.strftime("%m-%d-%Y")

  url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='{data_inicial}'&@dataFinalCotacao='{data_final}'&$format=json"
  res = requests.get(url)
  dados = res.json()
  cotacoes = dados['value']
  
  valores_compra = [i['cotacaoCompra'] for i in cotacoes]

  maximo = max(valores_compra)
  dic.update({'Maximo': (maximo)})

  minimo = min(valores_compra)
  dic.update({'Minimo': (minimo)})

  media = sum(valores_compra) / len(valores_compra)
  dic.update({'Media': (media)})

  return dic

#{'Maximo': 5.4744, 'Minimo': 5.1878, 'Media': 5.367476190476189}
cotar_periodo("07/2022")
