from televisores.marca import Marca

class TV:
    
    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        TV.numTV += 1
    
    def getMarca(self):
            return self.marca
    def setMarca(self, marca):
        if isinstance(marca, Marca):
            self.marca = marca

    def getControl(self):
        return self.control
    def setControl(self, control):
        self.control = control

    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio = precio

    def getVolumen(self):
        return self.volumen
    def setVolumen(self, volumen):
        if self.estado == True:
            self.volumen = volumen
    
    def getCanal(self):
        return self.canal
    def setCanal(self, canal):
        if (canal <= 120 and canal >= 0 and self.estado == True):
            self.canal = canal

    def getNumTV():
        return TV.numTV
    
    def setNumTV(numTV):
        TV.numTV = numTV

    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False
    def getEstado(self):
        return self.estado

    def canalUp(self):
        if (self.canal < 120 and self.estado == True):
            self.canal += 1
    def canalDown(self):
        if (self.canal > 0 and self.estado == True):
            self.canal -=  1
    
    def volumenUp(self):
        if (self.volumen < 7 and self.estado == True):
            self.volumen += 1
    def volumenDown(self):
        if (self.volumen > 0 and self.estado == True):
            self.volumen -= 1