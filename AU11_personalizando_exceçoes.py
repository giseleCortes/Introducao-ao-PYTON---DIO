class Error(Exception):
    pass


class InputError(Error):  # por convenção toda classe de eceção deve terminar com error
    def __init__(self, message):
        self.message = message


while True:  # Executa pra sempre, colocando errado ou certo
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')  # raise é utilizado para forçar uma exceção
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break  # força a saida do loop caso digite corretamente
    except ValueError:
        print('Valor inválido: Digite um numero de 0 a 10: ')
    except InputError as ex:
        print(ex)
