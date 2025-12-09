# eutilitycalculator/appliances/ApplianceService.py

def create_appliance(name, wattage, hours_per_day, days_per_month):
    """Creates an appliance dictionary structure."""
    return {
        'name': name,
        'wattage': wattage,
        'hours_per_day': hours_per_day,
        'days_per_month': days_per_month
    }

def register_appliance(customer_dict, name, wattage, hours_per_day, days_per_month):
    """Registers a new appliance into a specific customer's appliances list."""
    if customer_dict is None:
         print("Error: Invalid customer data.")
         return
    
    new_appliance = create_appliance(name, wattage, hours_per_day, days_per_month)
    customer_dict['appliances'].append(new_appliance)
    print(f"Appliance '{name}' added for customer '{customer_dict['name']}'.")

def list_appliances(customer_dict):
    """Lists all appliances for a given customer dictionary."""
    if customer_dict is None:
        print("Error: Invalid customer data.")
        return
    
    appliances_list = customer_dict['appliances']
    if not appliances_list:
        print(f"No appliances registered for {customer_dict['name']}.")
        return

    print(f"\n--- Appliances for {customer_dict['name']} ---")
    for app in appliances_list:
        print(f"Appliance: {app['name']}, Wattage: {app['wattage']}W, "
              f"Usage: {app['hours_per_day']} hrs/day for {app['days_per_month']} days/month")
    print("------------------------------------\n")