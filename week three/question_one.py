def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

amount_to_pay = calculate_discount(100, 25)
print(f"Amount to pay after discount: {amount_to_pay}")