
def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0

    for weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += value * (capacity / weight)
            capacity = 0
            break

    return total_value


n = int(input("Enter number of items: "))

items = []

for i in range(n):
    weight = float(input("Enter weight of item: "))
    value = float(input("Enter value of item: "))
    items.append((weight, value))

capacity = float(input("Enter knapsack capacity: "))

result = fractional_knapsack(capacity, items)

print("\nMaximum value:", result)




# Enter number of items: 3
# Enter weight of item: 10
# Enter value of item: 60
# Enter weight of item: 20
# Enter value of item: 100
# Enter weight of item: 30
# Enter value of item: 120
# Enter knapsack capacity: 50

# Maximum value: 240.0



# Example:
# Items = [(10, 60), (20, 100), (30, 120)]
# Knapsack Capacity = 50
#
# Value/Weight Ratio:
# Item 1 = 60/10 = 6
# Item 2 = 100/20 = 5
# Item 3 = 120/30 = 4
#
# Step 1: Take Item 1 completely.
# Profit = 60, Remaining Capacity = 40
#
# Step 2: Take Item 2 completely.
# Profit = 100, Remaining Capacity = 20
#
# Step 3: Take 20/30 fraction of Item 3.
# Profit = 120 * (20/30) = 80
#
# Maximum Profit = 60 + 100 + 80 = 240
#
# Final Answer = 240