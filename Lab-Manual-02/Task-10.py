import matplotlib.pyplot as plt

# Sample data: Regions and corresponding sales revenue (in $1000)
regions = ["North", "South", "East", "West", "Central"]
sales_revenue = [50, 65, 40, 70, 55]

plt.figure(figsize=(8, 5))
plt.bar(regions, sales_revenue, color="orange", alpha=0.8)


plt.xlabel("Regions")
plt.ylabel("Sales Revenue (in $1000)")
plt.title("Sales Revenue Comparison Across Different Regions")

for i, value in enumerate(sales_revenue):
    plt.text(i, value + 1, f"{value}", ha="center", fontsize=10, fontweight="bold")

plt.grid(axis="y", linestyle="--", alpha=0.6)

plt.show()
