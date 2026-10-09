
import os
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# TASK 4: TREND ANALYSIS BY RELEASE YEAR
# ==========================================

# Get the folder where this Python file is saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Dataset and output folder paths
INPUT_FILE = os.path.join(BASE_DIR, "Dataset.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Load the dataset
df = pd.read_csv(INPUT_FILE)

print("=" * 50)
print("NETFLIX TREND ANALYSIS BY RELEASE YEAR")
print("=" * 50)

print("\nDataset shape:", df.shape)
print("\nFirst five records:")
print(df.head())

# 2. Clean release year data
df["release_year"] = pd.to_numeric(
    df["release_year"], errors="coerce"
)

df = df.dropna(subset=["release_year"]).copy()
df["release_year"] = df["release_year"].astype(int)

# 3. Calculate yearly content releases
yearly_counts = (
    df.groupby("release_year")
    .size()
    .sort_index()
)

yearly_counts_df = yearly_counts.reset_index()
yearly_counts_df.columns = ["Release_Year", "Title_Count"]

yearly_counts_df.to_csv(
    os.path.join(OUTPUT_DIR, "yearly_content_counts.csv"),
    index=False
)

print("\nYearly Content Counts:")
print(yearly_counts_df.tail(10).to_string(index=False))

# 4. Identify the year with the highest number of titles
peak_year = yearly_counts.idxmax()
peak_count = yearly_counts.max()

print("\nPeak Release Year:", peak_year)
print("Number of Titles:", peak_count)

# 5. Create overall yearly trend chart
plt.figure(figsize=(12, 6))

plt.plot(
    yearly_counts.index,
    yearly_counts.values,
    marker="o"
)

plt.title("Netflix Content Trend by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "yearly_content_trend.png"),
    dpi=200
)

plt.show()
plt.close()

# 6. Analyze Movies and TV Shows separately
yearly_type = (
    df.groupby(["release_year", "type"])
    .size()
    .unstack(fill_value=0)
    .sort_index()
)

yearly_type.to_csv(
    os.path.join(OUTPUT_DIR, "yearly_content_by_type.csv")
)

print("\nYearly Content by Type:")
print(yearly_type.tail(10))

# 7. Plot Movies vs TV Shows
plt.figure(figsize=(12, 6))

for content_type in yearly_type.columns:
    plt.plot(
        yearly_type.index,
        yearly_type[content_type],
        marker="o",
        label=content_type
    )

plt.title("Netflix Movies vs TV Shows by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "yearly_trend_by_type.png"),
    dpi=200
)

plt.show()
plt.close()

# 8. Calculate year-over-year changes
changes = yearly_counts.to_frame(name="Title_Count")

changes["Yearly_Change"] = changes["Title_Count"].diff()

changes["Percentage_Change"] = (
    changes["Title_Count"].pct_change() * 100
).round(2)

changes = changes.reset_index()

changes.to_csv(
    os.path.join(OUTPUT_DIR, "year_over_year_changes.csv"),
    index=False
)

# 9. Generate summary report
summary = pd.DataFrame({
    "Metric": [
        "Total Dataset Records",
        "Records with Valid Release Year",
        "Earliest Release Year",
        "Latest Release Year",
        "Peak Release Year",
        "Titles in Peak Year",
        "Total Movies",
        "Total TV Shows"
    ],
    "Value": [
        len(pd.read_csv(INPUT_FILE)),
        len(df),
        int(yearly_counts.index.min()),
        int(yearly_counts.index.max()),
        int(peak_year),
        int(peak_count),
        int((df["type"] == "Movie").sum()),
        int((df["type"] == "TV Show").sum())
    ]
})

summary.to_csv(
    os.path.join(OUTPUT_DIR, "summary.csv"),
    index=False
)

print("\nProject Summary:")
print(summary.to_string(index=False))

print("\nAnalysis completed successfully!")
print("All charts and reports are saved in the outputs folder.")
