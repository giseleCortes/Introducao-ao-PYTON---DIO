from datetime import date, time, datetime, timedelta


def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)  # por padrão irá mostra o padrão americano
    print(
        data_atual.strftime('%d/%m/%y'))  # ler a documentação da biblioteca para entender melhor sobre essas diretivas
    data_atual_str = data_atual.strftime('%A-%B-%Y')
    print(type(data_atual_str))
    print(type(data_atual))


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y  %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.year)
    print(data_atual.date())
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2022 12:20:22'
    print(data_string)
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y  %H:%M:%S')
    print(data_convertida)
    print(type(data_convertida))


def soma_e_subtracao_de_datas():
    data_string = '01/01/2022 12:20:22'
    print(data_string)
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y  %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=200, hours=6, minutes=15)  # time delta não tem anos
    print(nova_data)


if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_time()
    # trabalhando_com_datetime()
    soma_e_subtracao_de_datas()
