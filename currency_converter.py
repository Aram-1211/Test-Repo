
def currency_converter(amount, from_currency, to_currency):
    
    conversion_rate = {
    'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
    'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
    'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
    'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }
    final_amount = round(amount * conversion_rate[from_currency][to_currency], 2)
    if final_amount < 0:
        final_amount = 0.0
    return final_amount

# Submit only this file currency_converter.py with the completed function.
# Do not add additional code for calling the function, or code to get user input.