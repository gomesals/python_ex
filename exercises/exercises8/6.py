class TV:
    canal = 0
    volume = 0

    def aumentarVolume(self):
        if self.volume <= 10:
            self.volume += 1

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1

    def trocarCanal(self, canal):
        if canal > 0 and canal < 100:
            self.canal = canal
