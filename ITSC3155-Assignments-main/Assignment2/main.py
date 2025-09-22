import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    is_on = True
    while is_on:
        choice = input("What size sandwich would you like? (small/medium/large): ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slices")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slices")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounces")
        elif choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid choice. Please choose small, medium, or large.")

if __name__=="__main__":
    main()
