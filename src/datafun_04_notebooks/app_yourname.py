"""
app_yourname.py - P04 scaffold (student version).

Student instructions:
- This file is a scaffold for your notebook code.
- Work through the TODOs in order.
- Keep the structure parallel to the worked example.
- Run this as a script while you build it.
- Later, copy each "Code Cell" block into your notebook.

Assumptions:
- You have a CSV file at: data/raw/penguins.csv
- The CSV includes columns like:
  species, island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex, year

TODO:
- Replace YOUR NAME below.
- Confirm the CSV path and file name match your project.
"""


# --- Code Cell: Imports and configuration ---

from pathlib import Path

import pandas as pd

# --- Code Cell: Paths and constants ---

ROOT_DIR = Path.cwd()

# TODO: Confirm your file name and location.
RAW_PATH = ROOT_DIR / "data" / "raw" / "penguins.csv"

# TODO: Optional - adjust display settings (recommended for notebooks).
pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 120)

# TODO: Confirm these columns exist in your dataset.
NUMERIC_COLS = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
]

# TODO: Confirm the grouping column exists (used for comparisons).
GROUP_COL = "species"


# --- Code Cell: Load the data ---

# TODO: Read the CSV file into a DataFrame named df.
# Hint: Use pd.read_csv(...)
df = pd.DataFrame()  # replace this placeholder

# TODO: Print a message confirming the file was loaded and show df.shape (rows, columns).
print("Loaded data from:", RAW_PATH)
print("Rows, Columns:", df.shape)


# --- Code Cell: Initial inspection (head, columns, info) ---

# TODO: Show the first 5 rows.
print("\nFirst 5 rows:")
print(df.head())

# TODO: Show the column names.
print("\nColumn names:")
print(list(df.columns))

# TODO: Show DataFrame info (types and non-null counts).
print("\nInfo (types, non-null counts):")
print(df.info())


# --- Code Cell: Dataset size and structure (rows/cols) ---

# TODO: Store the number of rows and columns in variables and print them.
n_rows, n_cols = df.shape
print("\nDataset size:")
print("Number of records (rows):", n_rows)
print("Number of columns:", n_cols)


# --- Code Cell: Data dictionary starter (column + dtype + missing count) ---

# TODO: Create a starter data dictionary as a DataFrame with:
# - column name
# - dtype
# - missing_count
# - missing_pct
#
# Hint: df.columns, df.dtypes, df.isna().sum(), df.isna().mean()
data_dictionary = pd.DataFrame()  # replace this placeholder

print("\nData dictionary (starter):")
print(data_dictionary)


# --- Code Cell: Data quality checks (missing, duplicates, basic sanity) ---

# TODO: Print missing values per column, sorted descending.
print("\nMissing values per column:")
# print(...)

# TODO: Count duplicate rows and print the count.
dup_count = 0  # replace this placeholder
print("\nDuplicate rows:", dup_count)

# TODO: Print describe() for the numeric columns.
print("\nBasic sanity check for numeric columns:")
print(df[NUMERIC_COLS].describe())


# --- Code Cell: Optional cleaning step (drop rows missing key numeric fields) ---

# TODO: Create df_clean by dropping rows with missing values
# in the numeric columns and the group column.
# Hint: df.dropna(subset=...)
df_clean = pd.DataFrame()  # replace this placeholder

print("\nAfter dropping rows missing key numeric fields:")
print("Rows, Columns:", df_clean.shape)


# --- Code Cell: Descriptive statistics overall ---

# TODO: Create overall statistics for numeric columns.
# Hint: df_clean[NUMERIC_COLS].describe().T
stats_overall = pd.DataFrame()  # replace this placeholder

print("\nOverall descriptive statistics (numeric columns):")
print(stats_overall)


# --- Code Cell: Descriptive statistics by group (species) ---

# TODO: Create grouped statistics by GROUP_COL for numeric columns.
# Suggested aggregation: count, mean, std, min, max
# Hint: df_clean.groupby(GROUP_COL)[NUMERIC_COLS].agg([...])
stats_by_group = pd.DataFrame()  # replace this placeholder

print("\nDescriptive statistics by group:")
print(stats_by_group)


# --- Code Cell: Simple correlations (numeric only) ---

# TODO: Create and print a correlation matrix.
# Hint: df_clean[NUMERIC_COLS].corr(numeric_only=True)
corr = pd.DataFrame()  # replace this placeholder

print("\nCorrelation matrix (numeric columns):")
print(corr)


# --- Code Cell: Exploratory visualizations (simple plots) ---

# TODO: Create at least TWO scatter plots using df_clean.plot(kind="scatter", ...)
# Choose two pairs of numeric columns that help answer:
# "Do measurements help distinguish species?"
#
# TODO: Create ONE boxplot by species for one numeric column.
# Hint: df_clean.boxplot(column="flipper_length_mm", by=GROUP_COL, grid=False)

# Example ideas (choose your own):
# - flipper_length_mm vs bill_length_mm
# - bill_depth_mm vs bill_length_mm
# - body_mass_g vs flipper_length_mm


# --- Code Cell: Save outputs (optional but professional) ---

# TODO: Create data/results/ if needed.
RESULTS_DIR = ROOT_DIR / "data" / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# TODO: Save your data dictionary starter to CSV.
data_dictionary_path = RESULTS_DIR / "penguins_data_dictionary_starter.csv"
# data_dictionary.to_csv(data_dictionary_path, index=False)

# TODO: Save overall stats, grouped stats, and correlations.
stats_overall_path = RESULTS_DIR / "penguins_stats_overall.csv"
stats_by_group_path = RESULTS_DIR / "penguins_stats_by_group.csv"
corr_path = RESULTS_DIR / "penguins_corr.csv"

# stats_overall.to_csv(stats_overall_path)
# stats_by_group.to_csv(stats_by_group_path)
# corr.to_csv(corr_path)

print("\nWrote results to (if you enabled saving):")
print("-", data_dictionary_path)
print("-", stats_overall_path)
print("-", stats_by_group_path)
print("-", corr_path)


# --- Code Cell: Notes to include in Markdown cells ---

# TODO: In your notebook Markdown, answer:
# - What does one row represent?
# - How many rows and columns are there?
# - What columns are most important for your question?
# - What missing data did you find? What did you decide to do?
# - What did the plots show?
# - What would you do next?

print("\nNotebook Markdown checklist:")
print("- One-row meaning (unit of analysis)")
print("- Rows/columns and structure notes")
print("- Data quality notes (missing/duplicates)")
print("- Which measurements differ by species?")
print("- Plot-based observations")
print("- Next steps (optional)")
