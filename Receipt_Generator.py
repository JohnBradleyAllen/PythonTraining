print("Thank you for shopping at Lovely Loveseats for Neat Suites on Fleet Street!\n")
#items for sale
lovely_loveseat_description = "- Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.\n"

stylish_settee_description = "- Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.\n"

luxurious_lamp_description = "- Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.\n"

#Sale price for each item
lovely_loveseat_price = 254.00
stylish_settee_price = 180.50
luxurious_lamp_price = 52.15

#sales tax that equals 8.8%
sales_tax = .088

#Customer 1
customer_one_total = lovely_loveseat_price + luxurious_lamp_price
customer_one_itemization = lovely_loveseat_description + luxurious_lamp_description
customer_one_tax = customer_one_total + sales_tax
customer_one_final_total = customer_one_total + customer_one_tax

#Receipt
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_final_total)