import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor

#fonction pour redessiner le cercle et les régions colorées
def draw_circle_and_regions(Px, Py):
    plt.clf()

    r = 6
    theta = np.linspace(0, 2*np.pi, 100)
    x1 = r * np.cos(theta)
    y1 = r * np.sin(theta)
    plt.plot(x1, y1, 'b')

    #ajout du centre du cercle O
    plt.plot(0, 0, 'bo')
    plt.annotate('O', (0, 0), textcoords="offset points", xytext=(0,10), ha='center')

    #ajout du point P
    plt.plot(Px, Py, 'go')
    plt.annotate('P', (Px, Py), textcoords="offset points", xytext=(0,10), ha='center')

    divisions = 8
    angles = np.linspace(0, 2*np.pi, divisions+1)

    for i in range(divisions):
        x_ai = r * np.cos(angles[i])
        y_ai = r * np.sin(angles[i])
        x_ai1 = r * np.cos(angles[i+1])
        y_ai1 = r * np.sin(angles[i+1])

        plt.plot([Px, x_ai], [Py, y_ai], 'k--')
        plt.plot([Px, x_ai1], [Py, y_ai1], 'k--')

        # Ajout des étiquettes A1, A2, ..., A8
        plt.annotate(f"A{i+1}", (x_ai, y_ai), textcoords="offset points", xytext=(0,10), ha='center')

        theta = np.linspace(angles[i], angles[i+1], 100)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        plt.fill(np.concatenate([[Px], x, [Px]]),
                 np.concatenate([[Py], y, [Py]]),
                 color='green' if i % 2 == 0 else 'red', alpha=0.4)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.draw()

#initialisation de la figure et du point P
fig, ax = plt.subplots()
Px, Py = 2, 3
draw_circle_and_regions(Px, Py)

#gestion de l'interaction
def on_click(event):
    global Px, Py
    Px, Py = event.xdata, event.ydata
    draw_circle_and_regions(Px, Py)

cursor = Cursor(ax, horizOn=False, vertOn=False)
fig.canvas.mpl_connect('button_press_event', on_click)

plt.show()
