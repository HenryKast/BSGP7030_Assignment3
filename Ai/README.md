# Assignment 3 — AI Linear Regression

This folder contains Python and R notebooks, standalone scripts, HTML exports, and a dedicated conda environment for linear regression analysis of `regression_data-1.csv`.

## Contents

| File | Description |
|------|-------------|
| `environment.yml` | Conda environment definition (`assignment3_ai`) |
| `regression_data-1.csv` | Sample dataset (YearsExperience, Salary) |
| `linear_regression_python.ipynb` | Python Jupyter notebook |
| `linear_regression_R.ipynb` | R Jupyter notebook |
| `linear_regression_python.html` | Exported HTML from the Python notebook |
| `linear_regression_R.html` | Exported HTML from the R notebook |
| `linear_regression_python.py` | Standalone Python script |
| `linear_regression_R.r` | Standalone R script |

## Environment Setup

This project uses the **`assignment3_ai`** conda environment (not `7030_class_2`).

From this folder:

```bash
conda env create -f environment.yml
conda activate assignment3_ai
```

The environment includes:

- Python 3.10, pandas, matplotlib, scikit-learn, scipy, jupyter, nbconvert
- R 4.5, ggplot2, IRkernel

## Notebooks

Both notebooks read the CSV, create a scatter plot, fit a linear model, overlay the regression line, and evaluate the model using:

- **MSE** (mean squared error)
- **r** (Pearson correlation)
- **slope**
- **intercept**
- **r_squared**

The final plot displays the slope formula and `r` in the **top-left corner**:

```
y = 8285.29x + 29203.52
r = 0.89
```

### Run in Jupyter

```bash
conda activate assignment3_ai
cd Ai
jupyter notebook
```

Open `linear_regression_python.ipynb` or `linear_regression_R.ipynb` and run all cells.

### Export HTML

```bash
conda activate assignment3_ai
jupyter nbconvert --to html linear_regression_python.ipynb
jupyter nbconvert --to html linear_regression_R.ipynb
```

## Standalone Scripts

Both scripts accept command-line arguments, print a metrics table in the terminal, and save an annotated regression plot.

### Usage

```text
python linear_regression_python.py <filename> <x_column> <y_column> [-o output.png] [--show]
Rscript linear_regression_R.r <filename> <x_column> <y_column> [--output output.png] [--show]
```

### Example

```bash
conda activate assignment3_ai
cd Ai

python linear_regression_python.py regression_data-1.csv YearsExperience Salary
Rscript linear_regression_R.r regression_data-1.csv YearsExperience Salary
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `filename` | Yes | Path to the CSV file |
| `x_column` | Yes | Predictor column name |
| `y_column` | Yes | Response column name |
| `-o` / `--output` | No | Save plot to a PNG file |
| `--show` | No | Display the plot on screen |

If neither `--output` nor `--show` is provided, the plot is saved by default to:

- `linear_regression_python_output.png`
- `linear_regression_R_output.png`

### Terminal Output

When run, each script prints a table like:

```text
+-----------+---------------+
| Metric    | Value         |
+-----------+---------------+
| MSE       | 17523844.0829 |
| r         | 0.8861        |
| slope     | 8285.2921     |
| intercept | 29203.5227    |
| r_squared | 0.7852        |
+-----------+---------------+
```

## Expected Results

Using the included dataset with `YearsExperience` as the predictor and `Salary` as the response:

| Metric | Value |
|--------|-------|
| MSE | ~17,523,844 |
| r | ~0.886 |
| slope | ~8,285 |
| intercept | ~29,204 |
| r_squared | ~0.785 |

## Troubleshooting

**Conda not found:** Use the full path to conda, for example:

```powershell
C:\Users\kasth\miniconda3\Scripts\conda.exe activate assignment3_ai
```

**Run scripts without activating the environment:**

```bash
conda run -n assignment3_ai python linear_regression_python.py regression_data-1.csv YearsExperience Salary
conda run -n assignment3_ai Rscript linear_regression_R.r regression_data-1.csv YearsExperience Salary
```

**CSV not found:** Run the scripts from the `Ai` folder, or pass the full path to the CSV file.

**R notebook kernel not found:** Register the IRkernel after activating the environment:

```bash
conda activate assignment3_ai
Rscript -e "IRkernel::installspec(name='ir', displayname='R (assignment3_ai)', user=TRUE)"
```
