dev = "Zomato"
def hotel():
    item = "Fried Rice"
    def order():
        quantity = 1
        print(f"You order {quantity} {item} from {dev}")
    order()
hotel()