# 2D Heat Equation Solver

A Python-based project for solving the two-dimensional heat equation using the explicit finite difference method.  
This project includes numerical simulation, 2D and 3D visualization, comparison with an exact solution, and convergence analysis.

---

## 1. Mathematical Model

The equation considered in this project is:
$$
\[
u_t = \alpha (u_{xx} + u_{yy})
\]
$$
where:

- \(u(x,y,t)\) is the temperature distribution
- \(\alpha\) is the thermal diffusivity

This equation describes the diffusion of heat in a two-dimensional domain.

---

## 2. Numerical Method

The solver uses the **explicit finite difference method**.

For interior grid points, the update formula is:

\[
u_{i,j}^{n+1}
=
u_{i,j}^n
+
\alpha \Delta t
\left(
\frac{u_{i+1,j}^n - 2u_{i,j}^n + u_{i-1,j}^n}{\Delta x^2}
+
\frac{u_{i,j+1}^n - 2u_{i,j}^n + u_{i,j-1}^n}{\Delta y^2}
\right)
\]

This method is simple and efficient, but it requires a stability condition on the time step.

---

## 3. Features

- Explicit finite difference solver for the 2D heat equation
- Gaussian initial condition simulation
- 2D heatmap visualization
- 3D surface plot visualization
- Comparison between numerical and exact solutions
- Error field visualization
- Mesh refinement and convergence study

---

## 4. Project Structure

```text
heat-equation-solver/
│
├─ main.py
├─ solver.py
├─ error_analysis.py
├─ README.md
│
├─ figures/
│  ├─ gaussian_2d.png
│  ├─ heat_3d.png
│  └─ convergence_plot.png
│
└─ results/
   └─ convergence_table.txt
