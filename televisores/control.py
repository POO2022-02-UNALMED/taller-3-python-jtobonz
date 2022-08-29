from televisores.tv import TV

class Control:

    def __init__(self):
        self.tv = None

    def getTv(self):
        return self.tv
    def setTv(self, tv):
        self.tv = tv
    
    def enlazar(self, tv):
        if isinstance(tv, TV):
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
            self.tv.setCanal(canal)