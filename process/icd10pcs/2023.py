"""Create the cleaned 2023 ICD-10-PCS data set"""

import pandas as pd
import tomli

from validation import validate_icd10pcs_dataframe


VERSION = "2023"

with open(r"../../datasets.toml", "rb") as f:
    CONF = tomli.load(f)

HEADER = CONF["ICD-10-PCS"]["HEADER"]
FILE_NAME = CONF["ICD-10-PCS"][VERSION]["FILE"]
DIRECTORY = CONF["ICD-10-PCS"]["DIRECTORY"]


def main():
    df = pd.read_fwf(
        rf"../../raw/{DIRECTORY}/{FILE_NAME}",
        encoding="windows-1252",
        colspecs=[(0, 7), (7, 500)]
    )
    df.columns = HEADER
    validate_icd10pcs_dataframe(df)
    df.to_csv(rf"../../data/{DIRECTORY}/{VERSION}.csv", index=False)


if __name__ == "__main__":
    main()
