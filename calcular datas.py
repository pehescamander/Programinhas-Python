import time
from datetime import date
from datetime import datetime
hoje = date.today()
hoje = hoje.strftime('%d/%m/%Y')
print('Calcule os dias ente duas datas.')
print('Use esse formato de data: ', hoje)
data1 = input('Digite a data incial para contar os dias: ')
data1 = datetime.strptime (data1, '%d/%m/%Y')
data2 = input('Digite a data final contar os dias: ')
data2 = datetime.strptime(data2, '%d/%m/%Y')
quantidade_dias = abs((data2 - data1).days)
print('Calculando os dias...')
print(f'A diferença entre essas datas é {quantidade_dias} dias.')
print('Obrigado por me usar. Att: Pedro Henrique Barros Silvério')