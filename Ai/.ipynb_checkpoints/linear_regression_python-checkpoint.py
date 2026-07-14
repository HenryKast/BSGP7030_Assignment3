"""Standalone linear regression script converted from linear_regression_python.ipynb."""
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


def parse_args():
    parser = argparse.ArgumentParser(
        description="Fit a linear regression model and plot the results."
    )
    parser.add_argument("filename", help="Path to the input CSV file")
    parser.add_argument("x_column", help="Name of the predictor column")
    parser.add_argument("y_column", help="Name of the response column")
    parser.add_argument(
        "-o",
        "--output",
        help="Save the plot to this PNG file path",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Display the plot on screen",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    dataset = pd.read_csv(args.filename)
    model = LinearRegression()
    model.fit(dataset[[args.x_column]], dataset[[args.y_column]])

    r_squared = model.score(dataset[[args.x_column]], dataset[[args.y_column]])

    plt.scatter(dataset[args.x_column], dataset[args.y_column], color="red")
    plt.plot(
        dataset[args.x_column],
        model.predict(dataset[[args.x_column]]),
        color="blue",
    )
    plt.annotate(
        f"R² = {r_squared:.3f}",
        xy=(0.05, 0.95),
        xycoords="axes fraction",
        fontsize=12,
    )
    plt.title(f"{args.y_column} vs {args.x_column}")
    plt.xlabel(args.x_column)
    plt.ylabel(args.y_column)

    print(f"R-squared: {r_squared:.4f}")

    output_path = Path(args.output) if args.output else None
    if output_path is None and not args.show:
        output_path = Path("linear_regression_python_output.png")

    if output_path is not None:
        plt.savefig(output_path, bbox_inches="tight")
        print(f"Plot saved to {output_path.resolve()}")

    if args.show:
        plt.show()
    else:
        plt.close()


if __name__ == "__main__":
    main()
