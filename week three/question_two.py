# question one code
def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


original_price =  int(input("Enter the original price: "))
print(f"Original price: {original_price}")
discount = int(input("Enter the discount percentage: "))
print(f"Discount percentage: {discount}")
amount_to_pay = calculate_discount(original_price,discount)
print(f"Amount to pay after discount: {amount_to_pay}")

