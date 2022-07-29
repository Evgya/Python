def get_customers_purchases(filename="input.txt"):
    _file = open(filename)
    customers = dict()
    for line in _file:
        purchase = line.split()
        customer_purchases = customers.setdefault(purchase[0], dict())
        customer_purchases[purchase[1]] =\
            customer_purchases.setdefault(purchase[1], 0) + int(purchase[2])
    _file.close()
    return customers

customers_purchases = get_customers_purchases()
for customer in sorted(customers_purchases.keys()):
    purchases = customers_purchases[customer]
    print(customer + ":")
    for purchase in sorted(purchases.keys()):
        print(purchase + ' ' + str(purchases[purchase]))
