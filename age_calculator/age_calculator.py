from datetime import date

def interactive_age_calculator():
    print("--- Python Age Calculator ---")
    try:
        year = int(input("Enter birth year (e.g., 1998): "))
        month = int(input("Enter birth month (1-12): "))
        day = int(input("Enter birth day (1-31): "))
        
        birth_date = date(year, month, day)
        today = date.today()
        
        
        if birth_date > today:
            print("Error: Birth date cannot be in the future.")
            return

        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        print(f"\nYou are exactly {age} years old.")
        
    except ValueError:
        print("Error: Please enter valid numbers and calendar dates.")


interactive_age_calculator()
