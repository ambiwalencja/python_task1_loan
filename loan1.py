#setting the inflation value

#welcome message
print("Hello. welcome to our brilliant loan calculator! Let's begin!")
#getting the loan information from the user
loan_amount = input("Type the loan amount:")
interest_rate = input("Type the interest rate of your loan:")
loan_installment = input("And now type the loan installment:")
total_loan_amount = (1 + float(interest_rate)) * float(loan_amount)
#checking if everything went correctly so far
print("Your total loan amount is: ", total_loan_amount)

#calculating the outstanding loan amount in each month
last_amount = total_loan_amount
current_amount = (1 + ((1.592824484+3)/1200)) * last_amount - float(interest_rate)
print(f'January, year 1: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((-0.453509101)/1200)) * last_amount - float(interest_rate)
print(f'February, year 1: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((2.324671717)/1200)) * last_amount - float(interest_rate)
print(f'March, year 1: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((-1.261254407)/1200)) * last_amount - float(interest_rate)
print(f'April, year 1: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.782526286)/1200)) * last_amount - float(interest_rate)
print(f'May, year 1: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((2.329384541)/1200)) * last_amount - float(interest_rate)
print(f'June, year 1: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.502229842)/1200)) * last_amount - float(interest_rate)
print(f'July, year 1: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.782526286)/1200)) * last_amount - float(interest_rate)
print(f'August, year 1: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((2.328848994)/1200)) * last_amount - float(interest_rate)
print(f'September, year 1: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((0.616921348)/1200)) * last_amount - float(interest_rate)
print(f'October, year 1: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((2.352295886)/1200)) * last_amount - float(interest_rate)
print(f'November, year 1: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((0.337779545)/1200)) * last_amount - float(interest_rate)
print(f'December, year 1: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = total_loan_amount
current_amount = (1 + ((1.577035247+3)/1200)) * last_amount - float(interest_rate)
print(f'January, year 2: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((-0.292781443)/1200)) * last_amount - float(interest_rate)
print(f'February, year 2: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((2.48619659)/1200)) * last_amount - float(interest_rate)
print(f'March, year 2: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((0.267110318)/1200)) * last_amount - float(interest_rate)
print(f'April, year 2: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.417952672)/1200)) * last_amount - float(interest_rate)
print(f'May, year 2: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.054243267)/1200)) * last_amount - float(interest_rate)
print(f'June, year 2: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.480520104)/1200)) * last_amount - float(interest_rate)
print(f'July, year 2: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.577035247)/1200)) * last_amount - float(interest_rate)
print(f'August, year 2: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((-0.07742069)/1200)) * last_amount - float(interest_rate)
print(f'September, year 2: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.165733399)/1200)) * last_amount - float(interest_rate)
print(f'October, year 2: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((-0.404186718)/1200)) * last_amount - float(interest_rate)
print(f'November, year 2: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.499708521)/1200)) * last_amount - float(interest_rate)
print(f'December, year 2: Your outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

