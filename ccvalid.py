#Credit card

card_number = str(input("Enter credit card number you want to check: "))

# Reverse the credit card number and take the digits in the odd positions and then the digits in the even positions
#
# Add up all the digits in the odd positions into a total.
#
# Multiply every even-positioned digit by two;
#   if the product is greater than 9 (e.g. 8 * 2 = 16),
#      then subtract 9 and add the result to the total.
#   Otherwise add the multiplication product to the total.
#
# If the total is divisible by 10 (the remainder after division by 10 is equal to 0 or the number ends in a zero);
#   then the credit card number is valid.


reversed_card_number = card_number[::-1]

even_digits = reversed_card_number[1::2]
odd_digits = reversed_card_number[0::2]

total = 0
for odd in odd_digits:
    total += int(odd)

multiplied = 0
for even in even_digits:
    multiplied = int(even)*2

    if multiplied > 9 :
        total += (multiplied - 9)
    else:
        total += multiplied

print(card_number)

if total % 10 == 0:
    print('valid')

else:
    print('Your credit card number is not valid. Please check for any typos.')
