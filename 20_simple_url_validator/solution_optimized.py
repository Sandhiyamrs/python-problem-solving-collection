class InvoiceGenerator:
    def generate(self, customer, items):
        invoice = {
            "customer": customer,
            "items": items,
            "total": sum(item["price"] for item in items)
        }
        return invoice
