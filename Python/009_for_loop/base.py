x = int(input("ENTER LINE LENGTH - "))
vh = input("Do you want a horizontal or vertical line? (h/v) - ")
if vh == "v":
    print(" ")
    for y in range(0,x):
        print("*")
elif vh == "h":
    print(" ")
    for y in range(0,x):
        print("*", end = (" "))
else:
    for y in range(0,x * 10):
        print("boi you stupid")