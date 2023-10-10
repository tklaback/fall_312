import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = [10, 100, 1000, 10_000, 100_000, 500_000, 1_000_000]
y = [0,	0.0014,	0.0112,	0.089, 0.7674, 3.8705, 7.887]

# Create a figure and axis
fig, ax = plt.subplots()

nlogn = [xi * np.log(xi) for xi in x]

# scaled_nlogn = [yi / max(nlogn) * max(y) for yi in nlogn]

ax.plot(x, nlogn, marker='x', linestyle='--', label='Scaled nlogn')

# c = sum(y) / sum(nlogn)

# print(c)

# # Plot the data
# ax.plot(x, y, marker='o', linestyle='-')

# Set log scale for y-axis
ax.set_xscale("log")

# Set titles and labels
ax.set_title("nlogn")
ax.set_xlabel("n (log scale)")
ax.set_ylabel("t")

# Display the plot
plt.show()
