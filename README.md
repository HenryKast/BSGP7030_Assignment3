# Linear Regression Project

This project fits a simple linear regression model to predict **Salary** from **YearsExperience** using the shared dataset `regression_data-1.csv`. The work is organized into two folders under `notebooks_scripting`:

- `Manual/` — reference notebooks, scripts, and environment setup files
- `Ai/` — AI-generated notebooks and standalone command-line scripts

Both folders use the same dataset and perform the same analysis:

1. Read the CSV file
2. Create a scatter plot
3. Fit a linear model
4. Overlay the regression line
5. Evaluate the model
6. Display the R² value on the plot

---

## Manual Folder

Path: `C:\Users\kasth\notebooks_scripting\Manual`

### Files

| File | Purpose |
|------|---------|
| `regression_data-1.csv` | Input dataset (`YearsExperience`, `Salary`) |
| `linear_regression_python.ipynb` | Python Jupyter notebook |
| `linear_regression_python.html` | Exported HTML version of the Python notebook |
| `linear_regression_R.ipynb` | R Jupyter notebook |
| `linear_regression_R.html` | Exported HTML version of the R notebook |
| `linear_regression_python.py` | Standalone Python script |
| `linear_regression_R.r` | Standalone R script |
| `environment-1.yml` | Conda environment definition (`7030_class_2`) |
| `requirements-1.txt` | Pip package list (alternative to conda) |
| `setup_env-1.sh` | Bash script to create the conda environment and launch JupyterLab |

### Environment setup

The Manual folder includes everything needed to recreate the course environment.

**Conda setup (recommended):**

```bash
cd notebooks_scripting/Manual
conda env create -f environment-1.yml
conda activate 7030_class_2
```

The `7030_class_2` environment includes Python 3.10, JupyterLab, pandas, matplotlib, scikit-learn, R, IRkernel, and ggplot2.

**Pip setup (alternative):**

```bash
pip install -r requirements-1.txt
```

**Full OSC/Linux setup script:**

`setup_env-1.sh` automates environment creation, registers Python and R Jupyter kernels, and starts JupyterLab on port 2000. This script is intended for the OSC cluster environment and uses `module load miniconda3`.

**Register kernels after activating the environment:**

```bash
python -m ipykernel install --user --name 7030_class_2 --display-name "Python (7030_class_2)"
Rscript -e "IRkernel::installspec(name='ir_7030_class_2', displayname='R (7030_class_2)')"
```

### How the Manual notebooks work

#### Python notebook (`linear_regression_python.ipynb`)

1. Reads `regression_data-1.csv` with pandas
2. Plots a red scatter plot of experience vs. salary
3. Fits `LinearRegression` from scikit-learn
4. Overlays the fitted line in blue
5. Prints the R² score with `model.score()`
6. Annotates the plot with `R² = 0.785`

Kernel: `7030_class_2`

#### R notebook (`linear_regression_R.ipynb`)

1. Reads `regression_data-1.csv` with `read.csv()`
2. Plots a red base-R scatter plot
3. Fits `lm(Salary ~ YearsExperience, data = dataset)`
4. Uses ggplot2 to overlay points and the regression line
5. Prints `summary(model)` with coefficients and R²
6. Annotates the plot with the R² value

Kernel: `ir_7030_class_2`

### Running the Manual notebooks

```powershell
cd C:\Users\kasth\notebooks_scripting\Manual
conda activate 7030_class_2
jupyter lab
```

Open the `.ipynb` files in JupyterLab, or open the `.html` files directly in a browser to view the exported results without running code.

**Export a notebook to HTML:**

```powershell
jupyter nbconvert --to html linear_regression_python.ipynb
jupyter nbconvert --to html linear_regression_R.ipynb
```

### How the Manual Python script works

`linear_regression_python.py` is a standalone version of the Python notebook. It accepts exactly three positional arguments:

```text
python linear_regression_python.py <filename> <x_column> <y_column>
```

**What it does:**

1. Reads the CSV file
2. Fits a scikit-learn linear regression model
3. Creates a scatter plot with a blue regression line
4. Annotates the plot with R²
5. Saves the plot to `linear_regression_python_output.png`
6. Displays the plot on screen with `plt.show()`

**Example:**

```powershell
cd C:\Users\kasth\notebooks_scripting\Manual
python linear_regression_python.py regression_data-1.csv YearsExperience Salary
```

### How the Manual R script works

`linear_regression_R.r` is a standalone version of the R notebook. It accepts exactly three positional arguments:

```text
Rscript linear_regression_R.r <filename> <x_column> <y_column>
```

**What it does:**

1. Reads the CSV file
2. Fits a linear model with `lm()`
3. Builds a ggplot2 plot with red points and a blue regression line (`geom_smooth(method = "lm")`)
4. Annotates the plot with R²
5. Saves the plot to `linear_regression_r_output.png`
6. Prints the plot to the screen

**Example:**

```powershell
cd C:\Users\kasth\notebooks_scripting\Manual
conda run -n 7030_class_2 Rscript linear_regression_R.r regression_data-1.csv YearsExperience Salary
```

### Manual folder expected output

Both Manual scripts produce **R² ≈ 0.785**, indicating that years of experience explains about 78.5% of the variation in salary for this dataset.

---

## Ai Folder

Path: `C:\Users\kasth\notebooks_scripting\Ai`

### Files

| File | Purpose |
|------|---------|
| `regression_data-1.csv` | Input dataset (`YearsExperience`, `Salary`) |
| `linear_regression_python.ipynb` | Python Jupyter notebook |
| `linear_regression_python.html` | Exported HTML version of the Python notebook |
| `linear_regression_R.ipynb` | R Jupyter notebook |
| `linear_regression_R.html` | Exported HTML version of the R notebook |
| `linear_regression_python.py` | Standalone Python script with command-line options |
| `linear_regression_R.r` | Standalone R script with command-line options |
| `README.md` | This documentation file |

### How the Ai notebooks work

The Ai notebooks follow the same analysis workflow as the Manual notebooks, with one structural difference in the R² plotting step: the final R² annotation is placed in its own section rather than combined with the overlay step.

#### Python notebook (`linear_regression_python.ipynb`)

1. Reads `regression_data-1.csv`
2. Creates a red scatter plot
3. Fits `LinearRegression`
4. Overlays the regression line with axis labels and title
5. Evaluates the model with `model.score()` (R²)
6. Replots with the R² annotation in the upper-left corner

Kernel: `7030_class_2`

#### R notebook (`linear_regression_R.ipynb`)

1. Reads `regression_data-1.csv`
2. Creates a red base-R scatter plot
3. Fits `lm(Salary ~ YearsExperience)`
4. Uses ggplot2 to overlay points and predicted values
5. Prints `summary(model)`
6. Creates a final ggplot with the R² annotation

Kernel: `ir_7030_class_2`

### Running the Ai notebooks

```powershell
cd C:\Users\kasth\notebooks_scripting\Ai
conda activate 7030_class_2
jupyter lab
```

Open the `.ipynb` files in JupyterLab, or open the `.html` files in a browser.

**Execute and export to HTML:**

```powershell
cd C:\Users\kasth\notebooks_scripting\Ai

jupyter nbconvert --execute --to html linear_regression_python.ipynb --ExecutePreprocessor.kernel_name=7030_class_2

conda run -n 7030_class_2 jupyter nbconvert --execute --to html linear_regression_R.ipynb --ExecutePreprocessor.kernel_name=ir_7030_class_2
```

### How the Ai Python script works

`linear_regression_python.py` converts the Python notebook into a command-line tool using `argparse`.

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `filename` | Yes | Path to the CSV file |
| `x_column` | Yes | Predictor column name |
| `y_column` | Yes | Response column name |
| `-o`, `--output` | No | Save the plot to a PNG file |
| `--show` | No | Display the plot on screen |

**Behavior:**

1. Resolves the CSV path from the current directory or the script directory
2. Fits a scikit-learn linear regression model
3. Prints `R-squared: 0.7852` to the terminal
4. Builds a scatter plot with a blue regression line and R² annotation
5. If `--output` is provided, saves the PNG to that path
6. If neither `--output` nor `--show` is provided, saves to `linear_regression_python_output.png` in the Ai folder
7. If `--show` is provided, opens the plot window

**Examples:**

```powershell
cd C:\Users\kasth\notebooks_scripting\Ai

# Save plot to PNG (default output file if -o is omitted and --show is not used)
python linear_regression_python.py regression_data-1.csv YearsExperience Salary

# Save plot to a specific file
python linear_regression_python.py regression_data-1.csv YearsExperience Salary -o linear_regression_python_output.png

# Display plot on screen
python linear_regression_python.py regression_data-1.csv YearsExperience Salary --show
```

### How the Ai R script works

`linear_regression_R.r` converts the R notebook into a command-line tool.

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `filename` | Yes | Path to the CSV file |
| `x_column` | Yes | Predictor column name |
| `y_column` | Yes | Response column name |
| `--output` | No | Save the plot to a PNG file |
| `--show` | No | Display the plot on screen |

**Behavior:**

1. Resolves the CSV path from the current directory or the script directory
2. Fits `lm(y ~ x)` and prints the full model summary
3. Builds a ggplot2 plot with red points, a blue regression line, and an R² label
4. If `--output` is provided, saves the PNG to that path
5. If neither `--output` nor `--show` is provided, saves to `linear_regression_R_output.png` in the Ai folder
6. If `--show` is provided, prints the plot to the graphics device

**Examples:**

```powershell
cd C:\Users\kasth\notebooks_scripting\Ai

# Save plot to PNG (default output file if flags are omitted)
conda run -n 7030_class_2 Rscript linear_regression_R.r regression_data-1.csv YearsExperience Salary

# Save plot to a specific file
conda run -n 7030_class_2 Rscript linear_regression_R.r regression_data-1.csv YearsExperience Salary --output linear_regression_R_output.png

# Display plot on screen
conda run -n 7030_class_2 Rscript linear_regression_R.r regression_data-1.csv YearsExperience Salary --show
```

### Running from the parent folder

The scripts live in the `Ai` subfolder. If you run commands from `notebooks_scripting` instead of `Ai`, include the `Ai\` prefix:

```powershell
cd C:\Users\kasth\notebooks_scripting

python Ai\linear_regression_python.py regression_data-1.csv YearsExperience Salary --show

conda run -n 7030_class_2 Rscript Ai\linear_regression_R.r regression_data-1.csv YearsExperience Salary --show
```

The Ai scripts automatically look for `regression_data-1.csv` in the current directory and in the `Ai` folder, so the dataset is found even when you run from the parent directory.

### Ai folder expected output

Both Ai scripts produce the same model results as the Manual versions:

- **R² ≈ 0.785**
- **Intercept ≈ 29,204**
- **YearsExperience coefficient ≈ 8,285**

### Differences between Manual and Ai scripts

| Feature | Manual scripts | Ai scripts |
|---------|----------------|------------|
| Argument parsing | Positional only (`sys.argv` / `commandArgs`) | Positional plus optional flags |
| Save vs. display | Always saves and shows | Choose `--output`, `--show`, or default save |
| CSV path handling | Must exist in current directory | Searches current directory and script directory |
| R regression line | `geom_smooth(method = "lm")` | `geom_line()` with `predict()` |
| Python R² display | Annotated, then saved and shown | Printed to terminal and annotated on plot |

### Requirements

- **Python:** pandas, matplotlib, scikit-learn
- **R:** ggplot2
- **Environment:** `7030_class_2` conda environment (or equivalent packages installed)
- **Jupyter kernels:** `7030_class_2` (Python), `ir_7030_class_2` (R)
