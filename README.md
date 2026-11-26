# 30k Songs Analysis

CSC17104 - Programming for Data Science, Final Project.

## Team

| Member | Student ID | Questions owned | Other tasks |
|---|---|---|---|
| Vo Thai Thanh | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |

## Dataset

- **Name:** 30000 Spotify Songs
- **Source:** TidyTuesday 2020-01-21 - https://github.com/rfordatascience/tidytuesday/tree/master/data/2020/2020-01-21 (also on Kaggle: TODO link)
- **Collected by / how:** TODO (who, when, how)
- **License:** TODO
- **Related public notebooks:** TODO (list them and explain how our questions differ)

## Questions

| # | Question | Owner | Type | Criteria |
|---|---|---|---|---|
| Q1 | TODO | TODO | ML / non-ML | TODO |

## Key findings

TODO

## How to run

```bash
conda env create -f environment.yml
conda activate songs30k
python -m src.download_data      # saves data/raw/spotify_songs.csv
jupyter lab                      # then run notebooks/ in order: 01 -> 02 -> 03
```

## Repository structure

```
README.md, environment.yml, LLM_USAGE.md
data/raw/, data/processed/   # not committed, created by src/download_data.py
src/                         # reusable Python modules
notebooks/                   # 01_collection_exploration, 02_analysis, 03_ml_question
slides.pdf
```
