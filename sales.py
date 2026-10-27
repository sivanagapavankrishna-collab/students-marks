



# Multi-Branch Sales Matrix Comparison

sales = [
    [[10, 20, 15], [12, 18, 20]],
    [[25, 20, 15], [20, 25, 30]],
    [[15, 10, 20], [18, 15, 25]]
]

branches = ["Branch A", "Branch B", "Branch C"]
products = ["Laptop", "Mobile", "Tablet"]

# Product-wise total sales
print("Product Total Sales:")

for p in range(3):
    total = 0

    for b in range(3):
        for d in range(2):
            total += sales[b][d][p]

    print(products[p], ":", total)

# Branch-wise comparison
print("\nBranch Total Sales:")

for b in range(3):
    total = 0

    for d in range(2):
        total += sum(sales[b][d])

    print(branches[b], ":", total)

# Best performing product in each branch
print("\nBest Product in Each Branch:")

for b in range(3):
    totals = [0, 0, 0]

    for d in range(2):
        for p in range(3):
            totals[p] += sales[b][d][p]

    best = totals.index(max(totals))

    print(branches[b], ":", products[best])

# Best branch
branch_totals = [
    sum(sum(day) for day in branch)
    for branch in sales
]

best_branch = branch_totals.index(max(branch_totals))

print("\nBest Performing Branch:", branches[best_branch])
