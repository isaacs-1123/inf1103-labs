inventory = 0
input_quantity = 0
failed_input = 0

while input_quantity != "quit":
    if inventory >500:
        print("Alert! Total inventory has exceeded 500 units.")
        break 
    else:    
        input_quantity = input("Please enter a stock quantity: ")
        if input_quantity == "quit":
            print("The Total Units Processed is", inventory, "and the Number of Failed/Reject Entries is",failed_input)
            input_quantity = "quit"
            
        elif input_quantity.isdigit():
            inventory += int(input_quantity)
            
        else:
            print("Error, this is not a valid input")
            failed_input +=1