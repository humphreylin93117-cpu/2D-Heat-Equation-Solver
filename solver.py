import numpy as np

def step(u, alpha, dt, dx, dy):
    un = u.copy()

    u[1:-1, 1:-1] = un[1:-1, 1:-1] + alpha * dt * (
        (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[:-2, 1:-1]) / dx**2
        + (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, :-2]) / dy**2
    )

    return u