print('''                                                                                                                   
███╗   ██╗ █████╗ ███╗   ███╗██╗████████╗██╗  ██╗███████╗    ██╗   ██╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
████╗  ██║██╔══██╗████╗ ████║██║╚══██╔══╝██║  ██║██╔════╝    ██║   ██║██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██╔██╗ ██║███████║██╔████╔██║██║   ██║   ███████║███████╗    ██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
██║╚██╗██║██╔══██║██║╚██╔╝██║██║   ██║   ██╔══██║╚════██║    ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
██║ ╚████║██║  ██║██║ ╚═╝ ██║██║   ██║   ██║  ██║███████║     ╚████╔╝ ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝      ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝''')

item1=['Skittles(6.25);001']
item2=['Chips(1.50);002']
item3=['Icecream(5.00);003']
item4=['Water(1.50);004']
item5=['Cola(3.50);005']
item6=['ColdCoffee(20.67);006']
item7=['Salads(10.00);007']
item8=['Prime(49.50);008']
item9=['Juice(2.30);009']
item10=['Kitkat(2.50);010']
print("Welcome to the Vending Machine!")
print("Item\tPrice\tCode")
print(item1)
print(item2)
print(item3)
print(item4)
print(item5)
print(item6)
print(item7)
print(item8)
print(item9)
print(item10)
x=str(input("--------------------\nEnter the product code:\n"))
if x=='001':
    print('You have chosen Skittles!')
    y=float(input("Pay the amount:\n"))
    Skittles = 6.25
    if y > Skittles:
        print("Take your change with your selected item: ",y - Skittles)
    elif y<Skittles:
        print("no enough money")
        print("Amount refunded")
    elif y==Skittles:
        print("Here is your Skittles")
elif x=='002':
    print('You have chosen Chips!')
    y=float(input("Pay the amount:\n"))
    Chips = 1.50
    if y > Chips:
        print("Take your change with your selected item: ",y - Chips)
    elif y<Chips:
        print("no enough money")
        print("Amount refunded")
    elif y==Chips:
        print("Here is your Chips")
elif x=='003':
    print('You have chosen Icecream!')
    y=float(input("Pay the amount:\n"))
    Icecream = 5.00
    if y > Icecream:
        print("Take your change with your selected item: ",y - Icecream)
    elif y<Icecream:
        print("no enough money")
        print("Amount refunded")
    elif y==Icecream:
        print("Here is your Icecream")
elif x=='004':
    print('You have chosen Water!')
    y=float(input("Pay the amount:\n"))
    Water = 1.50
    if y > Water:
        print("Take your change with your selected item: ",y - Water)
    elif y<Water:
        print("no enough money")
        print("Amount refunded")
    elif y==Water:
        print("Here is your Water")
elif x=='005':
    print('You have chosen =Cola!')
    y=float(input("Pay the amount:\n"))
    Cola = 3.50
    if y > Cola:
        print("Take your change with your selected item: ",y - Cola)
    elif y<Cola:
        print("no enough money")
        print("Amount refunded")
    elif y==Cola:
        print("Here is your Cola")
elif x=='006':
    print('You have chosen =ColdCoffee!')
    y=float(input("Pay the amount:\n"))
    ColdCoffee = 20.67
    if y > ColdCoffee:
        print("Take your change with your selected item: ",y - ColdCoffee)
    elif y<ColdCoffee:
        print("no enough money")
        print("Amount refunded")
    elif y==ColdCoffee:
        print("Here is your ColdCoffee")
elif x=='007':
    print('You have chosen =Salads!')
    y=float(input("Pay the amount:\n"))
    Salads = 10.00
    if y > Salads:
        print("Take your change with your selected item: ",y - Salads)
    elif y<Salads:
        print("no enough money")
        print("Amount refunded")
    elif y==Salads:
        print("Here is your Salads")
elif x=='008':
    print('You have chosen =Prime!')
    y=float(input("Pay the amount:\n"))
    Prime = 49.50
    if y > Prime:
        print("Take your change with your selected item: ",y - Prime)
    elif y<Prime:
        print("no enough money")
        print("Amount refunded")
    elif y==Prime:
        print("Here is your Prime")
elif x=='009':
    print('You have chosen =Juice!')
    y=float(input("Pay the amount:\n"))
    Juice = 2.30
    if y > Juice:
        print("Take your change with your selected item: ",y - Juice)
    elif y<Juice:
        print("no enough money")
        print("Amount refunded")
    elif y==Juice:
        print("Here is your Juice")
elif x=='010':
    print('You have chosen =Kitkat!')
    y=float(input("Pay the amount:\n"))
    Kitkat = 2.50
    if y > Kitkat:
        print("Take your change with your selected item: ",y - Kitkat)
    elif y<Kitkat:
        print("no enough money")
        print("Amount refunded")
    elif y==Kitkat:
        print("Here is your Kitkat")
while True:
    z=str(input("---------------------------\nBuy something more yes/no:\n"))

    if z=='no':
        print("==========================\nTHANKYOU FOR USING THE VENDING MACHINE:\n")
        break
    elif z=='yes':
        x=str(input("Input code to buy:\n"))
    if x=='001':
        print('You have chosen Skittles!')
        y=float(input("Pay the amount:\n"))
        Skittles = 6.25
        if y > Skittles:
            print("Take your change with your selected item: ",y - Skittles)
        elif y<Skittles:
            print("no enough money")
        elif y==Skittles:
            print("Here is your Skittles")
    elif x=='002':
        print('You have chosen Chips!')
        y=float(input("Pay the amount:\n"))
        Chips = 1.50
        if y > Chips:
            print("Take your change with your selected item: ",y - Chips)
        elif y<Chips:
            print("no enough money")
            print("Amount refunded")
        elif y==Chips:
            print("Here is your Chips")
    elif x=='003':
        print('You have chosen Icecream!')
        y=float(input("Pay the amount:\n"))
        Icecream = 5.00
        if y > Icecream:
            print("Take your change with your selected item: ",y - Icecream)
        elif y<Icecream:
            print("no enough money")
            print("Amount refunded")
        elif y==Icecream:
            print("Here is your Icecream")
    elif x=='004':
        print('You have chosen Water!')
        y=float(input("Pay the amount:\n"))
        Water = 1.50
        if y > Water:
            print("Take your change with your selected item: ",y - Water)
        elif y<Water:
            print("no enough money")
            print("Amount refunded")
        elif y==Water:
            print("Here is your Water")
    elif x=='005':
        print('You have chosen Cola!')
        y=float(input("Pay the amount:\n"))
        Cola = 3.50
        if y > Cola:
            print("Take your change with your selected item: ",y - Cola)
        elif y<Cola:
            print("no enough money")
            print("Amount refunded")
        elif y==Cola:
            print("Here is your Cola")
    elif x=='006':
        print('You have chosen ColdCoffee!')
        y=float(input("Pay the amount:\n"))
        ColdCoffee = 20.67
        if y > ColdCoffee:
            print("Take your change with your selected item: ",y - ColdCoffee)
        elif y<ColdCoffee:
            print("no enough money")
            print("Amount refunded")
        elif y==ColdCoffee:
            print("Here is your ColdCoffee")
    elif x=='007':
        print('You have chosen Salads!')
        y=float(input("Pay the amount:\n"))
        Salads = 10.00
        if y > Salads:
            print("Take your change with your selected item: ",y - Salads)
        elif y<Salads:
            print("no enough money")
            print("Amount refunded")
        elif y==Salads:
            print("Here is your Salads")
    elif x=='008':
        print('You have chosen Prime!')
        y=float(input("Pay the amount:\n"))
        Prime = 49.50
        if y > Prime:
            print("Take your change with your selected item: ",y - Prime)
        elif y<Prime:
            print("no enough money")
            print("Amount refunded")
        elif y==Prime:
            print("Here is your Prime")
    elif x=='009':
        print('You have chosen Juice!')
        y=float(input("Pay the amount:\n"))
        Juice = 2.30
        if y > Juice:
            print("Take your change with your selected item: ",y - Juice)
        elif y<Juice:
            print("no enough money")
            print("Amount refunded")
        elif y==Juice:
            print("Here is your Juice")
    elif x=='010':
        print('You have chosen Kitkat!')
        y=float(input("Pay the amount:\n"))
        Kitkat = 2.50
        if y > Kitkat:
            print("Take your change with your selected item: ",y - Kitkat)
        elif y<Kitkat:
            print("no enough money")
            print("Amount refunded")
        elif y==Kitkat:
            print("Here is your Kitkat")