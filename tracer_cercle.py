import matplotlib.pyplot as plt
import numpy as np

# Créer le cercle
theta = np.linspace(0, 2*np.pi, 100)
r = 6
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.plot(x, y, color="black")

# Points A1, A2, ..., A8
angleStep = np.pi/4  # 45 degrés en radians
points_A = [(r * np.cos(i*angleStep), r * np.sin(i*angleStep)) for i in range(8)]

# Point P
P = (-3, 2)

# Dessiner les segments de P aux points A
for Ax, Ay in points_A:
    plt.plot([P[0], Ax], [P[1], Ay], color="black")

# Configuration du graphique
plt.axis("equal")
plt.grid(True)
plt.show()
