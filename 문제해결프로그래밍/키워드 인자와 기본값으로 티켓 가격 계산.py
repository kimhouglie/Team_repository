def ticket_price(base=12000, student=False, weekend=False):
    price = base
    if student:
        price *= 0.8
    if weekend:
        price += 2000
    return int(price)

print(ticket_price())
print(ticket_price(student=True))
print(ticket_price(student=True, weekend=True))
