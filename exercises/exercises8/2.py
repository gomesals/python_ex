class Quadrado:
    lado = 0

    def mudarLado(self, lado):
        self.lado = lado

    def retornarLado(self):
        return self.lado

    def calcularArea(self):
        self.area = self.lado * self.lado
        return self.area
