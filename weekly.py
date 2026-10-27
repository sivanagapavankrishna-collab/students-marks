
# Weekly Electricity Consumption Matrix

appliances = ["Fan", "AC", "TV"]
limits = [50, 100, 30]

# Electricity readings for 7 days (kWh)
consumption = [
    [5, 6, 7, 8, 6, 7, 8],
    [15, 18, 20, 17, 16, 19, 20],
    [3, 4, 3, 5, 4, 3, 4]
]

# Appliance-wise total
print("Appliance Total Consumption:")

for i in range(3):
    total = sum(consumption[i])
    print(appliances[i], ":", total, "kWh")

    if total > limits[i]:
        print("Warning: Consumption Exceeded!")

# Daily total
print("\nDaily Total Consumption:")

for j in range(7):
    daily = 0

    for i in range(3):
        daily += consumption[i][j]

    print("Day", j + 1, ":", daily, "kWh")

# Weekly total
weekly = sum(sum(row) for row in consumption)

print("\nWeekly Consumption:", weekly, "kWh")
