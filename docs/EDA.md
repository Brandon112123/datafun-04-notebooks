## Exploratory Data Analysis

Objective: Implement Jupyter Notebook to perform exploratory data analysis
 (EDA) using pandas and other tools.
We will use the Seaborn library to load the Iris dataset.
Review the dataset here: iris.csv or see the local copy provided iris.csv.

## Step 1. Initial Title, Header, and Imports
Start by getting organized and providing the focus for your notebook.
1. Create a single Markdown title.
2. Create a Markdown header with author name, purpose, and date at the top.
3. Create a numbered section for Imports (using a Markdown cell).
4. Create a Python cell for all the import statements needed for this notebook, for example (yours may vary):

Jupyter Notebook Python cell example:

```python
import pandas as pd
import seaborn as sns
import matplotlib

# Axes object (basic plot type returned by Seaborn)
from matplotlib.axes import Axes
```

## Step 2. Load Data
Then, we acquire the data and load the data
into a suitable structure for analysis,
typically a pandas DataFrame when working with Python.
Everything we learned about data earlier can be helpful in this step.
You should be able to read csv, txt, JSON and more.

Some Python tools have datasets built in.
We'll use these so we can focus on the new skills in this module.
For example, in this project, we use the Iris dataset available in the Seaborn library.

The Iris dataset is a well-known dataset in data science and machine learning,
often used for various classification tasks and basic data exploration.

Load the data into a pandas DataFrame which is used to handle 2-dimensional spreadsheet data.  
We'll use sns.load_dataset() function and pass in the 'iris' (the name without .csv) to populate our DataFrame.

Jupyter Notebook Python cell example:

```python
# Load the Iris dataset into pandas DataFrame
iris_df: pd.DataFrame = sns.load_dataset('iris')

# List column names
iris_df.columns

# Inspect first few rows of the DataFrame
iris_df.head()

```


## Step 3. Initial Data Inspection
Once the data is loaded, the first task is to get a sense of what we're working with.

We can check the first few rows of the dataset using the DataFrame head() method to understand the structure of the data.
We can pass in an argument with the specific number of rows to view.
We can check the shape of the DataFrame with shape to see the number of rows and columns (an attribute - note there are no parentheses). 
We can see the data types of each column with dtypes (an attribute - note there are no parentheses). 
We can see a bit more by calling the info() method. 
This step is crucial for getting familiar with the dataset's format, size,
and the type of information each column holds.

Jupyter Notebook Python cell example:

```python
# Specify the number of rows to display
iris_df.head(10)

# Inspect the shape of the DataFrame with shape attribute
# The shape is a tuple with count of rows and columns in the DataFrame
iris_df.shape

# Inspect the data types of the columns with dtypes attribute
# The data types are returned as a pandas Series
iris_df.dtypes

# Inspect the data types of the columns with info() method
iris_df.info()
```

## Step 4. Initial Descriptive Statistics
The next step is to look at summary statistics.

Use the DataFrame describe() method to obtain a statistical summary of the numerical columns.
This includes count, mean, standard deviation, minimum, and maximum values, as well as the quartiles.
This provides insights into the distribution and central tendencies of the data, which can be crucial for identifying patterns, anomalies, or data integrity issues.

Jupyter Notebook Python cell example:

```python
# Inspect summary statistics for numerical columns
iris_df.describe()
```

## Step 5. Initial Data Distribution for Numerical Columns
We can show a histogram for a single numerical column by providing the EXACT column name.
To show histograms for ALL numerical columns, we can use hist().

Jupyter Notebook Python cell example:

```python
# Inspect histogram by one numerical column
iris_df['sepal_length'].hist()

# Inspect histograms for ALL numerical columns
iris_df.hist()

# Show all plots
matplotlib.pyplot.show()
```
Afterwards, use a Markdown cell to document your observations.

## Step 5. Initial Data Distribution for Categorical Columns
Choose a categorical column and use iris_df['column_name'].value_counts() to display the count of each category.
Use a loop to show the value counts for all categorical columns.

Jupyter Notebook Python cell example:

```python
# Inspect value counts by categorical column
# Column name must be EXACT.
# The value_counts() method is only available for Series objects.
# The value_counts() method returns a pandas Series with the counts of unique values in the column.
iris_df['species'].value_counts()

# Inspect value counts for ALL categorical columns
for col in iris_df.select_dtypes(include=['object', 'category']).columns:
    # Display count plot
    sns.countplot(x=col, data=iris_df)
    matplotlib.pyplot.title(f'Distribution of {col}')
    matplotlib.pyplot.show()

# Show all plots
matplotlib.pyplot.show()
```

Afterwards, use a Markdown cell to document your observations.

## Step 6. Initial Data Transformation and Feature Engineering
 Data rarely comes in the format needed for optimal analysis.
 This phase of data preparation or preprocessing is a multifaceted process that
 involves both cleaning and transforming the data for analysis. 

The distinction can be subtle, but in general:

***Data Cleaning*** is about ensuring the quality and consistency of the data. This includes:
- Handling missing values to prevent gaps in analysis.
- Removing duplicate entries to avoid skewed results.
- Correcting errors to maintain data accuracy.
- Potentially standardizing formats, such as ensuring dates are consistently formatted or categorical data is uniformly labeled.

**Data Transformation** focuses on preparing the data for analysis. This involves:
- Normalization or standardization of numerical data to bring different scales to a common scale.
- Encoding categorical variables, such as through one-hot encoding, to make them suitable for analysis.
- Renaming columns for clarity and consistency across the dataset.
- Feature engineering, which involves creating new features from existing data.

Use pandas and other tools to perform cleaning and transformations as needed.  
This step refines raw data into a form where additional analytical techniques
can be applied more effectively.

Jupyter Notebook Python cell example:

```python
# Feature Engineering
# Renaming a column
iris_df.rename(columns={'sepal_length': 'Sepal Length'}, inplace=True)

# Adding a new column
iris_df['Sepal Area'] = iris_df['Sepal Length'] * iris_df['sepal_width']

```

## Step 7. Initial Visualizations
With the data in the right shape, using the features and columns in the desired format,
the next step is to begin visualization.
This involves using appropriate chart types to extract and present insights from the data.

Libraries like seaborn and matplotlib offer a wide range of visualization options.
For instance, pair plots from seaborn can be very useful for understanding relationships between all variables in a dataset.
Create a variety of chart types using seaborn and matplotlib to showcase different aspects of the data.

Jupyter Notebook Python cell example:

```python
# Feature Engineering
# Renaming a column
iris_df.rename(columns={'sepal_length': 'Sepal Length'}, inplace=True)

# Adding a new column
iris_df['Sepal Area'] = iris_df['Sepal Length'] * iris_df['sepal_width']

# Create a pairplot of the Iris dataset
# A pairplot is a grid of scatter plots for each pair of numerical columns in the dataset
# The hue parameter is used to color the data points
# by species (a categorical column)
sns.pairplot(iris_df, hue='species')

# Show all plots
matplotlib.pyplot.show()
```
Important: After each visualization, use Markdown cells to document your observations and insights.

Add a scatter plot - good for showing two numerical variables with a categorical attribute as the color of the dot at each xy point.

Jupyter Notebook Python cell example:

```python
# A scatter plot is a plot of two numerical variables.
scatter_plt: Axes = sns.scatterplot(
    data=iris_df, x="Sepal Length", y="Sepal Area", hue="species"
)

# Set axis labels using the Matplotlib Axes methods set_xlabel() and set_ylabel()
scatter_plt.set_xlabel("Sepal Length (mm)")
scatter_plt.set_ylabel("Sepal Area (mm squared)")  

# Set the title using the Matplotlib Axes set_title() method
scatter_plt.set_title("Chart 1. Iris Sepal Length vs. Sepal Area (by Species)")

matplotlib.pyplot.show()
```

## Step 8. Initial Insights
Use your chart headings and annotations to provide your insights.
At the end add a section that summarizes your initial insights based on the facts discovered during your initial exploratory data analysis.

## Step 9. Annotate Your Notebook for Storytelling and Presentation
The final step of the EDA process is interpreting the visualizations and
statistics to craft a compelling narrative around your findings.
This involves combining your technical analysis with storytelling techniques to
make your findings clear and engaging for your audience.
The goal is to provide actionable insights and convey the significance of your
findings in a way that resonates with stakeholders, regardless of their
technical background.

Use your own custom opening to introduce yourself and the focus of your notebook.
Use Markdown section headings to introduce each step.
Interpret the visualizations and statistics to narrate a clear and compelling data story.
Present your findings in a logical and engaging manner.
Present your notebook with an opening that introduces yourself and your topic.
Use Markdown section headings to introduce each step.
Interpret the visualizations and statistics to narrate a clear and compelling data story.
Present your findings in a logical and engaging manner.

## Checklist

- [ ] Notebook has exactly one Markdown title (with a single hash).
- [ ] Notebook has useful Markdown header cell with author and purpose, and optionally, the date.
- [ ] Notebook uses numbered second level Markdown headings for organization.
- [ ] Notebook has numbered sections with useful content for:
  - [ ] 1. Imports
  - [ ] 2. Load Data
  - [ ] 3. Initial Data Inspection
  - [ ] 4. Initial Descriptive Statistics
  - [ ] 5. Initial Data Distribution for Numerical Columns
  - [ ] 6. Initial Data Transformation and Feature Engineering
  - [ ] 7. Initial Visualizations
  - [ ] 8. Initial Insights
- [ ] Notebook includes commentary as we go that tells a unique data story.
- [ ] Notebook includes unique insights into the dataset.
- [ ] Code and visuals are working, notebook is fully executed and on display in GitHub.
