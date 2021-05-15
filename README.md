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
   ```
   git checkout HEAD^1 data/data.tsv.dvc
   dvc checkout
   ```
8. List DVC tracked files in project
   - `dvc list https://github.com/harish678/DVC data`
9. Get latest upates of a file
   - `dvc update data/data.tsv.dvc`

<u>Note:</u>

1. DVC tracks every file using cache file in `.dvc/cache` directory.
2. `dvc import` to remember the Source URL.
