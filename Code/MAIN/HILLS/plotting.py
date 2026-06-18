from pathlib import Path

import matplotlib.pyplot as plt



FIGURES_DIR= Path("figures")

FIGURES_DIR.mkdir(exist_ok=True)


def save_figure(filename, dpi = 300, show= True):
    output = FIGURES_DIR/filename
    plt.tight_layout()
    plt.savefig(output,dpi=dpi)

    print(f"Saveed: {output}")

    if show:
        plt.show()
    plt.close()