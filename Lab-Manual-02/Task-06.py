import numpy as np

# Generate an array of 100 random values
random_values = np.random.rand(100)

# Normalize the values between 1 and 100
normalized_values = 1 + (random_values - random_values.min()) * (99 / (random_values.max() - random_values.min()))

# Print values with serial numbers
for i, value in enumerate(normalized_values, start=1):
    print(f"{i}:{value: .1f}")
