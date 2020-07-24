name = True
def two_fer(name):
    while True:
        name = input("What is your name?  ")
        if name.isdigit():
            print("Your name cannot be a number")
            
        elif name == "":
            return "One for you, one for me."
        
        else:
            return f"One for {name}, one for me."
    

fer_two = two_fer(name)

print(fer_two)
