import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = [100, 1000, 10_000, 100_000, 1_000_000]
bin_heap_y = [0.002, 0.0326, 0.4544, 6.4368, 88.954]
array_y = [0.002, 0.171, 16.9722, 1922.6, 169722.00]

# Create a figure and axis
fig, ax = plt.subplots()


# # Plot the data
ax.plot(x, array_y, marker='o', linestyle='-')
# ax.plot(x, bin_heap_y, marker='X', linestyle='--')

# Set log scale for y-axis
# ax.set_xscale("log")
# ax.set_yscale("log")

# Set titles and labels
ax.set_title("Array implementation")
ax.set_xlabel("n (log scale)")
ax.set_ylabel("t")

# Display the plot
plt.show()

