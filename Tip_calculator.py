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

def calculate_per_person_amount(total_amount, num_people):
    """Pure function to calculate amount per person"""
    return round(total_amount / num_people, 2)

def main():
    """Main function to orchestrate the program flow"""
    print("Hello, let's help you calculate your total bill including that tip!")
    
    # Get inputs using pure functions
    total_bill = get_input("How much was the total bill? R ", float)
    percentage_tip = get_input("What percentage tip would you like to give? (Only input numbers) ", int)
    split = get_input("How many people are splitting the bill? ", int)
    
    # Perform calculations using pure functions
    bill_with_tip = calculate_total_with_tip(total_bill, percentage_tip)
    bill_per_person = calculate_per_person_amount(bill_with_tip, split)
    
    # Output the result
    print(f"The total bill per person is R{bill_per_person}.")

if __name__ == "__main__":
    main()
