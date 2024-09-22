"""
First call a function in this case i used hi, in it is a print command 
Next there is another function called hello
and there is an input command in it assigned to variable name
and then there is a print command with that says hello then your name
Nasheel Nadeem
"""





















def hi(): # starts the function
    """
    starts the function
    prints Hello, World!
    """
    print("Hello, World!") #prints Hello, World!

def hello(): # starts the function
 """
 starts the function
 asks user to input name and assigns it to a variable (name)
 prints Hello! + name
 """
 name=input("Write your name: ") #asks user to input name and assigns it to a variable (name)
 print("Hello!",name) #prints Hello! + name

hi() #calls the function
hello() #calls the function