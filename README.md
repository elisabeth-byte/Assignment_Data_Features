# Assignment Data Features

## Requirements

Install the required libraries obviously; pandas and matplotlib

## Running the Code

Each dataset is analysed in a separate Python file:

- `dataset_vaer.py`
- `dataset_student.py`
- `dataset_bolig.py`

Run one of the scripts. 

## Reproducing the Results

The scripts perform:

1. Initial exploration of the dataset. 
2. Identification of missing values.
3. Application of the baseline method (`dropna()`).
4. Application of imputation methods:
   - Mean imputation
   - Median imputation
   - Mode imputation
   - Linear interpolation (weather dataset only)
5. Comparison of dataset size and summary statistics before and after imputation.

The values printed to the terminal correspond to the results presented in the report. 
