from Database import add_item, select_items, update_item, delete_item, create_table
shoppinglist = []

def add():
     add_item("Cherry", 1, 2.50)
     return
     item = input("please enter the articel you would like to add to the list:")
     if item:
        shoppinglist.append(item)
        print(f"your item {item} has been successfull added")
     else:
        print("empty input, please enter a articel")

def show_shoppinglist():
     shoppinglist = select_items()
     if shoppinglist:
          print("your shoppinglist:")
     for item in shoppinglist:
          print(item)
     else:
          print("shoppinglist is empty")

def update():
     select = input("Please enter id")
     
     try:
          id = int(select)
          name = input("Please enter item name")
          price_input = input("please enter a price")
          price = float(price_input)
          amount_input = input("please enter an amount")
          amount = int(amount_input)

          update_item(id, name, amount, price)
     except:
          print("Please enter a number")

def delete():
     select = input("Please enter id")

     try:
          id = int(select)
          delete_item(id)
     except:
          print("Please enter a number")

def main():
     create_table()
     while True:
          print("\n --- shoppinglist ---")
          print("\n 1. add articel")
          print("\n 2. show shoppinglist")
          print("\n 3. ubdate shoppinglist")
          print("\n 4. delete item")
          print("\n 5. stop programm")
          choice = input("please choose an option: \n")
          print(type(choice)) 
          if choice == "1":
               print("you've chosen option 1!")
               add()
          elif choice == "2":
               print("you've chosen option 2!")
               show_shoppinglist()
          elif choice == "3":
               print("you've chosen option 3!")
               update()
          elif choice == "4":
               print("you've chosen option 4!")
               delete()
          elif choice == "5":
               print("you've chosen option 3! Good Bye!")
               break
          else:
               print("Please select one of the mentioned options.")

main()