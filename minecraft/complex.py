class Complex:
    
    def __init__(self, real, imag):
        self.x = real
        self.y = imag


    def square(self):
	self.x = self.x * self.x - self.y * self.y
	self.y = 2 * self.x * self.y

