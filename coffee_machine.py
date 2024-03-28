import pyfiglet
import time
logo = pyfiglet.figlet_format("SAHIL'S AUTOMATIC COFFEE SHOP ")
print(logo)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 30,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 100,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}


def is_resource_sufficient(order_ingredient):
    is_enough = True
    for items in order_ingredient:
        if order_ingredient[items] >= resources[items]:
            print(f"sorry there is no enough {items}.")
            is_enough = False
    time.sleep(10)
    return is_enough


def process_coin():
    """returns the total calculated coin and returns the result"""
    print("please insert coin")
    total = int(input("how many notes of 10? :"))*10
    total += int(input("how many notes of 20? :"))*20
    total += int(input("how many notes of 100? :"))*100
    total += int(input("how many notes of 500? :"))*500
    time.sleep(3)
    return total


def is_transaction_successful(money_received,cost_of_the_drink):
    """return true if transaction is successful else return false."""
    if money_received >= cost_of_the_drink:
        change =(money_received-cost_of_the_drink)
        print(f"here is the change sir {change}")
        global profit
        profit += cost_of_the_drink
        return True
    else:
        print("Sorry not enough money , we have refunded the amount")
        return False

def make_coffee(drink_name,order_ingredient):
    for items in order_ingredient:
        resources[items] -= order_ingredient[items]
    for number in range(1,101):
        new_number=str(number)
        print(f"Please wait we are making your coffee : {new_number}% completed")
        time.sleep(0.10)
    print(f"here is your  {drink_name} sir !!!! THANK YOU !!")



profit = 0
is_on = True
print(" HELLO THERE GOOD MORNING")
while is_on:
    choice = input("what do you want latte, cappuccino or espresso?")
    if choice == "off":
        print("bye_bye")
        is_on = False
        time.sleep(5)
    elif choice == "report":
        print(f"milk ={resources['milk']}ml")
        print(f"water ={resources['water']}ml")
        print(f"coffee ={resources['coffee']}gm")
        print(f"Money = {profit}")
        time.sleep(5)
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
                time.sleep(5)






