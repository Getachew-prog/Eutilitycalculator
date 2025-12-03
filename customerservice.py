
customers = [] 

def register_customer():
    cid = input("Enter customer ID: ")
    name = input("Enter customer name: ")
    address = input("Enter customer address: ")

    customers.append({
        "id": cid,
        "name": name,
        "address": address
    })

    print("Customer registered successfully.\n")


def list_customers():
    if not customers:
        print("No customers found.\n")
        return

    print("\n-- Customer List-")
    for c in customers:
        print(f"ID: {c['id']}, Name: {c['name']}, Address: {c['address']}")
    print()