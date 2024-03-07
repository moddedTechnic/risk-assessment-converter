import shutil
from pathlib import Path

import pandas as pd
import typst

__dir__ = Path.cwd()

BUILD_DIR = __dir__ / "build"
DATA_DIR = BUILD_DIR / "data"
TEMPLATES_DIR = __dir__ / "templates"


def prepare_row(row):
    row["risk.attendees"] = row["risk.attendees"] == "Y" or row["risk.attendees"] == "y"
    row["risk.volunteers"] = (
        row["risk.volunteers"] == "Y" or row["risk.volunteers"] == "y"
    )
    row["risk.staff"] = row["risk.staff"] == "Y" or row["risk.staff"] == "y"
    row["risk.all"] = (
        row["risk.attendees"] and row["risk.volunteers"] and row["risk.staff"]
    )
    return row


def main():
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(exist_ok=True, parents=True)
    DATA_DIR.mkdir(exist_ok=True, parents=True)

    full_ra_file = __dir__ / "ra.xlsx"
    with full_ra_file.open("rb") as f:
        df = pd.read_excel(f, index_col=0)
    risks = df.fillna("").apply(prepare_row, axis=1)
    uni_risks = risks[
        [
            "hazard",
            "risk.attendees",
            "risk.volunteers",
            "risk.staff",
            "risk.all",
            "remove",
            "reduce",
            "control",
        ]
    ]

    uni_risks.to_json(DATA_DIR / "uni.risks.json", orient="records")

    typst.compile(
        TEMPLATES_DIR / "ra.uni.typst",
        output=BUILD_DIR / "ra.uni.pdf",
        root=__dir__,
    )


if __name__ == "__main__":
    exit(main())
