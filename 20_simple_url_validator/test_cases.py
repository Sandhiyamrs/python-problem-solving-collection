from solution_optimized import InvoiceGenerator

invoice = InvoiceGenerator()
data = invoice.generate(
    "John",
    [{"name": "Book", "price": 300}, {"name": "Pen", "price": 50}]
)

assert data["total"] == 350
print("Invoice generator tests passed")
