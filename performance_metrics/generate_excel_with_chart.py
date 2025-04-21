# generate_excel_from_csv.py

import sys
import pandas as pd

def generate_excel(csv_input, excel_output):
    # Load CSV
    df = pd.read_csv(csv_input, names=[
        "file", "source", "execution_time_ms",
        "memory_usage_mb_seconds", "average_memory_usage_mb", "max_memory_usage_mb"
    ])

    # Pivot so each .py file has all source metrics in one row
    pivot_df = df.pivot(index='file', columns='source')
    # Flatten MultiIndex columns
    pivot_df.columns = [f"{source.lower()}_{metric}" for metric, source in pivot_df.columns]
    pivot_df.reset_index(inplace=True)

    # Round values for better readability
    pivot_df = pivot_df.round(3)

    # Save to Excel
    pivot_df.to_excel(excel_output, index=False)
    print(f"Excel saved to {excel_output}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_excel_from_csv.py <input_csv> <output_excel>")
        sys.exit(1)

    generate_excel(sys.argv[1], sys.argv[2])
