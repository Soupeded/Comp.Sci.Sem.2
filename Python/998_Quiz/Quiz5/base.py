x = input("What is your favorite number? (Answer in complete sentence) - ")
y = input("Now what is your age? - ")
c = 0
for i in range(0,len(x)):
    if (x[i:i+2] == "11"):
        c = c+(int(x[i:i+2]))
print(c * y)

#I gave up :P