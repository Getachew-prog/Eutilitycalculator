# eutilitycalculator/calculators/ConsumptionCalculator.py

def calculate_monthly_consumption(customer_dict):
    """Calculates total monthly kWh consumption from a customer dictionary."""
    total_kwh = 0
    if customer_dict is None:
        return 0
        
    for appliance in customer_dict['appliances']:
        # Calculate monthly consumption for one appliance in Wh
        monthly_wh = appliance['wattage'] * appliance['hours_per_day'] * appliance['days_per_month']
        # Convert to kWh and add to total
        total_kwh += monthly_wh / 1000
    return total_kwh