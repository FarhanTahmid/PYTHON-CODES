def makePizza(size,*toppings):
    print(f"Making {size} inch pizza with following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
makePizza(8,'pepperoni')
makePizza(16,'mushrooms','green peppers','extra cheese')
