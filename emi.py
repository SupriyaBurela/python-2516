actual_price=float(input("enter price"))
down_payment=float(input("enter down payment"))
bank_interest_rate=float(input("enter rate of interest"))
loan_period=int(input("enter period of loan"))
principal_loan_amount=actual_price-down_payment
monthly_interest_rate=bank_interest_rate/(12*100)
total_months=loan_period*12
emi=(principal_loan_amount*monthly_interest_rate*(1+monthly_interest_rate)**total_months)/((1+monthly_interest_rate)**total_months-1)
print(f"The total amount of emi{emi}")