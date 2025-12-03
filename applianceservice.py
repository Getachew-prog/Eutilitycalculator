
appliances = []   
def register_appliance():
    name = input("Appliance name: ")
    watt = float(input("Wattage (W): "))
    quantity = int(input("Quantity: "))
    hours = float(input("Hours used per day: "))

    appliances.append({
        "name": name,
        "watt": watt,
        "quantity": quantity,
        "hours": hours
    })

    print("Appliance saved.\n")


def list_appliances():
    if not appliances:
        print("No appliances found.\n")
        return

    print("\n--- Appliance List ---")
    for a in appliances:
        print(f"{a['name']} : {a['watt']}W, Quantity: {a['quantity']}, usage hours/day: {a['hours']}")
    print()