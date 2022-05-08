# A diferença entre método e função e que:
# por convenção função retorna um valor e métodos não
# em python essa diferenciação não é explicita, os metodos são denominados definições que são
# declarados pelas letras def sempre com um nome e tem seus parametros separados por virgula

def soma(a, b):  # metodo
    return a + b  # função

# isso permite chamar apenas a função soma, sem precisar fazer sempre soma = a + b


print(soma(1, 2))
print(soma(5, 4))


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


print(subtracao(6, 3))
print(multiplicacao(8, 9))
print(divisao(10, 2))


# os metodos auxiliam em não ter que regerar código
# no caso sempre que eu quiser utilizar essa soma basta chamar o metodo

# CLASSES por convenção as classes começam com letra maiuscula

class Calculadora:
    def __init__(self, num1, num2):  # inicializador
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b


calculadora = Calculadora(10, 2) # isso é estanciar e foi passado os parametros
print(calculadora.valor_a)
print(calculadora.valor_b)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())
# ao estanciar o metodo init é chamado automaticamente, ja o metodo soma precisa ser chamado

# nesse caso passando o valor apenas uma vez, temos todas as operações

