# txt = "Hello World"[::-1]
# print(txt)
#...............


# reverse string with functional way with user input
def reverse(str):   
    return str[::-1]  

string = input("Enter your string : ")
    
print ("The original string  is : ",string)   
print ("The reversed string is : ",reverse(string))  



# reverse string with class 
class Reverse:

    def __init__(self, str):
        self.str = str[::-1]
        
    def show(self):
        return f"The reversed string is {self.str}"

ob = Reverse('riyad')
print(ob.show())

ob2 = Reverse('saikat')
print(ob2.show())