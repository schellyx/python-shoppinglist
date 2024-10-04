shoppinglist = []

def add_item():
     item = input("please enter the articel you would like to add to the list:")
     if item:
        shoppinglist.append(item)
        print(f"your item {item} has been successfull added")
     else:
        print("empty input, please enter a articel")

def show_shoppinglist():
        if shoppinglist:
            print("your shoppinglist:")
            for item in shoppinglist:
                print(item)
        else:
            print("shoppinglist is empty")

def main():
    while True:
        print("\n --- shoppinglist ---")
        print("\n 1. add articel")
        print("\n 2. show shoppinglist")
        print("\n 3. stop programm")
        choice = input("please choose an option: \n")
        print(type(choice))

        if choice == "1":
             print("you've chosen option 1!")
             add_item()
        elif choice == "2":
             print("you've chosen option 2!")
             show_shoppinglist()
        elif choice == "3":
             print("you've chosen option 3! Good Bye!")
             break
        else:
             print("Please select one of the mentioned options.")
             
main()