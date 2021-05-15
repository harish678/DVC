# DVC

## Installation

`pip install dvc`

## Getting Started

1. Create a Directory
2. `git init`
3. `dvc init`
4. Getting Data
   - `dvc get [URL] -o [file-path]`
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

<u>Note:</u>

1. DVC tracks every file using cache file in `.dvc/cache` directory.
