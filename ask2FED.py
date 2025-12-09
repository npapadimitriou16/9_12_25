class rectangle:
    def lenght():
        lenght = int(input("give me the length of the rectangle: "))
        return lenght
    def width():   
        width = int(input("give me the width of the rectangle: "))
        return width
    def CalcArea(len,wid):
        surface = len * wid
        return surface
    
print("The surface of the rectangel is: " , rectangle.CalcArea(rectangle.lenght(),rectangle.width()))

    