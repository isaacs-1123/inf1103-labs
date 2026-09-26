#global constant
tax_rate = 0.1
max_capacity = 500
inventory_file = "inventory.txt"



def get_valid_input():
    user_input = input("Please enter a stock quantity or type quit to exit: ")
    if user_input == "quit":
        return "quit"
    elif user_input.isdigit():
        return int(user_input)
    elif user_input.startswith("-"):
        print("Error, this is not a valid input. Please enter a non-negative stock quantity.")
        return None
    else:
        print("Error, this is not a valid input.")
        return None

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total  

def calculate_tax(amount):
    tax = amount * tax_rate
    return tax

def generate_report(total_units, failed_attempts):
    print(f"The Total Units Processed is {total_units} and the Number of Failed/Reject Entries is {failed_attempts}")

def load_inventory():
    try:
        with open(inventory_file, "r") as file:
            lines = [line.strip() for line in file if line.strip()]
            if lines and lines[0].isdigit():
                inventory = int(lines[0])
                transaction_history = [int(line) for line in lines[1:] if line.isdigit()]
                return inventory, transaction_history
    except FileNotFoundError:
        pass

    return 0, []


def save_inventory(inventory, transaction_history):
    with open(inventory_file, "w") as file:
        file.write(f"{inventory}\n")
        
        for amount in transaction_history:
            file.write(f"{amount}\n")




def main():

    inventory = 0
    failed_input = 0 
    exit_program = False
    transaction_history = []

    inventory, transaction_history = load_inventory()

    while not exit_program:
        
        result = get_valid_input()

        if result == "quit":  
            exit_program = True

        elif result is None:
            failed_input += 1

        else:   
            
            if inventory + result > max_capacity:
                print(f"Alert! Total inventory has exceeded {max_capacity} units.")
                exit_program = True
                

            else:
                inventory = process_delivery(inventory, result)
                transaction_history.append(result)
                tax = calculate_tax(result)
                print(f"Added {result} items to inventory. Delivery tax: {tax:.2f} Total Inventory: {inventory}")

    save_inventory(inventory, transaction_history)
    generate_report(inventory, failed_input)

if __name__ == "__main__":
    main()