# https://web.dio.me/course/introducao-a-programacao-com-python/learning/bcc0f1da-a2d2-4597-8747-3a069b1f7a13?back=/browse
# O numero primo é aquele que é divisivel APENAS por 1 e por ele mesmo.
# RANGE é utilizado para percorrer uma aqguencia de numeros
# in range(100) irá percorrer de 0 a 99
# in range (1,101) irá percorrer do numero 1 ao 100
# in range (90, 101) irá percorrer do 90 ao 100


a = int(input('Entre com o numero: '))
div = 0
b= ':'
c= '='
for x in range(1, a+1):
    resto = a % x
    print(a, b, x, c, resto)
# sempre que o numero que está no laço for divisivel pelo numero percorrido o resto será ZERO
    if resto == 0:
        div += 1  # entendi o programa até essa parte, não consegui entender a logica em ter um "contador" aqui.
                  # entendiiii cada vez que aparecer um zero o contador soma +1 o que significa que o numero foi divisivel
                  # no caso dos numeros primos so pode aparecer dois zeros.

if div == 2:
    print('Numero {} é primo'.format(a))
else:
    print('Numero  {} não é primo' .format(a))