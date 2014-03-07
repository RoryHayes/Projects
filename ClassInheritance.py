class Parent:
    
    parentAttr = 100
    def __init__(self):
        print ('Calling Parent constructor')

    def parentMethod(self):
        print('Calling Parent method')

    def setAttr (self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print('Parent attribute: ', Parent.parentAttr)

class Child (Parent):
    
    def __init__(self):
        print ('Calling the chid constructor')

    def childMethod(self):
        print ('calling child method')

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

    
