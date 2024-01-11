import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42) 
x_data = np.random.rand(50) 
y_data = np.random.rand(50) 

plt.scatter(x_data, y_data, color='blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of Random Data')
plt.legend()
plt.show()
