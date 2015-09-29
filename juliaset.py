import cmath
import numpy as np

class JuliaSet:
    def __init__(self, c, n = 100):
        self.c = c
        self.n = n
        self._d = .001
    
    def juliamap(self, z):
        return z ** 2 + self.c
    
    def iterate(self, z):
        for m in np.arange(1, self.n+1):
            z = self.juliamap(z)
            if abs(z) > 2:
                return m
        return 0
    
    
    def setcomplexplane(self, _d):
        x, y = -2, -2
        self._complexplane = []
        while (x <= 2 and y <= 2):
            z = complex(x,y)
            self._complexplane.append(z)
            x = self._d + x
            y = self._d + y
        
    def set_spacing(self, d):
        self._d = d
        self.setcomplexplane(d)
        
    
    def generate(self):
        self.set = []
        for i in self._complexplane:
            self.set.append(self.iterate(i))
        return self.set