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

"""
inflation = 2.324671717
inflation = 1.261254407
inflation = 1.782526286
inflation = 2.329384541
inflation = 1.502229842
inflation = 1.782526286
inflation = 2.328848994
inflation = 0.616921348
inflation = 2.352295886
inflation = 0.337779545
inflation = 1.577035247
inflation = -0.292781443
inflation = 2.48619659
inflation = 0.267110318
inflation = 1.417952672
inflation = 1.054243267
inflation = 1.480520104
inflation = 1.577035247
inflation = -0.07742069
inflation = 1.165733399
inflation = -0.404186718
inflation = 1.499708521
"""