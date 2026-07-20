"""Standalone linear regression script converted from linear_regression_python.ipynb."""
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def resolve_path(path_str: str) -> Path:
    """Resolve a user path from the current directory or the script directory."""
    path = Path(path_str)
    if path.exists():
        return path.resolve()

    script_dir = Path(__file__).resolve().parent
    script_relative = script_dir / path_str
    if script_relative.exists():
        return script_relative.resolve()

    raise FileNotFoundError(
        f"Could not find '{path_str}' in the current directory or '{script_dir}'."
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description="Fit a linear regression model, print metrics, and plot the results."
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


def print_metrics_table(metrics: dict) -> None:
    """Display regression metrics as a terminal table."""
    headers = ["Metric", "Value"]
    rows = [
        ("MSE", f"{metrics['mse']:.4f}"),
        ("r", f"{metrics['r']:.4f}"),
        ("slope", f"{metrics['slope']:.4f}"),
        ("intercept", f"{metrics['intercept']:.4f}"),
        ("r_squared", f"{metrics['r_squared']:.4f}"),
    ]
    col0 = max(len(headers[0]), max(len(r[0]) for r in rows))
    col1 = max(len(headers[1]), max(len(r[1]) for r in rows))
    border = f"+-{'-' * col0}-+-{'-' * col1}-+"
    print(border)
    print(f"| {headers[0]:<{col0}} | {headers[1]:<{col1}} |")
    print(border)
    for name, value in rows:
        print(f"| {name:<{col0}} | {value:<{col1}} |")
    print(border)


def main():
    args = parse_args()

    data_path = resolve_path(args.filename)
    dataset = pd.read_csv(data_path)
    x = dataset[args.x_column]
    y = dataset[args.y_column]

    model = LinearRegression()
    model.fit(dataset[[args.x_column]], dataset[[args.y_column]])
    y_pred = model.predict(dataset[[args.x_column]]).ravel()

    slope, intercept, r_value, _, _ = linregress(x, y)
    mse = mean_squared_error(y, y_pred)
    r_squared = model.score(dataset[[args.x_column]], dataset[[args.y_column]])

    metrics = {
        "mse": mse,
        "r": r_value,
        "slope": slope,
        "intercept": intercept,
        "r_squared": r_squared,
    }
    print_metrics_table(metrics)

    plt.scatter(x, y, color="red")
    plt.plot(x, y_pred, color="blue", label="Fitted line")
    plt.text(
        0.05,
        0.95,
        f"y = {slope:.2f}x + {intercept:.2f}\nr = {r_value:.2f}",
        transform=plt.gca().transAxes,
        fontsize=12,
        verticalalignment="top",
    )
    plt.title(f"{args.y_column} vs {args.x_column}")
    plt.xlabel(args.x_column)
    plt.ylabel(args.y_column)
    plt.legend()

    output_path = Path(args.output) if args.output else None
    if output_path is None and not args.show:
        output_path = Path(__file__).resolve().parent / "linear_regression_python_output.png"

    if output_path is not None:
        plt.savefig(output_path, bbox_inches="tight")
        print(f"Plot saved to {output_path.resolve()}")

    if args.show:
        plt.show()
    else:
        plt.close()


if __name__ == "__main__":
    main()
