def get_input(prompt, converter):
    """A pure function to get and convert user input"""
    while True:
        try:
            return converter(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def calculate_total_with_tip(bill_amount, tip_percent):
    """Pure function to calculate total with tip"""
    return bill_amount * (1 + tip_percent / 100)

print("Hello, let's help you calculate your total bill including that tip! ")

total_bill = float(input("How much was the total bill? R "))

percentage_tip = int(input("What percentage tip would you like to give?(Only input numbers and not the percent(%) symbol "))

split = int(input("How many people are splitting the bill? "))

bill_with_tip = percentage_tip/100 * total_bill + total_bill

bill_per_person = round(bill_with_tip/split,2)

print(f"The total bill is R{bill_per_person}.")