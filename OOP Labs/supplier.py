class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        self.supplier_id: str = supplier_id
        self.name: str = name
        self.contact_email: str = contact_email

    def get_supplier_id(self) -> str:
        return self.supplier_id

    def get_name(self) -> str:
        return self.name

    def get_contact_email(self) -> str:
        return self.contact_email

    def display_information(self) -> None:
        print(f"Supplier ID: {self.supplier_id} | Name: {self.name} | Email: {self.contact_email}")