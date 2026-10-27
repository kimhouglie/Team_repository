def calculate_total(price, quantity, discount_rate):
    subtotal=price * quantity
    discounted=subtotal * (1-discount_rate)
    return int(discounted)
print(calculate_total(1500,3,0))
print(calculate_total(5000,3,0.1))
print(calculate_total(5000,3,0.155))
