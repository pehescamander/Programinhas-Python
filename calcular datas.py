continuar = '1'
while continuar == '1':
    try:
        import time
        from datetime import date
        from datetime import datetime
        hoje = date.today()
        hoje = hoje.strftime('%d/%m/%Y')
        print('\n')
        print('Calcule os dias ente duas datas.')
        print('Use esse formato de data: ', hoje)
        print('\n')
        data1 = input('Digite a DATA INICIAL para contar os dias: ')
        data1 = datetime.strptime (data1, '%d/%m/%Y')
        data2 = input('Digite a DATA FINAL contar os dias: ')
        data2 = datetime.strptime(data2, '%d/%m/%Y')
        quantidade_dias = abs((data2 - data1).days)
        print('\n')
        print('Calculando os dias...')
        print(f'A diferença entre essas datas é {quantidade_dias} dias.')
        print('\n')
        print('Obrigado por me usar. Att: Pedro Henrique Barros Silvério')
        continuar = input('Se quiser somar a diferença entre outras datas digite 1 ou aperte enter para sair ')
    except:
        print('\n')
        print('Parece que você digitou uma data invalida ou em outro formato')
        print('Por favor, use somente datas validas seguindo o formato suportado')
        continuar = input('Você pode digitar 1 para continuar ou enter para sair ')
if continuar != '1':
    exit
