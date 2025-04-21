"""LIC Management System
Description:
A Python application for managing customers, policies, and claims in an insurance system. 

Features
1.Customer Management:
Add, view, and delete customers.
2.Policy Management:
Create and view policies.
3.Claim Management:
File and view claims (linked to customers).
4.Reports:
Displays total customers, policies, and claims."""


customers = {}
policies = {}
claims = {}

while True:
    print("\n--- LIC Management System ---")
    print("1. Customer Management")
    print("2. Policy Management")
    print("3. Claim Management")
    print("4. Reports")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '5':  
        print("Exiting the system.")
        break

    elif choice == '1':  
        while True:
            print("\n--- Customer Management ---")
            print("1. Add Customer")
            print("2. View Customers")
            print("3. Delete Customer")
            print("4. Back")

            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':  
                customer_id = input("Enter Customer ID: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                policy = input("Enter Policy Name: ")
                premium = float(input("Enter Premium Amount: "))

                customers[customer_id] = {
                    "Name": name, 
                    "Age": age, 
                    "Policy": policy, 
                    "Premium": premium
                }
                print(f"Customer {name} added successfully!")

            elif sub_choice == '2':  
                print("\n--- Customer List ---")
                if customers:
                    print("{:<10} {:<15} {:<10} {:<15} {:<10}".format("ID", "Name", "Age", "Policy", "Premium"))
                    print("=" * 60)
                    for cid, data in customers.items():
                        print("{:<10} {:<15} {:<10} {:<15} ₹{:<10.2f}".format(
                            cid, data["Name"], data["Age"], data["Policy"], data["Premium"]
                        ))
                else:
                    print("No customers found.")

            elif sub_choice == '3':  
                cust_id = input("Enter Customer ID to delete: ")
                if cust_id in customers:
                    del customers[cust_id]
                    print("Customer deleted successfully.")
                else:
                    print("Customer not found.")
                    
            elif sub_choice == '4':  
                break  
            
            else:
                print("Invalid choice. Try again.")

    elif choice == '2':  
        while True:
            print("\n--- Policy Management ---")
            print("1. Add Policy")
            print("2. View Policies")
            print("3. Back")

            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':  
                policy_id = input("Enter Policy ID: ")
                name = input("Enter Policy Name: ")
                tenure = int(input("Enter Tenure (years): "))
                premium = float(input("Enter Premium: "))

                policies[policy_id] = {
                    "Name": name, 
                    "Tenure": tenure, 
                    "Premium": premium, 
                }
                print(f"Policy {name} added successfully!")

            elif sub_choice == '2':  
                print("\n--- Policy List ---")
                if policies:
                    print("{:<10} {:<15} {:<10} {:<15} {:<10}".format("ID", "Name", "Tenure", "Premium"))
                    print("=" * 60)
                    for pid, data in policies.items():
                        print("{:<10} {:<15} {:<10} ₹{:<15.2f} {:<10}".format(
                            pid, data["Name"], data["Tenure"], data["Premium"]
                        ))
                else:
                    print("No policies found.")

            elif sub_choice == '3':  
                break  

            else:
                print("Invalid choice. Try again.")

    elif choice == '3':  
        while True:
            print("\n--- Claim Management ---")
            print("1. Add Claim")
            print("2. View Claims")
            print("3. Back")

            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':  
                claim_id = input("Enter Claim ID: ")
                cust_id = input("Enter Customer ID: ")
                amount = float(input("Enter Claim Amount: "))

                if cust_id in customers:
                    claims[claim_id] = {
                        "Customer": cust_id, 
                        "Amount": amount
                    }
                    print("Claim added successfully.")
                else:
                    print("Customer not found!")

            elif sub_choice == '2':  
                print("\n--- Claim List ---")
                if claims:
                    print("{:<10} {:<15} {:<15}".format("Claim ID", "Customer ID", "Amount"))
                    print("=" * 45)
                    for cl_id, data in claims.items():
                        print("{:<10} {:<15} ₹{:<15.2f}".format(
                            cl_id, data["Customer"], data["Amount"]
                        ))
                else:
                    print("No claims found.")

            elif sub_choice == '3':  
                break  

            else:
                print("Invalid choice. Try again.")

    elif choice == '4':  
        print("\n--- Reports ---")

        # Customer Summary
        print(f"Total Customers: {len(customers)}")

        # Policy Summary
        print(f"Total Policies: {len(policies)}")

        # Simplified Claim Report
        print(f"Total Claims: {len(claims)}")

    else:
        print("Invalid choice. Try again.")











# # Dictionaries to store customer, policy, and claim data
# customers = {}
# policies = {}
# claims = {}

# # Main menu loop
# while True:
#     print("\n--- LIC Management System ---")
#     print("1. Customer Management")
#     print("2. Policy Management")
#     print("3. Claim Management")
#     print("4. Reports")
#     print("5. Exit")
    
#     choice = input("Enter your choice: ")

#     # Exit the system
#     if choice == '5':  
#         print("Exiting the system.")
#         break

#     # Customer Management
#     elif choice == '1':  
#         while True:
#             print("\n--- Customer Management ---")
#             print("1. Add Customer")
#             print("2. View Customers")
#             print("3. Delete Customer")
#             print("4. Back")

#             sub_choice = input("Enter your choice: ")

#             if sub_choice == '1':  # Add a new customer
#                 customer_id = input("Enter Customer ID: ")
#                 name = input("Enter Name: ")
#                 age = int(input("Enter Age: "))
#                 policy = input("Enter Policy Name: ")
#                 premium = float(input("Enter Premium Amount: "))

#                 # Store customer details in the dictionary
#                 customers[customer_id] = {
#                     "Name": name, 
#                     "Age": age, 
#                     "Policy": policy, 
#                     "Premium": premium
#                 }
#                 print(f"Customer {name} added successfully!")

#             elif sub_choice == '2':  # View all customers
#                 print("\n--- Customer List ---")
#                 if customers:
#                     print("{:<10} {:<15} {:<10} {:<15} {:<10}".format("ID", "Name", "Age", "Policy", "Premium"))
#                     print("=" * 60)
                    
#                     # Loop through customers and display details
#                     for cid, data in customers.items():
#                         print("{:<10} {:<15} {:<10} {:<15} ₹{:<10.2f}".format(
#                             cid, data["Name"], data["Age"], data["Policy"], data["Premium"]
#                         ))
#                 else:
#                     print("No customers found.")

#             elif sub_choice == '3':  # Delete a customer by ID
#                 cust_id = input("Enter Customer ID to delete: ")
#                 if cust_id in customers:
#                     del customers[cust_id]
#                     print("Customer deleted successfully.")
#                 else:
#                     print("Customer not found.")
                    
#             elif sub_choice == '4':  # Go back to the main menu
#                 break  
            
#             else:
#                 print("Invalid choice. Try again.")

#     # Policy Management
#     elif choice == '2':  
#         while True:
#             print("\n--- Policy Management ---")
#             print("1. Add Policy")
#             print("2. View Policies")
#             print("3. Back")

#             sub_choice = input("Enter your choice: ")

#             if sub_choice == '1':  # Add a new policy
#                 policy_id = input("Enter Policy ID: ")
#                 name = input("Enter Policy Name: ")
#                 tenure = int(input("Enter Tenure (years): "))
#                 premium = float(input("Enter Premium: "))

#                 # Store policy details in the dictionary
#                 policies[policy_id] = {
#                     "Name": name, 
#                     "Tenure": tenure, 
#                     "Premium": premium, 
#                 }
#                 print(f"Policy {name} added successfully!")

#             elif sub_choice == '2':  # View all policies
#                 print("\n--- Policy List ---")
#                 if policies:
#                     print("{:<10} {:<15} {:<10} {:<15} {:<10}".format("ID", "Name", "Tenure", "Premium"))
#                     print("=" * 60)
                    
#                     # Loop through policies and display details
#                     for pid, data in policies.items():
#                         print("{:<10} {:<15} {:<10} ₹{:<15.2f} {:<10}".format(
#                             pid, data["Name"], data["Tenure"], data["Premium"]
#                         ))
#                 else:
#                     print("No policies found.")

#             elif sub_choice == '3':  # Go back to the main menu
#                 break  

#             else:
#                 print("Invalid choice. Try again.")

#     # Claim Management
#     elif choice == '3':  
#         while True:
#             print("\n--- Claim Management ---")
#             print("1. Add Claim")
#             print("2. View Claims")
#             print("3. Back")

#             sub_choice = input("Enter your choice: ")

#             if sub_choice == '1':  # Add a new claim
#                 claim_id = input("Enter Claim ID: ")
#                 cust_id = input("Enter Customer ID: ")
#                 amount = float(input("Enter Claim Amount: "))

#                 # Check if the customer exists before adding a claim
#                 if cust_id in customers:
#                     claims[claim_id] = {
#                         "Customer": cust_id, 
#                         "Amount": amount
#                     }
#                     print("Claim added successfully.")
#                 else:
#                     print("Customer not found!")

#             elif sub_choice == '2':  # View all claims
#                 print("\n--- Claim List ---")
#                 if claims:
#                     print("{:<10} {:<15} {:<15}".format("Claim ID", "Customer ID", "Amount"))
#                     print("=" * 45)
                    
#                     # Loop through claims and display details
#                     for cl_id, data in claims.items():
#                         print("{:<10} {:<15} ₹{:<15.2f}".format(
#                             cl_id, data["Customer"], data["Amount"]
#                         ))
#                 else:
#                     print("No claims found.")

#             elif sub_choice == '3':  # Go back to the main menu
#                 break  

#             else:
#                 print("Invalid choice. Try again.")

#     # Generate reports
#     elif choice == '4':  
#         print("\n--- Reports ---")

#         # Display total number of customers
#         print(f"Total Customers: {len(customers)}")

#         # Display total number of policies
#         print(f"Total Policies: {len(policies)}")

#         # Display total number of claims
#         print(f"Total Claims: {len(claims)}")

#     else:
#         print("Invalid choice. Try again.")
