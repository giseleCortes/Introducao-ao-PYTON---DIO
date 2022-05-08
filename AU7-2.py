# passando numeros diferentes nas operações
class Calculadora:
    # def __init__(self):  # inicializador
        # pass  # o inicializador não pode ficar vazio, então utilizamos o pass que não tem nenhuma função
            # mas nesse caso podemos não utilizar o init

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

calculadora = Calculadora()  # como eu quero usar numero diferentes nas operações eu não passo nenhum parametro aqui

print(calculadora.soma(10, 5))
print(calculadora.subtracao(8, 7))
print(calculadora.multiplicacao(100, 3))
print(calculadora.divisao(10, 5))
