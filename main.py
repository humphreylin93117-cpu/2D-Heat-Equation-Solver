import os
import numpy as np
import matplotlib.pyplot as plt
from solver import step


def gaussian_initial_condition(X, Y, x0, y0, sigma, amplitude=100.0):
    return amplitude * np.exp(-((X - x0) ** 2 + (Y - y0) ** 2) / (2 * sigma ** 2))


def plot_2d(u, save_path=None):
    plt.figure(figsize=(6, 5))
    plt.imshow(u, cmap="hot", interpolation="bilinear")
    plt.colorbar(label="Temperature")
    plt.title("2D Heat Distribution")
    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path, dpi=300)

    plt.show()


def plot_3d(X, Y, u, save_path=None):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")

    ax.plot_surface(X, Y, u, cmap="hot")
    ax.set_title("3D Heat Distribution")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("Temperature")

    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path, dpi=300)

    plt.show()


def main():
    os.makedirs("figures", exist_ok=True)

    nx, ny = 50, 50
    alpha = 1.0
    dx = 1.0
    dy = 1.0
    dt = 0.1
    nsteps = 100

    x = np.arange(nx)
    y = np.arange(ny)
    X, Y = np.meshgrid(x, y)

    x0 = nx // 2
    y0 = ny // 2
    sigma = 5.0

    u = gaussian_initial_condition(X, Y, x0, y0, sigma, amplitude=100.0)

    for _ in range(nsteps):
        u = step(u, alpha, dt, dx, dy)

    plot_2d(u, save_path="figures/gaussian_2d.png")
    plot_3d(X, Y, u, save_path="figures/heat_3d.png")


if __name__ == "__main__":
    main()