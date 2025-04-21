class Inventory:
    def __init__(self):
        self.inventory = {} # Initialize the inventory dictionary


    def add_item(self, item_id, name, quantity, price): #Add a new item to the inventory
        if item_id in self.inventory:
            print(f"\nItem ID '{item_id}' already exists!")  # Check for duplicate IDs
        else:
            self.inventory[item_id] = [name, quantity, price]  # Add values to dictionary
            print(f"\n{name} added successfully!")


    def display_inventory(self): # Display the current inventory in table format
        if not self.inventory:
            print("\nInventory is empty.")
        else:
            print("\n{:<10}{:<15}{:<10}{:<10}".format("ID", "Name", "Quantity", "Price"))
            print("-" * 50)

            for item_id, (name, quantity, price) in self.inventory.items():
                print(f"{item_id:<10}{name:<15}{quantity:<10}{price:<10.2f}")


    def update_item(self, item_id, quantity, price): # Update quantity and price of an existing item
        if item_id in self.inventory:
            self.inventory[item_id][1] = quantity  # Update quantity
            self.inventory[item_id][2] = price     # Update price
            print(f"\n{self.inventory[item_id][0]} updated successfully!")
        else:
            print("\nItem ID not found!")


    def delete_item(self, item_id): # Delete an item from the inventory
        if item_id in self.inventory:
            del self.inventory[item_id]  # Remove the item from dictionary
            print("\nItem deleted successfully!")
        else:
            print("\nItem ID not found!")


inventory = Inventory()

while True:
    print("\n------ Inventory Management System ------")
    print(
    """
    1. Add Item
    2. View Inventory
    3. Update Item
    4. Delete Item
    5. Exit
    """)

    choice = input("Choose an option: ")

    # Add Item
    if choice == "1":   
        print("\n--- Add New Item ---")
        item_id = input("Enter item ID: ")
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory.add_item(item_id, name, quantity, price)


    # View Inventory
    elif choice == "2":  
        print("\n--- Current Inventory ---")
        inventory.display_inventory()


    # Update Item
    elif choice == "3":  
        print("\n--- Update Item ---")
        item_id = input("Enter item ID to update: ")

        if item_id in inventory.inventory:
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory.update_item(item_id, quantity, price)
        else:
            print("\nItem ID not found!")


    # Delete Item
    elif choice == "4":
        print("\n--- Delete Item ---")
        item_id = input("\nEnter item ID to delete: ")
        inventory.delete_item(item_id)


    # Exit
    elif choice == "5":  
        print("\nExiting the Inventory Management System. Goodbye!\n")
        break


    else:
        print("\nInvalid choice. Try again.")
