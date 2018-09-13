# check_barcodes

Reads the file provenance report and prints out lanes with samples/barcodes that may have
a collision with another sample/barcode that was processed in a different workflow run.

## Requirements
- virtualenv
- python3

## Installation

```
# local install
/usr/bin/python3 -m venv venv
# or cluster install
/.mounts/labs/PDE/Modules/sw/python/Python-3.6.4/bin/python3.6 -m venv venv

# activate virtual environment
source venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

## Run

```
source venv/bin/activate

python cli.py check-barcodes --help
```
