# eutilitycalculator/calculators/BillCalculator.py

def calculate_bill(total_kwh):
    """Calculates the monthly bill in ETB based on consumption tiers."""
    bill_amount = 0.0
    service_charge = 0.0

    # Define tariff tiers (kwh_limit, rate, service_charge_for_tier)
    # Based on the provided image in the prompt instructions
    tiers = [
        (50, 0.2730, 10.00),
        (100, 0.7670, 42.00),
        (200, 1.6250, 42.00),
        (300, 2.0000, 42.00),
        (400, 2.2000, 42.00),
        (500, 2.4050, 42.00),
        (float('inf'), 2.4810, 42.00) # > 500 kWh
    ]

    remaining_kwh = total_kwh
    previous_limit = 0

    for limit, rate, charge in tiers:
        if total_kwh <= limit:
            # Determine service charge based on the highest tier reached
            # Using logic derived from the table structure
            if limit == 50: service_charge = 10.00
            else: service_charge = 42.00

            bill_amount += remaining_kwh * rate
            break
        else:
            kwh_in_tier = limit - previous_limit
            bill_amount += kwh_in_tier * rate
            remaining_kwh -= kwh_in_tier
            previous_limit = limit
            
    return bill_amount + service_charge