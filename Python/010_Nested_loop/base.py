sym = input("What symbol would you like to use? - ")
x = int(input("What is the width of your box? - "))
y = int(input("What is the height of your box? - "))
for i in range(0,y):
    for c in range(0,x):
        print(sym, end = (" "))
    print("")