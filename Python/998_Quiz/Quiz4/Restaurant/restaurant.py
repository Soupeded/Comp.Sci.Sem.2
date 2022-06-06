import random
rlist = ["Din Tai Fung", "Chuck E. Cheese", "Kitchen Nightmares"]
menulist1 = ["Cucumbers", "Noodles", "Dumplings"]
menulist2 = ["Pizza", "Cheese", "Chuck"]
menulist3 = ["Steak", "Chicken", "Lamb Sauce"]
x = random.randrange(2)
if x == 0:
    print(rlist[0])
    print(menulist1)
    i = input("Pick something from the menu (1-3) - ")
    if i == 1:
        print("Enjoy your " + menulist1[0])
    elif i == 2:
        print("Enjoy your " + menulist1[1])
    elif i == 3:
        print("Enjoy your " + menulist1[2])
    else:
        print("Are you ok?")
elif x == 1:
    print(rlist[1])
    print(menulist2)
    i = input("Pick something from the menu (1-3) - ")
    if i == 1:
        print("Enjoy your " + menulist2[0])
    elif i == 2:
        print("Enjoy your " + menulist2[1])
    elif i == 3:
        print("Enjoy your " + menulist2[2])
    else:
        print("Are you ok?")
elif x == 2:
    print(rlist[0])
    print(menulist3)
    i = input("Pick something from the menu (1-3) - ")
    if i == 1:
        print("Enjoy your " + menulist3[0])
    elif i == 2:
        print("Enjoy your " + menulist3[1])
    elif i == 3:
        print("Enjoy your " + menulist3[2])
    else:
        print("Are you ok?")