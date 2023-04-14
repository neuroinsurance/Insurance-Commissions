# ask users name 
user_name = input("What is your name? ")
print("Hello ,", user_name)

# Ask user if personal or commercial insurance broker
broker_type = input("are you a personal or commercial insurance broker? ")
if broker_type == "personal":
    print(user_name, "you're a personal insurance broker!")
elif broker_type == "commercial":
    print(user_name, "you're a commercial insurance broker!")

# Ask user how much new gross written premiums they sold last month
new_gwp = int(input("How much gross written premium did you sell last month? "))

# Ask how much gross written premium renewed last month
old_gwp = int(input("How much gross written premium did you renew last month? "))

# Determine new business commission based on broker type
if broker_type =="commercial":
    new_business_commission = new_gwp * 0.20
else:
    new_business_commission = new_gwp * 0.16

# Determine renewal income from book of business. Commercial = 20% and Personal = 16%
if broker_type == "commercial":
    renewal_commission = old_gwp * 0.20
else: 
    renewal_commission = old_gwp * 0.16 

# Add new business commission + renewal commissions for total month compensation
total_commission = new_business_commission + renewal_commission
print(f"{user_name}, your total commission for the month is ${total_commission}")

