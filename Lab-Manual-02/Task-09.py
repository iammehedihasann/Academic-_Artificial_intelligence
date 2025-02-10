import matplotlib.pyplot as plt

# Data: Days of the week and corresponding temperatures (in °C)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperatures = [22, 24, 19, 23, 25, 27, 26]

# Create a line plot
plt.figure(figsize=(8, 5))
plt.plot(days, temperatures, marker="o",linestyle="-", color="g", label="Temperature (°C)")

# Add labels and title
plt.title("Temperature Variations Over a Week")
plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")


# Show legend and grid
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

# Display the plot
plt.show()
