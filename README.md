# Trend-Analysis-by-Release-Year
Analyze how Netflix content production has changed over time.

## Objective
Analyze how Netflix content production has changed over time by grouping titles by release year, comparing Movies and TV Shows, identifying high-volume years, and visualizing yearly trends.

## Files
- `Task4.py` — Python analysis script.
- `Dataset.csv` — input dataset provided for this project.
- `outputs/yearly_content_counts.csv` — total titles by release year.
- `outputs/yearly_content_by_type.csv` — yearly counts split by Movies and TV Shows.
- `outputs/year_over_year_changes.csv` — yearly absolute and percentage changes.
- `outputs/summary.csv` — summary metrics.
- `outputs/yearly_content_trend.png` — overall release-year line chart.
- `outputs/yearly_trend_by_type.png` — Movies vs TV Shows trend chart.

## Requirements
Python 3.9+ recommended.
Install dependencies:
```bash
pip install pandas matplotlib
```

## How to run in PyCharm
1. Extract the ZIP file or place `Task4.py` and `Dataset(2).csv` in the same project folder.
2. Open `Task4.py` in PyCharm.
3. Install `pandas` and `matplotlib` in the project's interpreter if needed.
4. Run the script.

Or use the terminal:
```bash
python Task4.py --input "Dataset(2).csv" --output-dir outputs
```

## Methodology
1. Load the CSV dataset.
2. Convert `release_year` to numeric values and ignore records with missing or invalid years for year-based calculations.
3. Count titles per release year.
4. Split yearly counts by content type (`Movie` and `TV Show`).
5. Calculate year-over-year absolute and percentage changes.
6. Save reports as CSV files and trend charts as PNG images.

## Interpretation notes
- This project analyzes the year a title was released, not necessarily the year Netflix added it to the platform.
- The latest year may have fewer titles because of incomplete coverage in the source dataset.
- Counts represent dataset records, not a verified count of all content ever produced by Netflix.
