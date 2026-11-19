import csv
import json
from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory

INVENTORY_FILE = "inventory.json"


def load_inventory() -> list[dict]:
    try:
        with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_inventory(data: list[dict]) -> None:
    try:
        with open(INVENTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except OSError as e:
        print(f"Error saving inventory: {e}")


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="", encoding="utf-8")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0
        with file:
            reader = csv.reader(file)
            next(reader, None)  # skip header row
            for row_num, row in enumerate(reader, start=2):
                if not row:
                    continue
                try:
                    product_type = row[0].strip()
                    product_id = row[1].strip()
                    name = row[2].strip()
                    price = float(row[3].strip())
                    stock_quantity = int(row[4].strip())

                    product = ProductFactory.create(
                        product_type, product_id, name, price, stock_quantity, 0.0, supplier
                    )
                    inventory.add_product(product)
                    loaded += 1
                except (ValueError, IndexError) as e:
                    print(f"Skipping invalid row {row_num} ({row}): {e}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")