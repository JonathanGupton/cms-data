"""Create the cleaned 2023 MS-DRG file"""

import pandas as pd
import tomli

from validation import validate_drg_dataframe


VERSION = "2023"

with open(r"../../datasets.toml", "rb") as f:
    CONF = tomli.load(f)

HEADER = CONF["MS-LTC-DRG"]["HEADER"]
FILE_NAME = CONF["MS-LTC-DRG"][VERSION]["FILE"]
DIRECTORY = CONF["MS-LTC-DRG"]["DIRECTORY"]


def main():
    df = pd.read_csv(
        rf"../../raw/{DIRECTORY}/{FILE_NAME}",
        skiprows=1,
        encoding="windows-1252",
        skipfooter=5,
        sep="\t",
        engine="python",
    )
    df.drop("FY 2021 LTCH Cases1", axis=1, inplace=True)
    df["MS-LTC-DRG"] = df["MS-LTC-DRG"].astype(int)
    df["MS-LTC-DRG Title"] = df["MS-LTC-DRG Title"].str.replace(r"*", "", regex=False)
    df["MS-LTC-DRG Title"] = df["MS-LTC-DRG Title"].str.replace(r"+", "", regex=False)
    df.columns = HEADER
    validate_drg_dataframe(df)
    df.to_csv(rf"../../data/{DIRECTORY}/{VERSION}.csv", index=False)


if __name__ == "__main__":
    main()
