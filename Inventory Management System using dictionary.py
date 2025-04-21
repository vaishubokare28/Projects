inventory = {}

while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item_id = input("Enter item ID: ")
        
        if item_id in inventory:
            print("Item already exists!")
        else:
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            
            inventory[item_id] = [name, quantity, price]
            print("Item added!")

    elif choice == "2":
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\nID\tName\t\tQuantity\tPrice")
            print("-" * 40)
            
            for item_id in inventory:
                name, quantity, price = inventory[item_id]
                print(f"{item_id}\t{name}\t\t{quantity}\t\t${price:.2f}")

    elif choice == "3":  
        item_id = input("Enter item ID to update: ")

        if item_id in inventory:
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            
            inventory[item_id][1] = quantity
            inventory[item_id][2] = price
            print("Item updated!")
        else:
            print("Item not found!")

    elif choice == "4":
        item_id = input("Enter item ID to delete: ")

        if item_id in inventory:
            del inventory[item_id]
            print("Item deleted!")
        else:
            print("Item not found!")

    elif choice == "5":
        print("Exiting. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
