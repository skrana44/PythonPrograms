def greet(name,surname):
    #METHOD 1 for below python 3.6
    message = "Hi %s %s" %(name.title(),surname.title())
    #METHOD 2 & 3 for above python 3.6. Thie is commented though
    #message = f"Hi {name.title()} {surname.title()}."
    #message = "Hi {} {}".format(name.title(),surname.title())
    return message

value1 = input("Please enter your name: ")
value2 = input("Please enter your surname: ")
print(greet(value1,value2))
