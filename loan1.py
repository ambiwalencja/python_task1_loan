#setting the inflation value
inflation = 1.592824484
#welcome message
print("Hello. welcome to our brilliant loan calculator! Let's begin!")
#getting the loan information from the user
loan_amount = input("Type the loan amount:")
interest_rate = input("Type the interest rate of your loan:")
loan_installment = input("And now type the loan installment:")
total_loan_amount = (1 + float(interest_rate)) * float(loan_amount)
#checking if everything went correctly so far
print("Your total loan amount is: ". total_loan_amount)

