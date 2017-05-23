'''
    Classes are used to structure the program and __init__ is the first
    method that is invoked when the object of the class is created.
'''
class program():
    #This is the method invoked when the object is created and
    #This can contain initial setiting or the default value of the object
    #self is the accessor to the object.
    def __init__(self,*args,**kwargs):
        #defining certain properties using the object if the properties are
        #not to be referenced then we don't need to use the self pointer.
        self.lang = input("what is the language: ")
        #converting the user input to float value.
        self.version = float(input("What is the version of the language: "))
        self.skillLevel = input("What is the skill level: ")
#creating an object.
p1 = program();
print("Language : ",p1.lang)
print("version : ",p1.version)
print("skill level :",p1.skillLevel)
