# eutilitycalculator/customers/CustomerService.py

def create_customer(customer_id, name):
    """Creates a customer dictionary structure."""
    return {
        'id': customer_id,
        'name': name,
        'appliances': []  # List to store appliance dictionaries
    }

def get_customer(customers_list, customer_id):
    """Finds a customer dictionary in the list by ID."""
    for customer in customers_list:
        if customer['id'] == customer_id:
            return customer
    return None

def register_customer(customers_list, customer_id, name):
    """Registers a new customer into the main customers list."""
    if get_customer(customers_list, customer_id):
        print(f"Error: Customer with ID {customer_id} already exists.")
        return
    
    new_customer = create_customer(customer_id, name)
    customers_list.append(new_customer)
    print(f"Customer '{name}' registered successfully.")

def list_customers(customers_list):
    """Lists all registered customers."""
    if not customers_list:
        print("No customers registered yet.")
        return
    print("\n--- Registered Customers ---")
    for customer in customers_list:
        print(f"ID: {customer['id']}, Name: {customer['name']}")
    print("----------------------------\n")