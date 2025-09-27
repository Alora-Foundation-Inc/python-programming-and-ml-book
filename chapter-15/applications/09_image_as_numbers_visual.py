import numpy as np
import matplotlib.pyplot as plt

# 8x8 "happy face" grayscale (0..1)
face = np.array([
 [0,0,0,0,0,0,0,0],
 [0,1,1,0,0,1,1,0],
 [0,1,1,0,0,1,1,0],
 [0,0,0,0,0,0,0,0],
 [0,0,0,1,1,0,0,0],
 [0,0,1,0,0,1,0,0],
 [0,1,0,0,0,0,1,0],
 [0,0,0,0,0,0,0,0],
], dtype=float)

plt.figure(figsize=(4,4))
plt.imshow(face, cmap="gray", vmin=0, vmax=1)
plt.title("An Image is a Grid of Numbers")
plt.axis("off")
plt.show()
