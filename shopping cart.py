import time

grocery_items = ["tomatoes", "potatoes", "onions", "carrots", "apples", "bananas", "mangos", "oranges"]
prices = [120, 80, 100, 90, 250, 150, 300, 200,]
print(grocery_items)

#EHHHEHEHHHEHEHEHEHEHEHEHHE

cart = []     
price_cart = []

person_wants = input("Would you like to modify your cart? (Y/N): ").lower()
person_wantsTF = False

if person_wants == "yes" or person_wants == "y":
    person_wantsTF = True
elif person_wants == "no" or person_wants == "n":
    Usure = input("Are you sure? (Y/N): ").lower()
    if Usure == "yes" or Usure == "y":
        print("Okay, no changes will be made to your cart.")
        person_wantsTF = False
    elif Usure == "no" or Usure == "n": 
        print("Alright, you can still modify your cart.")
        person_wantsTF = True
    else:
        print("Invalid option.")
else:
    print("Invalid option.")

while person_wantsTF == True:
    person_need = input("what would you like to do, add an item from the following, remove an item from cart or proceed with the total? A/R/T (<- reply with letters) ").lower()
    if person_need == "a":
        item_want = input("what item do you want to add? ").lower()
        if item_want in grocery_items:
            cart.append(item_want)
            ind_want = grocery_items.index(item_want)
            priceses = price_cart.append(prices[ind_want])
            time.sleep(1)
            print(f"{cart} -item has been added to the cart!")
            time.sleep(2)
        else:
            print("not in the grocery items.. lets try this again.")
            time.sleep(1.9)
            continue
    elif person_need == "r":
        item_remove = input("what Item do you want to remove from your cart? ")
        time.sleep(1.3)
        if item_remove in cart:
            cart.remove(item_remove)
            print(f"{cart} -item has been removed from cart!")
            time.sleep(2)

        else:
            print("invalid option")
            continue
    elif person_need == "t":
        total_cart = sum(price_cart)
        if total_cart == 0:
            print("you know you can add items to your cart..")
        else:
            print(f"the sum of the item/items in your cart is {total_cart}RS")
        break
    else:
        print("pick a proper option")
else:
    print("Maybe try again")