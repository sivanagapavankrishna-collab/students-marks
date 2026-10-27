
# Hospital Ward Occupancy Monitoring

wards = ["General", "ICU", "Emergency"]

capacity = [50, 20, 30]

# Bed occupancy for 3 wards across 3 days
occupancy = [
    [30, 40, 55],
    [15, 18, 22],
    [20, 25, 28]
]

max_occupancy = 0
peak_ward = ""
peak_day = 0

for i in range(len(wards)):
    print("\nWard:", wards[i])

    for j in range(len(occupancy[i])):
        beds = occupancy[i][j]

        utilization = (beds / capacity[i]) * 100

        print("Day", j + 1, "Occupancy:", beds)
        print("Utilization:", round(utilization, 2), "%")

        if beds > capacity[i]:
            print("Capacity Violation!")

        if beds > max_occupancy:
            max_occupancy = beds
            peak_ward = wards[i]
            peak_day = j + 1

print("\n----- Final Report -----")
print("Peak Demand Ward:", peak_ward)
print("Peak Demand Day:", peak_day)
print("Maximum Occupancy:", max_occupancy)
