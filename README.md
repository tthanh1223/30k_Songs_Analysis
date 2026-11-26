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

## How we work with Git

Individual grades are based partly on the Git history, so everyone commits their own work from their own GitHub account.

### One-time setup

```bash
git clone https://github.com/tthanh1223/30k_Songs_Analysis.git
cd 30k_Songs_Analysis
git config user.name  "<your name>"            # must match your GitHub account
git config user.email "<your GitHub email>"
conda env create -f environment.yml
python -m src.download_data
```

### File ownership

Two people editing the same notebook almost always ends in a merge conflict that cannot be resolved cleanly, so each file has one owner.

| File | Owner |
|---|---|
| `notebooks/01_collection_exploration.ipynb` | Vo Thai Thanh |
| `notebooks/02_q<k>_<name>.ipynb` (one per non-ML question) | question owner |
| `notebooks/03_q<k>_<name>.ipynb` (one per ML question) | question owner |
| `src/` (shared loading and cleaning functions) | TODO |
| `README.md`, `slides.pdf` | TODO |

Want a change in a file you do not own? Ask its owner, or open an issue.

### Daily workflow

1. Never commit directly to `main`. Start from an up-to-date `main` and create a branch for your part:
   ```bash
   git switch main
   git pull
   git switch -c q1-<name>
   ```
2. Commit small, meaningful steps. Write messages that say what changed, e.g. `Q1: add bootstrap CI for genre trend`, not `update`.
   ```bash
   git add notebooks/02_q1_<name>.ipynb
   git commit -m "Q1: ..."
   git push -u origin q1-<name>
   ```
3. Open a pull request into `main`. Another member reads it, then merges. Keep pull requests small: one section of a question, not the whole question.
4. If `main` moved while you were working, update your branch before opening the pull request:
   ```bash
   git fetch
   git rebase origin/main
   git push --force-with-lease      # only on your own branch, never on main
   ```

### Notebooks and data

- `data/` is ignored. Everyone recreates it with `python -m src.download_data`. Processed data is produced by code, never committed.
- While working, clear outputs before committing to keep diffs small. `nbdime` (`nbdiff`) helps to read notebook diffs.
- Before submission, each owner runs **Restart & Run All** on their notebooks in order (01 → 02 → 03) and commits them with outputs.

## LLM usage

Following the course rules (Section 6 of the project spec):

- LLM tools are used **as a tutor only**: to explain concepts, error messages or library functions. They do not write our analysis, answers or reflections.
- Every member must be able to explain every line of the submission.
- Each **significant** use is recorded in `LLM_USAGE.md`, one row per use:

| Column | What to write |
|---|---|
| Date | `YYYY-MM-DD` |
| Member | who asked |
| Tool | e.g. ChatGPT, Claude, Copilot |
| What we asked | the question, in one sentence |
| How we used / changed the answer | what we kept, what we changed or rejected, and why |

- Significant = it shaped the content or code: a method, a question idea, a piece of code, a fix for a bug. Not significant: a quick syntax lookup, a typo fix, asking where a file is.
- Copied code or text from other sources (public notebooks, websites, other groups) is cited where it is used, and public notebooks on this dataset are listed in the Dataset section above.
