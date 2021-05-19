# DVC

## Installation

`pip install dvc`

## Getting Started

1. Create a Directory
2. `git init`
3. `dvc init`
4. Getting Data
   ```
   dvc get [URL] -o [file-path]
   dvc import [URL] -o [file-path]
   ```
5. Track the Data
   - `dvc add [file-path]`
6. Push data to remote storage
   ```console
    dvc remote add -d storage gdrive://[UID]`
    dvc push
   ```
7. Revert back (**give .dvc file**)
   ```console
   git checkout HEAD^1 data/data.tsv.dvc
   dvc checkout
   ```
8. List DVC tracked files in project
   - `dvc list https://github.com/harish678/DVC data`
9. Get latest upates of a file
   - `dvc update data/data.tsv.dvc`

## DVC Pipeline

2 ways using `dvc run` or `dvc.yml` file.

```console
dvc run -n prepare \
          -p prepare.seed,prepare.split \
          -d src/prepare.py -d data/data.xml \
          -o data/prepared \
          python src/prepare.py data/data.xml
```

`dvc repro` to run the pipeline using **dvc.yml** file

`dvc dag` to visualize the pipeline

## DVC Experiments

`dvc params diff` will show the difference in params over time.
`dvc metrics diff` will show the difference in metrics over time.
`dvc plots diff` will save the HTML file with plots   

<u>Note:</u>

1. DVC tracks every file using cache file in `.dvc/cache` directory.
2. `dvc import` to remember the Source URL.
