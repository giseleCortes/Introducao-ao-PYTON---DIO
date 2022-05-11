# Modulos
#
# Modulos em PYTHON são os arquivos .py. Cada "folha" é um modulo e eles podem interegir entre site

# Importação pelo console

# Abrir o python console e então utilizar o  import nomedoarquivo(modulo)
# dessa forma "pegamos" todo o arquivo
# pode se importar e estanciar a classe ao mesmo tempo
#
#     televisao = AU7-3 televisao.Televisao

#main

# if __name__ == '__main__':

# quando importamos o modulo (import AU7-3 televisao) ele ira executar tudo que contem no modulo
# para que isso nao ocorra utilizamos o main
# essa função diz "quando o main ( proprio arquivo) estiver me chamando ( sendo executado) eu faço o quem abaixo de mim
# caso contrário, não.
# ou seja se eu executar no proprio modulo original ele ira executar mas se eu chamar em outro arquivo ele irá "rodar"
# apenas quando solicitado.

# importando apenas uma classe especifica

# para isso utilizamos o from
        #from AU7-3_televisao import Televisao
# dessa forma basta estanciar a classe apos a importação e utilizar

# CHAMANDO DENTRO DO PROPRIO ARQUIVO
# as formas acima são utilizadas para chamar o modulo pelo console mas podemos chamar o modulo dentro do proprio arquivo
# no inicio da pagina digitamos

from AU7-3 televisao import Televisao # o nome dos arquivos estao com espaço por isso da erro nesse caso.
                                      # lembrar sempre de utilizar o underscore(underline)
# e depois basta estanciar a classe
televisao = Televisao ()


