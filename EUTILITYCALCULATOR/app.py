
from customer.customerservice import register_customer, list_customers
from appliance.applianceservice import register_appliance, list_appliances, appliances
from calculator.consumptioncalculator import calculate_monthly_kwh
from calculator.billcalculater import calculate_bill
def main_menu():
    while True:
        print("\n------ Electricity Billing System ------")
        print("1. Customer")
        print("2. Appliance")
        print("3. Consumption & Bill")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            print("\n1. Register Customer")
            print("2. List Customers")
            sub = input("Enter choice: ")

            if sub == "1":
                register_customer()
            elif sub == "2":
                list_customers()

        elif choice == "2":
            print("\n1. Register Appliance")
            print("2. List Appliances")
            sub = input("Enter choice: ")

            if sub == "1":
                register_appliance()
            elif sub == "2":
                list_appliances()

        elif choice == "3":
            if not appliances:
                print("No appliances added yet.\n")
                continue

            total_kwh = calculate_monthly_kwh(appliances)
            calculate_bill(total_kwh)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main_menu()