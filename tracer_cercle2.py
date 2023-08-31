import matplotlib.pyplot as plt
import numpy as np

# Créer un cercle
theta = np.linspace(0, 2*np.pi, 100)
r = 6
x1 = r * np.cos(theta)
y1 = r * np.sin(theta)
plt.plot(x1, y1, 'b')

# Point P à l'intérieur du cercle
Px, Py = (2, 3)
plt.plot(Px, Py, 'go')

# Diviser le cercle en 8 arcs de cercle
divisions = 8
angles = np.linspace(0, 2*np.pi, divisions+1)

# Pour chaque division, dessiner le triangle et colorier le secteur
for i in range(divisions):
    # Coordonnées de Ai et Ai+1
    x_ai = r * np.cos(angles[i])
    y_ai = r * np.sin(angles[i])
    x_ai1 = r * np.cos(angles[i+1])
    y_ai1 = r * np.sin(angles[i+1])
    
    plt.plot([Px, x_ai], [Py, y_ai], 'k--')
    plt.plot([Px, x_ai1], [Py, y_ai1], 'k--')
    
    # Colorier le secteur
    theta = np.linspace(angles[i], angles[i+1], 100)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.fill(np.concatenate([[Px], x, [Px]]),
             np.concatenate([[Py], y, [Py]]),
             color='green' if i % 2 == 0 else 'red', alpha=0.4)

plt.gca().set_aspect('equal', adjustable='box')
plt.show()
