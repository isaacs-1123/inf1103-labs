inventory = 0
input_quantity = 0
failed_input = 0

def get_valid_input():
    user_input = input("Please enter a stock quantity or type quit to exit: ")
    if user_input == "quit":
        return "quit"
    elif user_input.isdigit():
        return int(user_input)
    else:
        print("Error, this is not a valid input.")
        return None

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total  

while input_quantity != "quit":
    result = get_valid_input()

    if result == "quit":  
        print("The Total Units Processed is", inventory, "and the Number of Failed/Reject Entries is",failed_input) 
        input_quantity = "quit"

    elif result is None:
        failed_input += 1

    else:
        input_quantity = result
        inventory = process_delivery(inventory, result)
        if inventory >500:
            print("Alert! Total inventory has exceeded 500 units.")
            break 

        else:
            print("Added", input_quantity, "items to inventory. Total Inventory:",inventory)




    


