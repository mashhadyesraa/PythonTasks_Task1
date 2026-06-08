item1 = float(input(str("Enter your first Item: ")))
item2 = float(input(str("Enter your Second Item: ")))
item3 = float(input(str("Enter your Third Item: ")))

budget = float(input(str("Enter your Budget: ")))

total_cost = item1 + item2 + item3

print("Total Cost:", total_cost,"\n")

if total_cost <= budget:
    remaining = budget - total_cost
    print("You can buy what you need and the remaining is: " ,remaining,"\n")
else:
    needed = total_cost - budget
    print("your costs exceeds your budget, you need:", needed,"\n")
