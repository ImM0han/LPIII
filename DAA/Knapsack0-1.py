
def knapsack(capacity, weights, values, n):
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    weights.append(int(input("Enter weight: ")))
    values.append(int(input("Enter value: ")))

capacity = int(input("Enter knapsack capacity: "))

result = knapsack(capacity, weights, values, n)

print("Maximum value:", result)





# Enter number of items: 3
# Enter weight: 10
# Enter value: 60
# Enter weight: 20
# Enter value: 100
# Enter weight: 30
# Enter value: 120
# Enter knapsack capacity: 50

# Maximum value: 220




# Items:
# Item 1: Weight = 10, Value = 60
# Item 2: Weight = 20, Value = 100
# Item 3: Weight = 30, Value = 120

# Knapsack Capacity = 50

# Select Item 1 and Item 2:
# Total Weight = 10 + 20 = 30
# Total Value = 60 + 100 = 160

# Select Item 2 and Item 3:
# Total Weight = 20 + 30 = 50
# Total Value = 100 + 120 = 220

# Maximum Profit = 220