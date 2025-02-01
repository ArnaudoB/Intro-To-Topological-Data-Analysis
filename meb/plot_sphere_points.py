import matplotlib.pyplot as plt
import numpy as np

def plot_sphere_points(S, c, r, output_file=None):
  
  d = len(S[0]) # dimension

  assert d == 2 or d == 3, "Points must be in 2D or 3D"

  S = np.array(S)

  fig = plt.figure(figsize=(6, 6))

  if d == 2 :
    ax = fig.add_subplot(111)
    plt.scatter(S[:, 0], S[:, 1], color='blue', label='Vertices')
    plt.scatter(c[0], c[1], color='red', label='Center')
    circle = plt.Circle(c, r, color='green', fill=False, linestyle='--', label='Circle')
    ax.add_artist(circle)

  if d == 3 :
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(S[:, 0], S[:, 1], S[:, 2], color='blue', label='Vertices')
    ax.scatter(c[0], c[1], c[2], color='red', label='Center')
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = r * np.outer(np.cos(u), np.sin(v)) + c[0]
    y = r * np.outer(np.sin(u), np.sin(v)) + c[1]
    z = r * np.outer(np.ones(np.size(u)), np.cos(v)) + c[2]
    ax.plot_surface(x, y, z, color='green', alpha=0.2, label='Sphere')

  buffer = r * 0.2  # Add a buffer around the circle for aesthetics
  ax.set_xlim(c[0] - r - buffer, c[0] + r + buffer)
  ax.set_ylim(c[1] - r - buffer, c[1] + r + buffer)
  if d == 3 :
    ax.set_zlim(c[2] - r - buffer, c[2] + r + buffer)

  # Add labels and legend
  if d ==2 :
    ax.set_title(f'Plot of the sphere of center ({c[0]:.2f}, {c[1]:.2f}) and radius {r:.3f}')
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  if d == 3 :
    ax.set_title(f'Plot of the sphere of center ({c[0]:.2f}, {c[1]:.2f}, {c[2]:.2f}) and radius {r:.3f}')
    ax.set_zlabel('Z')
  plt.legend(loc='upper right')
  plt.gca().set_aspect('equal', adjustable='box')
  plt.show()
  if output_file is not None:
    plt.savefig(output_file)