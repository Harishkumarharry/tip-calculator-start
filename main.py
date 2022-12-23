#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.\n")
total_Bill = input("What was the total bill? ")
tip_Percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_People = input("How many people to split the bill? ")

total_Bill_Float = float(total_Bill)
tip_Percentage_Int = int(tip_Percentage)
num_People_Int = int(num_People)

tip_Calc = total_Bill_Float * (tip_Percentage_Int / 100)

total_amount = total_Bill_Float + tip_Calc

per_Person = round(total_amount/num_People_Int, 2)

print(f"Each person should pay : ${per_Person}")