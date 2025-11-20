class InvoiceItem:
    def __init__(self, product_name, barcode, unit_price, quantity):
        self.product_name = product_name
        self.barcode = barcode
        self.unit_price = unit_price
        self.quantity = quantity

    def line_total(self):
        sales = self.unit_price * self.quantity
        return sales
    
i1 = InvoiceItem("Hoover", "6473838", 20, 500)
print(i1.line_total())

class Invoice:
    def __init__(self, invoice_id, customer_name):
        self.invoice_id = invoice_id
        self.customer_name = customer_name
        self.items =[]

    def add_items(self, items)
        self.items.append

        
