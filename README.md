# Risk Assessments

```toml
# conf.toml

title = "event title"
department = "reviewing department"

id = "a number"
assessor = "your name here"
authoriser = "probably a member of staff"
review = false # or a "string" of when to review next
```

```sh
pip install poetry
poetry install
poetry shell
python3 generate.py
```

Converts `ra.xlsx` to PDFs in `./build/`.
