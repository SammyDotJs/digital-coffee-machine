from Menu import MENU, resources

# penny: $0.01
# nickel: $0.05
# dime: $0.10
# quarter: $0.25


print(MENU)


def report(water, milk, coffee, money):
    return f"""Water: {water}ml,\nMilk": {milk}ml,\nCoffee: {coffee}g,\nMoney: ${money}
    """


def coins(quart, dime, nick, penny, flavor, cost, resource, ingredients):
    available_water = resource["water"]
    available_milk = resource["milk"]
    available_coffee = resource["coffee"]
    flavor_water = ingredients["water"]
    if flavor == "espresso":
        ingredients["milk"] = 0
    flavor_milk = ingredients["milk"]

    flavor_coffee = ingredients["coffee"]

    if available_water < flavor_water:
        return "Sorry, there is not enough water."
    elif available_milk < flavor_milk:
        return "Sorry, there is not enough milk"
    elif available_coffee < flavor_coffee:
        return "Sorry, there is not enough water"
    elif available_water < flavor_water and available_milk < flavor_milk and available_coffee < flavor_coffee:
        return "Sorry, all ingredients are unavailable."
    quarters = quart * 0.25
    dimes = dime * 0.10
    nickel = nick * 0.05
    pennies = penny * 0.01

    total_price = quarters + dimes + nickel + pennies
    if total_price < cost:
        refund = "Sorry that's not enough money. Money refunded."
        return refund
    change = round(total_price - cost, 2)
    return f"Here is {change} in change.\nHere is your {flavor}☕ Enjoy!"


def coffee_machine():
    money = 0
    is_machine_on = True

    while is_machine_on:
        sold = ""
        add_money = ""
        flavour_prompt = input("What would you like? (espresso/latte/cappuccino): ")
        if flavour_prompt == "espresso":
            resources["water"] -= MENU[flavour_prompt]["ingredients"]["water"]
            resources["coffee"] -= MENU[flavour_prompt]["ingredients"]["coffee"]

            print("Please insert coins.")
            quarte = int(input("How many quarters?: "))
            dim = int(input("How many dimes?: "))
            nickle = int(input("How many nickles?: "))
            penni = int(input("How many pennies?: "))
            sold = coins(quart=quarte, dime=dim, nick=nickle, penny=penni, flavor=flavour_prompt,
                         cost=MENU[flavour_prompt]["cost"], resource=resources, ingredients=MENU[flavour_prompt]["ingredients"])
            add_money = sold.split()
            if f"{flavour_prompt}☕" in add_money:
                money += MENU[flavour_prompt]["cost"]
            # code
        elif flavour_prompt == "latte":
            resources["water"] -= MENU[flavour_prompt]["ingredients"]["water"]
            resources["milk"] -= MENU[flavour_prompt]["ingredients"]["milk"]
            resources["coffee"] -= MENU[flavour_prompt]["ingredients"]["coffee"]
            quarte = int(input("How many quarters?: "))
            dim = int(input("How many dimes?: "))
            nickle = int(input("How many nickles?: "))
            penni = int(input("How many pennies?: "))
            sold = coins(quart=quarte, dime=dim, nick=nickle, penny=penni, flavor=flavour_prompt,
                         cost=MENU[flavour_prompt]["cost"], resource=resources, ingredients=MENU[flavour_prompt]["ingredients"])
            add_money = sold.split()
            if f"{flavour_prompt}☕" in add_money:
                money += MENU[flavour_prompt]["cost"]
            # code
        elif flavour_prompt == "cappuccino":
            resources["water"] -= MENU[flavour_prompt]["ingredients"]["water"]
            resources["milk"] -= MENU[flavour_prompt]["ingredients"]["milk"]
            resources["coffee"] -= MENU[flavour_prompt]["ingredients"]["coffee"]
            quarte = int(input("How many quarters?: "))
            dim = int(input("How many dimes?: "))
            nickle = int(input("How many nickles?: "))
            penni = int(input("How many pennies?: "))
            sold = coins(quart=quarte, dime=dim, nick=nickle, penny=penni, flavor=flavour_prompt,
                         cost=MENU[flavour_prompt]["cost"], resource=resources, ingredients=MENU[flavour_prompt]["ingredients"])
            add_money = sold.split()
            if f"{flavour_prompt}☕" in add_money:
                money += MENU[flavour_prompt]["cost"]
            # code
        elif flavour_prompt == "report":
            rep = report(resources["water"], resources["milk"], resources["coffee"], money)
            print(rep)
        elif flavour_prompt == "off":
            is_machine_on = False
        else:
            print("Invalid prompt")
        if sold == "Sorry, all ingredients are unavailable.":
            is_machine_on = False
        print(sold)




coffee_machine()
