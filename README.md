# bubble-vs-quicksort

This project was created as part of an MSc Computer Science assignment.

It compares the performance of two sorting algorithms — Bubble Sort and Quicksort — implemented in Python.  
The task involves analysing their time complexity, generating performance graphs for various input sizes, and reporting on their efficiency.

## Features

- Python implementation of Bubble Sort and Quicksort
- Performance benchmarking across increasing input sizes
- Matplotlib graph to visualise execution time
- Clean project structure with virtual environment and requirements file

## How to Run

1. Clone the repository:
git clone https://github.com/wykesprojectsbubble-vs-quicksort.git
cd bubble-vs-quicksort

2. Create and activate a virtual environment:
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the script:
python sort_compare.py

The output graph will be saved as `graph.png` and also displayed on-screen.

## Files

- `sort_compare.py` – main Python script
- `requirements.txt` – dependencies list
- `graph.png` – performance output (excluded in .gitignore by default)
- `.gitignore` – excludes `.venv/`, `__pycache__/`, and `graph.png`

## Notes

- Bubble Sort has O(n²) time complexity and performs poorly on large datasets.
- Quicksort has average-case O(n log n) time complexity and scales efficiently.