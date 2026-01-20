"""app_case.py - Project script (example).

Author: Denise Case
Date: 2026-01

Purpose:
- Perform exploratory data analysis (EDA) on the penguins dataset
- Practice key Python skills in a notebook environment

This file is written as a runnable script.

Assumptions:
- You have a CSV file at: data/raw/penguins.csv
- The CSV contains columns like:
  species, island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex, year


OBS:
  Don't edit this file - it should remain a working example.
"""


# === DECLARE IMPORTS ===

from pathlib import Path

import pandas as pd

# === CONFIGURE LOGGER ONCE PER MODULE (FILE) ===

LOG: logging.Logger = get_logger("P04", level="DEBUG")


# === DECLARE GLOBAL CONSTANTS ===

ROOT_DIR = Path.cwd()
RAW_PATH = ROOT_DIR / "data" / "raw" / "penguins.csv"

NUMERIC_COLS = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
]

GROUP_COL = "species"

# === SET CONFIGURATION ===

# Set pandas display options (optional but helpful in notebooks)
pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 120)


# --- Code Cell: Load the data ---

# Read CSV into a DataFrame
df = pd.read_csv(RAW_PATH)

print("Loaded data from:", RAW_PATH)
print("Rows, Columns:", df.shape)


# --- Code Cell: Initial inspection (head, columns, info) ---

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(list(df.columns))

print("\nInfo (types, non-null counts):")
print(df.info())


# --- Code Cell: Dataset size and structure (rows/cols) ---

n_rows, n_cols = df.shape
print("\nDataset size:")
print("Number of records (rows):", n_rows)
print("Number of columns:", n_cols)


# --- Code Cell: Data dictionary starter (column + dtype + missing count) ---

# This is a compact "starter dictionary" students can expand later.
data_dictionary = pd.DataFrame(
    {
        "column": df.columns,
        "dtype": [str(t) for t in df.dtypes],
        "missing_count": df.isna().sum().values,
        "missing_pct": (df.isna().mean() * 100).round(2).values,
    }
)

print("\nData dictionary (starter):")
print(data_dictionary)


# --- Code Cell: Data quality checks (missing, duplicates, basic sanity) ---

print("\nMissing values per column:")
print(df.isna().sum().sort_values(ascending=False))

dup_count = int(df.duplicated().sum())
print("\nDuplicate rows:", dup_count)

print("\nBasic sanity check for numeric columns:")
print(df[NUMERIC_COLS].describe())


# --- Code Cell: Optional cleaning step (drop rows missing key numeric fields) ---

# For EDA, it's common to create a "cleaned view" used for numeric analysis.
# We keep the original df and create df_clean.
df_clean = df.dropna(subset=NUMERIC_COLS + [GROUP_COL])

print("\nAfter dropping rows missing key numeric fields:")
print("Rows, Columns:", df_clean.shape)


# --- Code Cell: Descriptive statistics overall ---

stats_overall = df_clean[NUMERIC_COLS].describe().T
print("\nOverall descriptive statistics (numeric columns):")
print(stats_overall)


# --- Code Cell: Descriptive statistics by group (species) ---

# Grouped summary helps answer the guiding question:
# "Do measurements differ by species?"
stats_by_species = df_clean.groupby(GROUP_COL)[NUMERIC_COLS].agg(
    ["count", "mean", "std", "min", "max"]
)
print("\nDescriptive statistics by species:")
print(stats_by_species)


# --- Code Cell: Simple correlations (numeric only) ---

corr = df_clean[NUMERIC_COLS].corr(numeric_only=True)
print("\nCorrelation matrix (numeric columns):")
print(corr)


# --- Code Cell: Exploratory visualizations (keep simple, notebook-friendly) ---

# In a notebook, these will display inline.
# In a script, they will open plot windows depending on your environment.

ax1 = df_clean.plot(
    kind="scatter",
    x="flipper_length_mm",
    y="bill_length_mm",
    title="Flipper length vs Bill length",
)
ax1.set_xlabel("Flipper length (mm)")
ax1.set_ylabel("Bill length (mm)")

ax2 = df_clean.plot(
    kind="scatter",
    x="bill_depth_mm",
    y="bill_length_mm",
    title="Bill depth vs Bill length",
)
ax2.set_xlabel("Bill depth (mm)")
ax2.set_ylabel("Bill length (mm)")

# Boxplots by species help visualize separability.
ax3 = df_clean.boxplot(
    column="flipper_length_mm",
    by=GROUP_COL,
    grid=False,
)
ax3.set_title("Flipper length by species")
ax3.set_xlabel("Species")
ax3.set_ylabel("Flipper length (mm)")

# Remove pandas' automatic extra title line (useful in notebooks)
# In some environments, boxplot adds a second title line; this is safe to ignore.


# --- Code Cell: Save outputs (optional but professional) ---

RESULTS_DIR = ROOT_DIR / "data" / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

data_dictionary_path = RESULTS_DIR / "penguins_data_dictionary_starter.csv"
data_dictionary.to_csv(data_dictionary_path, index=False)

stats_overall_path = RESULTS_DIR / "penguins_stats_overall.csv"
stats_overall.to_csv(stats_overall_path)

stats_by_species_path = RESULTS_DIR / "penguins_stats_by_species.csv"
stats_by_species.to_csv(stats_by_species_path)

corr_path = RESULTS_DIR / "penguins_corr.csv"
corr.to_csv(corr_path)

print("\nWrote results to:")
print("-", data_dictionary_path)
print("-", stats_overall_path)
print("-", stats_by_species_path)
print("-", corr_path)


# --- Code Cell: Notes to self (what to write in Markdown cells) ---

print("\nNotes to include in Markdown cells:")
print("- What does one row represent?")
print("- Rows/columns and what surprised you about the structure.")
print("- Any missing data patterns and your choice (drop vs keep).")
print("- Which measurements seem most useful for separating species?")
print("- What plots suggest about separability and overlap.")
print(
    "- Next steps (optional): feature selection, simple rules, or a basic classifier later."
)
