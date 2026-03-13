import os
import numpy as np
import matplotlib.pyplot as plt


def compute_orders(hs, errors):
    orders = []
    for i in range(len(hs) - 1):
        p = np.log(errors[i] / errors[i + 1]) / np.log(hs[i] / hs[i + 1])
        orders.append(p)
    return orders


def print_convergence_table(grid_sizes, hs, max_errors, l2_errors, max_orders, l2_orders):
    print("Grid       dx          Max error       Max order      L2 error        L2 order")
    print("-" * 78)

    for i in range(len(grid_sizes)):
        grid = f"{grid_sizes[i]}x{grid_sizes[i]}"
        dx = hs[i]
        emax = max_errors[i]
        el2 = l2_errors[i]

        if i == 0:
            print(f"{grid:<10} {dx:<11.6f} {emax:<15.8e} {'-':<14} {el2:<15.8e} {'-'}")
        else:
            print(
                f"{grid:<10} {dx:<11.6f} {emax:<15.8e} "
                f"{max_orders[i-1]:<14.6f} {el2:<15.8e} {l2_orders[i-1]:.6f}"
            )


def save_convergence_table(filepath, grid_sizes, hs, max_errors, l2_errors, max_orders, l2_orders):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("Grid       dx          Max error       Max order      L2 error        L2 order\n")
        f.write("-" * 78 + "\n")

        for i in range(len(grid_sizes)):
            grid = f"{grid_sizes[i]}x{grid_sizes[i]}"
            dx = hs[i]
            emax = max_errors[i]
            el2 = l2_errors[i]

            if i == 0:
                f.write(f"{grid:<10} {dx:<11.6f} {emax:<15.8e} {'-':<14} {el2:<15.8e} {'-'}\n")
            else:
                f.write(
                    f"{grid:<10} {dx:<11.6f} {emax:<15.8e} "
                    f"{max_orders[i-1]:<14.6f} {el2:<15.8e} {l2_orders[i-1]:.6f}\n"
                )


def plot_convergence(hs, max_errors, l2_errors, save_path=None):
    ref = max_errors[0] * (hs / hs[0]) ** 2

    plt.figure(figsize=(8, 6))
    plt.loglog(hs, max_errors, 'o-', label='Max error')
    plt.loglog(hs, l2_errors, 's-', label='L2 error')
    plt.loglog(hs, ref, '--', label=r'Reference slope $h^2$')

    plt.xlabel('h')
    plt.ylabel('Error')
    plt.title('Log-Log Error Convergence')
    plt.legend()
    plt.grid(True, which='both', ls='--')
    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path, dpi=300)

    plt.show()


def main():
    hs = np.array([0.041667, 0.020408, 0.010101])
    max_errors = np.array([3.40896751e-04, 7.77409595e-05, 1.90382308e-05])
    l2_errors = np.array([1.70448376e-04, 3.89104526e-05, 9.52151225e-06])
    grid_sizes = [25, 50, 100]

    max_orders = compute_orders(hs, max_errors)
    l2_orders = compute_orders(hs, l2_errors)

    os.makedirs("figures", exist_ok=True)
    os.makedirs("results", exist_ok=True)

    print_convergence_table(grid_sizes, hs, max_errors, l2_errors, max_orders, l2_orders)
    save_convergence_table(
        "results/convergence_table.txt",
        grid_sizes, hs, max_errors, l2_errors, max_orders, l2_orders
    )
    plot_convergence(hs, max_errors, l2_errors, save_path="figures/convergence_plot.png")


if __name__ == "__main__":
    main()