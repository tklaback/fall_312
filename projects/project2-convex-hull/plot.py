import matplotlib.pyplot as plt

# Sample data
x = [10, 100, 1000, 10_000, 100_000, 500_000, 1_000_000]
y = [0,	0.0014,	0.0112,	0.089, 0.7674, 3.8705, 7.887]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y, marker='o', linestyle='-')

# Set log scale for y-axis
ax.set_xscale("log")

# Set titles and labels
ax.set_title("Logarithmic Plot")
ax.set_xlabel("X values")
ax.set_ylabel("Y values (log scale)")

# Display the plot
plt.show()
