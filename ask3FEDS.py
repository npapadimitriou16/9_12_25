class Vector():
    
    def ReadData(self):
        self.x, self.y = 5,6
        print("The values of X and Y are: ",self.x,self.y)   
        return self.x,self.y
    
    def SetData(self,x,y):
        self.x =  input(("Change the First original values of the numbers: "))
        self.y =  input(("Change the Second original values of the numbers: "))
        
    
    def PrintData(self):
        print(self.x,self.y)

x = Vector()
x.ReadData()
x.SetData(4,6)
x.PrintData()

