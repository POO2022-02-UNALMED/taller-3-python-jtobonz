class Marca:

    def __init__(self, nombre ):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

class TV:
    
    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        self.numTV += 1
    
    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca

    def getControl(self):
        return self.control
    def setControl(self, control):
        self.control = control

    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.marca = precio

    def getVolumen(self):
        return self.volumen
    def setVolumen(self, volumen):
        if self.estado == True:
            self.volumen = volumen
    
    def getCanal(self):
        return self.canal
    def setCanal(self, canal):
        if self.estado == True:
            self.canal = canal

    def getNumTV(self):
        return self.numTV
    #def setNumTV(self, numTV):
    #    self.numTV = numTV

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

class Control:

    def __init__(self):
        self.tv = None

    def getTv(self):
        return self.tv
    def setTv(self, tv):
        self.tv = tv
    
    def enlazar(self, tv):
        self.setTv(tv)
        self.tv.setControl(self)

    
    def turnOn(self):
        if isinstance(self.tv, TV):
            self.tv.turnOn()
        
    def turnOff(self):
        if isinstance(self.tv, TV):
            self.tv.turnOff()
        
    def canalUp(self):
        if isinstance(self.tv, TV):
            self.tv.canalUp()
    
    def canalDown(self):
        if isinstance(self.tv, TV):
            self.tv.canalDown()

    def volumenUp(self):
        if isinstance(self.tv, TV):
            self.tv.volumenUp()

    def volumenDown(self):
        if isinstance(self.tv, TV):
            self.tv.volumenDown()

    def setCanal(self, canal):
        if isinstance(self.tv, TV):
            self.tv.getCanal(canal)

    
    

    
    
