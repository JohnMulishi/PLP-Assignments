def calculate_discount(Price,discount_percent):
    if discount_percent >= 20:
        discount_amount = Price * (discount_percent/100)
        Final_price = Price - discount_amount
        return Final_price
    else:
        return Price
Original_price = float(input(" Please enter the price of the item: "))
discount_percentage = float(input("Please enter the discount percentage: ")) 
            
final_price = calculate_discount(Original_price, discount_percentage)  
print(f"The final price after applying the discount is: ${final_price:.2f}")            