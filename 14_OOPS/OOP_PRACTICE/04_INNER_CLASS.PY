class color:
    def __init__(self):
        self.name = 'Green'
        self.lg = self.lightgreen()
        
    def show (self):
        print('name: ',self.name)
        
    class lightgreen :
        def __init__(self):
            self.name = "lightGreen"
            self.code = "024avc"
            
        def display(self):
            print('name: ',self.name)
            print('code: ',self.code)
            
            
outer =color()
outer.show()

g=outer.lg
g.display()