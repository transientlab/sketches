import math
from sagemath import 

x, y = ('x y')
W = plot3d(1 + x^2 + 2*y^2, (x, 0, 2), (y, 0, 1), frame=True, color='purple', opacity=0.8)
show(W, figsize=8)

