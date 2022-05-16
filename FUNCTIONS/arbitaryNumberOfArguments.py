def makePizza(*toppings):
    print("Making pizza with following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
makePizza('pepperoni')
makePizza('mushrooms','green peppers','extra cheese')
