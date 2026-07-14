Prompts used to build the AI section of the assignment:

1. I would like to create two notebooks with the following goals, 
A Jupyter Notebook using the Python kernel
A Jupyter Notebook using the R kernel
The dataset: regression_data-1.csv
Exported HTML versions of both notebooks (.html)

I would like this all done in the notebooks_scripting directory using the ai folder. I have uploaded the dataset for you already
Each Notebook must
Read the CSV file, Create a scatter plot, Fit a linear model, Overlay the regression line, Evaluate the model, plot the R sqaured value, and Be saved as both .ipynb and .html. Do not modify anything in the manual folder

2. In the same ai folder using the notebooks you created, I would like to 
Convert each Jupyter Notebook (Python and R) into a standalone script and run it from the command line. You scripts should be able to:

Modify the script to accept command-line arguments

Run the script from the terminal and generate the regression plot

Save the plot as an image file (.png) or as output to the screen

3. The files are all there however when running the code, these two errors are given: PS C:\Users\kasth\notebooks_scripting> python linear_regression_python.py regression_data-1.csv YearsExperience Salary --show
C:\Users\kasth\miniconda3\envs\7030_class_2\python.exe: can't open file 'C:\\Users\\kasth\\notebooks_scripting\\linear_regression_python.py': [Errno 2] No such file or directory
PS C:\Users\kasth\notebooks_scripting> conda run -n 7030_class_2 Rscript linear_regression_R.r regression_data-1.csv YearsExperience Salary --show
ERROR conda.cli.main_run:execute(148): `conda run Rscript linear_regression_R.r regression_data-1.csv YearsExperience Salary --show` failed. (See above for error)
PS C:\Users\kasth\notebooks_scripting>

4. In the readme include all relevant information to how the code works and running the code in the AI folder. Additionally create an additional section in the readme for how the code in the manual folder works and runs. Place the manual section first in the readme. Do not edit any files in the manual folder or create a new readme file, only modify the existing file.