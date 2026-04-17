import pandas as pd
import os
from datetime import datetime

# ------------------------------------------------------------
# WGU D598 - Task 2 (Coding)
# Author: (Bernesha Liburd)
# Purpose:
#   1) Import dataset into a DataFrame
#   2) Identify duplicate rows
#   3) Group IDs by state + descriptive stats (mean, median, min, max)
#   4) Filter negative debt-to-equity ratios
#   5) Create debt-to-income ratio DataFrame (Long-term Debt / Revenue)
#   6) Concatenate ratio to original DataFrame
#   7) Export outputs to an Excel workbook
# ------------------------------------------------------------


def safe_output_filename(base_name: str) -> str:
    """
    If base_name is locked/open (PermissionError), this function returns
    a timestamped filename to avoid overwriting the locked file.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    name, ext = os.path.splitext(base_name)
    return f"{name}_{timestamp}{ext}"


def main():
    # -------------------------
    # SETTINGS
    # -------------------------
    input_file = "D598 Data Set.xlsx"          # dataset file name [1](blob:https://www.microsoft365.com/c7a8ef7a-370f-4911-bb95-505d8c390170)
    output_file = "D598_Task2_Output.xlsx"     # desired output file name

    # -------------------------
    # 1) Import the data file into a DataFrame
    # -------------------------
    if not os.path.exists(input_file):
        raise FileNotFoundError(
            f"ERROR: Cannot find '{input_file}'.\n"
            f"Make sure BOTH files are in the same folder:\n"
            f"  - task2_analysis.py\n"
            f"  - {input_file}\n\n"
            f"Current working directory:\n  {os.getcwd()}"
        )

    df = pd.read_excel(input_file, engine="openpyxl")

    print("✅ Data loaded successfully.")
    print("Current working directory:", os.getcwd())
    print("Rows/Columns:", df.shape)
