
customers = []

def register_customer():
    cid = input("Enter customer ID: ")
    
    for customer in customers:
        if customer["id"] == cid:
            print(f"Error: Customer ID '{cid}' already exists!")
            print("Please use a different customer ID.\n")
            return False
    
    name = input("Enter customer name: ")
    address = input("Enter customer address: ")

    customers.append({
        "id": cid,
        "name": name,
        "address": address,
        "appliances": []  
    })

    print(f"Customer '{name}' registered successfully with ID: {cid}\n")
    return True

def list_customers():
    if not customers:
        print("No customers found.\n")
        return

    print("\n--- Customer List ---")
    for c in customers:
        appliance_count = len(c["appliances"])
        print(f"ID: {c['id']}, Name: {c['name']}, Address: {c['address']}, Appliances: {appliance_count}")
    print()

def get_customer_by_id(cid):
    for customer in customers:
        if customer["id"] == cid:
            return customer
    return None

def customer_exists(cid):
    return any(customer["id"] == cid for customer in customers)

def add_appliance_to_customer(cid, appliance_id):
    customer = get_customer_by_id(cid)
    if customer:
        customer["appliances"].append(appliance_id)
        return True
    return False

def get_customer_appliances(cid):
    customer = get_customer_by_id(cid)
    if customer:
        return customer["appliances"]
    return []