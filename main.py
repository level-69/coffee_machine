from storage import menu, store
import os

def clear():
    # Check if running in a terminal that supports clearing
    if os.name == 'nt':
        os.system('cls')
    elif os.getenv('TERM'):
        os.system('clear')
    else:
        print("\n"*3)  # Print new lines as a fallback to simulate clearing the screen

x = 1
total_earning = 0


def report(report):
    if user_choice == "report":
        for n in store:
            if n == "water":
                print(f"{n} = {store[n]} ml")
            elif n == "milk":
                print(f"{n} = {store[n]} ml")
            elif n == "coffee":
                print(f"{n} = {store[n]} g")
        # earning(user_choice)
        print(f"Your today earning is {total_earning}.")


def off_machine(off):
    if user_choice == "off":
        exit()


def resource_suff():

    if user_choice == "espresso":
        water = menu["espresso"]["ingredient"]["water"]
        coffee = menu["espresso"]["ingredient"]["coffee"]
        if water > store["water"]:
            print("Sorry, No more water left.")
            exit()

        if coffee > store["coffee"]:
            print("Sorry, No more coffee left.")
            exit()

    if user_choice == "latte":
        water = menu["latte"]["ingredient"]["water"]
        coffee = menu["latte"]["ingredient"]["coffee"]
        milk = menu["latte"]["ingredient"]["milk"]
        if water > store["water"]:
            print("Sorry, No more water left.")
            exit()

        if coffee > store["coffee"]:
            print("Sorry, No more coffee left.")
            exit()

        if milk > store["milk"]:
            print("Sorry, No more milk left.")
            exit()



    if user_choice == "cappuccino":
        water = menu["espresso"]["ingredient"]["water"]
        coffee = menu["cappuccino"]["ingredient"]["coffee"]
        milk = menu["cappuccino"]["ingredient"]["milk"]
        if water > store["water"]:
            print("Sorry, No more water left.")
            exit()

        if coffee > store["coffee"]:
            print("Sorry, No more coffee left.")
            exit()

        if milk > store["milk"]:
            print("Sorry, No more milk left.")
            exit()



def coin_processing():
    global total_bill
    penny  = int(input("How many penny you have : \n"))
    dime = int(input("How many dime you have : \n"))
    nickel = int(input("How many nickel you have : \n"))
    quater = int(input("How many quater you have : \n"))
    total_bill_cent = 1*penny + 10*dime + 5*nickel + 25*quater
    total_bill = total_bill_cent/100
    print(total_bill)
    return total_bill


def price_cal(coffee):
    global amount_return
    if total_bill >= menu[user_choice]["cost"]:
        amount_return = total_bill - menu[user_choice]["cost"]
        print(f"Wait a second, we are preparing you {user_choice}.")
        print(f"Take you change of {amount_return}")

    elif total_bill <+ menu[user_choice]["cost"]:
        print("Money is not suffecient")
        # exit()
    return amount_return


def material_sub(user_choice):
    if user_choice == "espresso":
        store["water"] = store["water"] - 50
        store["coffee"] = store["coffee"] - 18
    if user_choice == "latte":
        store["water"] = store["water"] - 200
        store["coffee"] = store["coffee"] - 24
        store["milk"] = store["milk"] - 150
    if user_choice == "cappuccino":
        store["water"] = store["water"] - 250
        store["coffee"] = store["coffee"] - 24
        store['milk'] = store["milk"] - 150


def earning(user_choice):
    global earn
    espresso = 0
    latte = 0
    cappuccino = 0
    if user_choice == "espresso":
        if total_bill >= menu[user_choice]["cost"]:
            espresso += 1
    elif user_choice == "latte":
        if total_bill >= menu[user_choice]["cost"]:
            latte += 1
    elif user_choice == "cappuccino":
        if total_bill >= menu[user_choice]["cost"]:
            cappuccino += 1
    earn = espresso*1.5 + latte*2 + cappuccino*3
    return earn


while x == 1:
    clear()
    user_choice = input("What do you like? (espresso, latte, cappuccino)\n")
    if user_choice == "off":
        exit()
    else:

        if user_choice == "report":
            report(user_choice)
            earning(user_choice)
        elif user_choice == "espresso":
            off_machine(user_choice)
            resource_suff()
            coin_processing()
            price_cal(user_choice)
            material_sub(user_choice)
            earning(user_choice)
            total_earning = total_earning + earn
        elif user_choice == "latte":
            off_machine(user_choice)
            resource_suff()
            coin_processing()
            price_cal(user_choice)
            material_sub(user_choice)
            earning(user_choice)
            total_earning = total_earning + earn
        elif user_choice == "cappuccino":
            off_machine(user_choice)
            resource_suff()
            coin_processing()
            price_cal(user_choice)
            material_sub(user_choice)
            earning(user_choice)
            total_earning = total_earning + earn
        else:
            print("please enter valid input")