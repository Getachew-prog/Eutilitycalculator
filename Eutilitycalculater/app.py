

# Import functions from modules
from customer import customerservice as cs
from applaince import applainceservice as asvc
from calculater import consumptioncalculater as cc
from calculater import billcalculater as bc

# Main data storage: A list of customer dictionaries
customers_db = []

def main_menu():
    print("\n=== E-Utility Calculator Main Menu ===")
    print("1. Customer")
    print("2. Appliance")
    print("3. Consumption")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    return choice

def handle_customer_menu():
    print("\n--- Customer Menu ---")
    print("1. Register Customer")
    print("2. List Customers")
    choice = input("Enter your choice : ")

    if choice == '1':
        customer_id = input("Enter Customer ID: ")
        name = input("Enter Customer Name: ")
        
        # Pass the main database list to the function
        cs.register_customer(customers_db, customer_id, name)
    elif choice == '1':
        # Pass the main database list to the function
        cs.list_customers(customers_db)
    else:
        print("Invalid choice.")

def handle_appliance_menu():
    print("\n--- Appliance Menu ---")
    customer_id = input("Enter Customer ID to manage appliances: ")
    # Find the specific customer dict
    customer_dict = cs.get_customer(customers_db, customer_id)
    
    if not customer_dict:
        print("Customer not found.")
        return

    print("1. Register Appliance")
    print("2. List Appliances")
    choice = input("Enter your choice : ")

    if choice == '1':
        try:
            name = input("Enter Appliance Name: ")
            wattage = float(input("Enter Wattage (W): "))
            hours = float(input("Enter Hours used per day: "))
            days = int(input("Enter Days used per month: "))
            # Pass the specific customer dictionary to receive the appliance
            asvc.register_appliance(customer_dict, name, wattage, hours, days)
        except ValueError:
            print("Invalid input. Please enter numeric values for wattage, hours, and days.")
    elif choice == '2':
        asvc.list_appliances(customer_dict)
    else:
        print("Invalid choice.")

def handle_consumption_menu():
    print("\n--- Consumption & Bill Calculation ---")
    customer_id = input("Enter Customer ID to calculate bill: ")
    customer_dict = cs.get_customer(customers_db, customer_id)

    if not customer_dict:
        print("Customer not found.")
        return

    if not customer_dict['appliances']:
        print("No appliances registered for this customer. Cannot calculate bill.")
        return

    # Calculate total monthly consumption using the customer dict
    total_kwh = cc.calculate_monthly_consumption(customer_dict)
    
    # Calculate total bill amount using the resulting kWh
    total_bill = bc.calculate_bill(total_kwh)

    print(f"\n--- Bill Details for {customer_dict['name']} ---")
    print(f"Total Monthly Consumption: {total_kwh:.2f} kWh")
    print(f"Total Bill Amount: {total_bill:.2f} ETB")
    print("------------------------------------\n")


def main():
    while True:
        choice = main_menu()
        if choice == '1':
            handle_customer_menu()
        elif choice == '2':
            handle_appliance_menu()
        elif choice == '3':
            handle_consumption_menu()
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()