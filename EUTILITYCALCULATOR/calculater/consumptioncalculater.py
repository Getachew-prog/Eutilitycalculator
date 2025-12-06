
def calculate_monthly_kwh(appliances):
    total_kwh = 0
    print("\n--- Monthly Consumption Per Appliance ---")
    for a in appliances:
        kw = a['watt'] / 1000
        daily_kwh = kw * a['quantity'] * a['hours']
        monthly_kwh = daily_kwh * 30
        total_kwh += monthly_kwh

        print(f"{a['name']}: {monthly_kwh:} kWh")
    print(f"\nTOTAL Monthly Energy Consumption = {total_kwh:} kWh")
    return total_kwh