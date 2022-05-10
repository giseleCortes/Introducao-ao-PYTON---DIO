class Televisao:
    def __init__(self):  # nesse caso sempre que eu estanciar uma televisão ela irá iniciar desligada
        self.ligada = False
        self.channel = 2

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def channel_up(self):
        if self.ligada:
            self.channel += 1

    def channel_down(self):
        if self.ligada:
            self.channel -= 1


televisao = Televisao()

print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))
print('Channel: {}' .format(televisao.channel))
