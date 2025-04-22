class Solids:
    def __init__(self):
        pass
    def surfaceArea(self):
        pass
    def volume(self):
        pass
    
class cube:
    def __init__(self,side):
        self.side=side
    def surfaceArea(self):
        return 6*self.side*self.side
    def volume(self):
        return (self.side)**3
    
class cuboid:
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def surfaceArea(self):
        return 2*((self.l*self.b)+(self.b*self.h)+(self.h*self.l))
    def volume(self):
        return self.l*self.b*self.h
    
class cylinder:
    def __init__(self,r,h):
        self.r=r
        self.h=h
    def surfaceArea(self):
        return 2*3.14*self.r*(self.r+self.h)
    def volume(self):
        return 3.14*(self.r**2)*self.h  
class sphere:
    def __init__(self,r):
        self.r=r
    def surfaceArea(self):
        return 4*3.14*(self.r**2)
    def volume(self):
        return (4/3)*3.14*(self.r**3)
class cone:
    def __init__(self,r,h):
        self.r=r
        self.h=h
    def surfaceArea(self):
        return 3.14*self.r*(self.r+(self.h**2+self.r**2)**0.5)
    def volume(self):
        return (1/3)*3.14*(self.r**2)*self.h          
    
solid=cube(10)
print("The volume and surface area of the cube are:")
print("Volume:")
print(solid.volume())
print("Surface Area:")
print(solid.surfaceArea())
solid=cuboid(10,420,30)
print("The volume and surface area of the cubiod are:")
print("Volume:")
print(solid.volume())
print("Surface Area:")
print(solid.surfaceArea())
solid=cylinder(6.9,20)
print("The volume and surface area of the cylinder are:")
print("Volume:")
print(solid.volume())
print("Surface Area:")
print(solid.surfaceArea())
