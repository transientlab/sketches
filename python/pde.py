import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters
nx = 11
ny = 11
nz = 11
dx = 0.1
dy = 0.1
dz = 0.1
nt = 100
sigma = 0.2
dt = sigma * dx * dy * dz

# Initial conditions
u = np.zeros((nx, ny, nz))
u[int(nx / 2), int(ny / 2), int(nz / 2)] = 1

# Numerical solution using finite difference method
for n in range(nt + 1):
    un = u.copy()
    u[1:-1, 1:-1, 1:-1] = un[1:-1, 1:-1, 1:-1] + sigma * (un[2:, 1:-1, 1:-1] - 2 * un[1:-1, 1:-1, 1:-1] + un[:-2, 1:-1, 1:-1] + 
                                                           un[1:-1, 2:, 1:-1] - 2 * un[1:-1, 1:-1, 1:-1] + un[1:-1, :-2, 1:-1] +
                                                           un[1:-1, 1:-1, 2:] - 2 * un[1:-1, 1:-1, 1:-1] + un[1:-1, 1:-1, :-2])

# Plot the results
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
x, y, z = np.meshgrid(np.linspace(0, 1, nx), np.linspace(0, 1, ny), np.linspace(0, 1, nz))
ax.scatter(x, y, z, c=u, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()