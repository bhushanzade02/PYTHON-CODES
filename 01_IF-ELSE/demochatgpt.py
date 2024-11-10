a = 15
b = 4
c = 3

"""Addition: Find the sum of a and b.
Subtraction: Find the difference between a and b.
Multiplication: Find the product of a and c.
Division: Find the quotient of a divided by b.
Floor Division: Find the result of floor division of a by b.
Modulus: Find the remainder when a is divided by b.
Exponentiation: Find the value of b raised to the power of c


add=a+b
print(add)

sub=a-b
print(sub)

mul=a*c
print(mul)

div=a/b
print(div)

floordiv=a//b
print(floordiv)

mod=a%b
print(mod)

exp=b**c
print(exp)

temp=mod+a
print(temp) """



total_income = 8500   # Total monthly income in dollars
total_expenses = 4235  # Total monthly expenses in dollars
tax_rate = 0.12   # Tax rate as a decimal (12%)
bonus_percentage = 0.05  # Bonus as a percentage of income (5%)
initial_savings = 1200  # Initial savings balance
monthly_savings_goal = 300  # Monthly savings goal in dollars



net_profit=total_income-total_expenses
print(net_profit)

tax=tax_rate * net_profit


print("net_profit after deduction of tax")
net_profit-=tax
print(net_profit)



bonus=total_income*bonus_percentage
print(bonus)