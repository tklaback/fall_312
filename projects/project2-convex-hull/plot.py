import numpy as np
import matplotlib.pyplot as plt

x = [10, 100, 1000, 10_000, 100_000, 1_000_000]
y = [.00023, .00291, .01959, .16187, 1.69392, 16.18877]

x_array = np.array(x)
y_array = np.array(y)

plt.figure(figsize=(8, 6))
plt.plot(x_array, y_array, 'o-', label='My Data Points')
plt.title('A Simple Plot of y = sin(x)')
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend(loc='best')
plt.grid(True)
plt.show()