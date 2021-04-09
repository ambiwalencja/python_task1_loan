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
current_amount = (1 + ((1.592824484+3)/1200)) * last_amount - float(loan_installment)
#print(f'last amount is {last_amount}')
#print(f'interest rate is {interest_rate}')
#print(f'current amount is {current_amount}')
#print(f'difference is {last_amount-current_amount}')
print(f'January, year 1: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((-0.453509101+3)/1200)) * last_amount - float(loan_installment)
print(f'February, year 1: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((2.324671717+3)/1200)) * last_amount - float(loan_installment)
print(f'March, year 1: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.261254407+3)/1200)) * last_amount - float(loan_installment)
print(f'April, year 1: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.782526286+3)/1200)) * last_amount - float(loan_installment)
print(f'May, year 1: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((2.329384541+3)/1200)) * last_amount - float(loan_installment)
print(f'June, year 1: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.502229842+3)/1200)) * last_amount - float(loan_installment)
print(f'July, year 1: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.782526286+3)/1200)) * last_amount - float(loan_installment)
print(f'August, year 1: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((2.328848994+3)/1200)) * last_amount - float(loan_installment)
print(f'September, year 1: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((0.616921348+3)/1200)) * last_amount - float(loan_installment)
print(f'October, year 1: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((2.352295886+3)/1200)) * last_amount - float(loan_installment)
print(f'November, year 1: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((0.337779545+3)/1200)) * last_amount - float(loan_installment)
print(f'December, year 1: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.577035247+3)/1200)) * last_amount - float(loan_installment)
print(f'January, year 2: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((-0.292781443+3)/1200)) * last_amount - float(loan_installment)
print(f'February, year 2: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((2.48619659+3)/1200)) * last_amount - float(loan_installment)
print(f'March, year 2: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((0.267110318+3)/1200)) * last_amount - float(loan_installment)
print(f'April, year 2: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.417952672+3)/1200)) * last_amount - float(loan_installment)
print(f'May, year 2: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.054243267+3)/1200)) * last_amount - float(loan_installment)
print(f'June, year 2: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.480520104+3)/1200)) * last_amount - float(loan_installment)
print(f'July, year 2: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.577035247+3)/1200)) * last_amount - float(loan_installment)
print(f'August, year 2: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((-0.07742069+3)/1200)) * last_amount - float(loan_installment)
print(f'September, year 2: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.165733399+3)/1200)) * last_amount - float(loan_installment)
print(f'October, year 2: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((-0.404186718+3)/1200)) * last_amount - float(loan_installment)
print(f'November, year 2: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

last_amount = current_amount
current_amount = (1 + ((1.499708521+3)/1200)) * last_amount - float(loan_installment)
print(f'December, year 2: \nYour outstanding loan amount is {current_amount}. this is {last_amount - current_amount} less than the previous month.')

