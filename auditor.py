inventory = 0
input_quantity = 0

while input_quantity != "quit":
        input_quantity = input("Please enter a stock quantity: ")
        if input_quantity == "quit":
            input_quantity = "quit"
            
        elif input_quantity.isdigit():
            inventory += int(input_quantity)
            
        else:
            print("Error, this is not a valid input")
