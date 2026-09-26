# Global Constants
EXIT_SIGNAL = -99
MAX_CAPACITY = 500
TAX_RATE = 0.1
INVENTORY_FILE = "inventory.txt"  

ITEM_FIELDS = {
    "id": 0,
    "name": 1,
    "quantity": 2,
    "transaction_history": 3
}

FIELD_SEPARATOR = ","
HISTORY_SEPARATOR = "|"


def find_item(inventory, item_name_or_id):
    for item in inventory:
        if (str(item[ITEM_FIELDS["id"]]).strip() == str(item_name_or_id).strip() or 
            item[ITEM_FIELDS["name"]].lower().strip() == str(item_name_or_id).lower().strip()):
            return item
    return None


def get_valid_input(item_name):
    qty_input = input("Enter Quantity: ").strip()
    
    if qty_input.lower() == "quit" or qty_input == str(EXIT_SIGNAL):
        return EXIT_SIGNAL, 0
        
    if qty_input.isdigit():
        return int(qty_input), 0
    elif qty_input.startswith("-"):
        print("Error, this is not a valid input. Please enter a non-negative stock quantity.")
        return None, 1
    else:
        print("Error, this is not a valid input.")
        return None, 1


def process_delivery(item, new_quantity):
    item[ITEM_FIELDS["quantity"]] += new_quantity
    item[ITEM_FIELDS["transaction_history"]].append(new_quantity)
    return None


def calculate_tax(amount, tax_rate):
    return amount * tax_rate


def display_inventory(inventory):
    print("Current Orders:\n")
    for item in inventory:
        item_id = item[ITEM_FIELDS["id"]]
        name = item[ITEM_FIELDS["name"]]
        quantity = item[ITEM_FIELDS["quantity"]]
        print(f"{item_id}, {name}, {quantity}")
    print()
    return None


def display_status(item, valid_quantity, tax_amount):
    item_id = item[ITEM_FIELDS["id"]]
    name = item[ITEM_FIELDS["name"]]
    print("\nNew Order Added:")
    print(f"{item_id},{name},{valid_quantity}\n")
    return None


def generate_report(inventory, failed_entries):
    total_units = sum(item[ITEM_FIELDS["quantity"]] for item in inventory)
    print(f"\nThe Total Units in inventory is {total_units} and the Number of Failed/Reject Entries is {failed_entries}")
    return None


def load_inventory():
    inventory = []
    try:
        with open(INVENTORY_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(FIELD_SEPARATOR)
                if len(parts) >= 3:
                    item_id = parts[ITEM_FIELDS["id"]]
                    name = parts[ITEM_FIELDS["name"]]
                    quantity = int(parts[ITEM_FIELDS["quantity"]])
                    
                    history = []
                    if len(parts) > ITEM_FIELDS["transaction_history"] and parts[ITEM_FIELDS["transaction_history"]]:
                        history = [
                            int(x) for x in parts[ITEM_FIELDS["transaction_history"]].split(HISTORY_SEPARATOR) 
                            if x.strip().isdigit()
                        ]
                    
                    inventory.append([item_id, name, quantity, history])
    except FileNotFoundError:
        item1 = ["1001", "Wireless Mouse", 2, [2]]
        item2 = ["1002", "Keyboard", 1, [1]]
        item3 = ["1003", "USB Cable", 3, [3]]
        inventory = [item1, item2, item3]

    return inventory


def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        for item in inventory:
            item_id = item[ITEM_FIELDS["id"]]
            name = item[ITEM_FIELDS["name"]]
            quantity = item[ITEM_FIELDS["quantity"]]
            history_list = item[ITEM_FIELDS["transaction_history"]]
            
            history_str = HISTORY_SEPARATOR.join(str(h) for h in history_list)
            file.write(f"{item_id}{FIELD_SEPARATOR}{name}{FIELD_SEPARATOR}{quantity}{FIELD_SEPARATOR}{history_str}\n")
    return None


def main():
    failed_entries = 0
    exit_program = False

    inventory = load_inventory()
    display_inventory(inventory)

    while not exit_program:
        product_name = input("Enter Product Name/ID or type quit to exit: ").strip()
        
        if product_name.lower() == "quit":
            break
            
        selected_item = find_item(inventory, product_name)
        
        if not selected_item:
            next_id = str(1001 if not inventory else int(max(item[ITEM_FIELDS["id"]] for item in inventory)) + 1)
            selected_item = [next_id, product_name, 0, []]
            new_product = True
        else:
            new_product = False

        quantity_result, failed_count = get_valid_input(product_name)
        failed_entries += failed_count

        if quantity_result == EXIT_SIGNAL:
            exit_program = True
        elif quantity_result is not None:
            current_total_units = sum(item[ITEM_FIELDS["quantity"]] for item in inventory)
            
            if current_total_units + quantity_result > MAX_CAPACITY:
                print(f"Alert! Total inventory has exceeded {MAX_CAPACITY} units.")
                exit_program = True
            else:
                if new_product:
                    inventory.append(selected_item)
                
                process_delivery(selected_item, quantity_result)
                tax = calculate_tax(quantity_result, TAX_RATE)
                display_status(selected_item, quantity_result, tax)

    save_inventory(inventory)
    print("Transactions has been successfully saved to inventory.txt")
    generate_report(inventory, failed_entries)


if __name__ == "__main__":
    main()