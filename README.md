def calculate_total(price, quantity, discount_rate):
    subtotal=price * quantity
    discounted=subtotal * (1-discount_rate)
    return int(discounted)
print(calculate_total(1500,3,0))
print(calculate_total(5000,3,0.1))
print(calculate_total(5000,3,0.155))
<img width="59" height="46" alt="image" src="https://github.com/user-attachments/assets/0c30fdfe-d88b-41b2-9820-d022ec7bfb0e" />
