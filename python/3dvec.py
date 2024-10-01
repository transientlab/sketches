import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

import numpy as np



# vectors = [[0, 0, 0, 1, 1, 1],
#                [0, 0, 0, -1, -1, 1],
#                [0, 0, 0, -1, 1, 1],
#                [0, 0, 0, 1, -1, 1],
#                [0, 0, 0, 1, -1, -1],
#                [0, 0, 0, 1, 1, -1],
#                [0, 0, 0, -1, 1, -1],
#                [0, 0, 0, -1, -1, -1]
#                ]

# grid = 8
# # for x in range(grid):
# #     v = [-grid/2+x, 0, 3, 0, 0, 1]
# #     vectors.append(v)

# soa = np.array(vectors)

# # X, Y, Z, U, V, W = zip(*soa)
# fig = plt.figure()
# fig, ax = plt.subplots()
# ax = fig.add_subplot(111, projection='3d')
# # ax.quiver(X, Y, Z, U, V, W)
# ax.set_xlim([-10, 10])
# ax.set_ylim([-10, 10])
# ax.set_zlim([-10, 10])

# def update():
#     v = [-, 0, 3, 0, 0, 1]
#     vectors.append(v)
#     soa = np.array(vectors)
#     X, Y, Z, U, V, W = zip(*soa)
#     ax.quiver(X, Y, Z, U, V, W)
#     return (vectors)

# ani = animation.FuncAnimation(fig=fig, func=update, frames=60, interval=30)
# plt.show()





# fig, ax = plt.subplots()
# t = np.linspace(0, 3, 40)
# g = -9.81
# v0 = 14
# z = g * t**2 / 2 + v0 * t

# v02 = 13
# z2 = g * t**2 / 2 + v02 * t

# scat = ax(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
# line2 = ax.plot(t[0], z2[0], label=f'v0 = {v02} m/s')[0]
# ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
# ax.legend()


# def update(frame):
#     # for each frame, update the data stored on each artist.
#     x = t[:frame]
#     y = z[:frame]
#     # update the scatter plot:
#     data = np.stack([x, y]).T
#     scat.set_offsets(data)
#     # update the line plot:
#     line2.set_xdata(t[:frame])
#     line2.set_ydata(z2[:frame])
#     return (scat, line2)




# ani = animation.FuncAnimation(fig=fig, func=update, frames=60, interval=30)
# plt.show()


# klasa ciało
# położenie
# promień
# prędkość
# przyspieszenie





G = 0.00001

mA = 10
xA0, yA0, zA0  = -1, 1, 1
vxA0, vyA0, vzA0 = 0.1, 0, 0

mB = 100
xB0, yB0, zB0  = 1, 0, -1
vxB0, vyB0, vzB0 = -0.1, 0, 0


a = [mA, xA0, yA0, zA0, vxA0, vyA0, vzA0]
b = [mB, xB0, yB0, zB0, vxB0, vyB0, vzB0]

fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))

def calc_vectors(t):

    global a
    global b
    print(a)
    mA = a[0]
    mB = b[0]
    xa = a[1]
    ya = a[2]
    za = a[3]
    xb =  b[1]
    yb =  b[2]
    zb =  b[3] + b[6]*t
    ua = -G*mA*mB/pow((xb-xa), 2)
    va = -G*mA*mB/pow((yb-ya), 2)
    wa = -G*mA*mB/pow((zb-za), 2)
    ub = -G*mA*mB/pow((xa-xb), 2)
    vb = -G*mA*mB/pow((ya-yb), 2)
    wb = -G*mA*mB/pow((za-zb), 2)
    a = [mA, xa, ya, za, a[4]+ua, a[5]+va, a[6]+wa]
    b = [mB, xb, yb, zb, b[4]+ub, b[5]+vb, b[6]+wb]


    vectors =[[xa,ya,za,100,0,0],[xb,yb,zb,100,0,0]]
    r = np.linalg.norm(vectors[0])
    print(r)
    soa = np.array(vectors)
    X, Y, Z, U, V, W = zip(*soa)
    return X, Y, Z, U, V, W

quiver = ax.quiver(*calc_vectors(0))

ax.set_xlim(-1000, 1000)
ax.set_ylim(-1000, 1000)
ax.set_zlim(-1000, 1000)

def update(t):
    global quiver
    quiver.remove()
    quiver = ax.quiver(*calc_vectors(t))

ani = FuncAnimation(fig, update, frames=np.linspace(0,10,100), interval=1)
plt.show()