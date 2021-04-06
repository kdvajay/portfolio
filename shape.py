class shape():
    def what_am_i(self):
        print("i am a shape")
        
class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calc_perimeter(self):
        return self.length*2 + self.width*2

class square(shape):
    def __init__(self,s1):
        self.s1=s1
        
    def calc_perimeter(self):
        return self.s1*4
    
a_rectangle=rectangle(20,50)
a_square=square(29)
a_rectangle.what_am_i()
a_square.what_am_i()


        
    
        