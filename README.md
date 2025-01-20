# Topsis-102217223

A simple Python package to calculate TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) scores for multi-criteria decision-making.

## Installation

To install the package from PyPI, use:
```bash
pip install Topsis-102217223
```

If you are working locally, you can install the package after building it:
```bash
pip install .
```

## Usage

You can run the package from the command line as follows:
```bash
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

### Parameters:
1. **InputDataFile**: The CSV file containing the data for TOPSIS analysis.
2. **Weights**: A comma-separated string of weights for each criterion (e.g., `"1,1,1,1,1"`).
3. **Impacts**: A comma-separated string of impacts (`+` for beneficial and `-` for non-beneficial) for each criterion (e.g., `"+,+,-,+,+"`).
4. **ResultFileName**: The name of the output CSV file to save the results.

### Example:

```bash
topsis input_files/102217223-data.csv "1,1,1,1,1" "+,+,-,+,+" output_files/102217223-result.csv
```

### Input CSV File Format:

The input CSV file must have:
- The first column containing the object names (e.g., `M1, M2, M3`).
- The remaining columns containing numeric values for the criteria.

#### Example Input File (`102217223-data.csv`):
```csv
Fund Name,P1,P2,P3,P4,P5
M1,0.75,0.56,6.3,47,13.65
M2,0.81,0.66,3.7,34.8,9.99
M3,0.86,0.74,5.6,55.5,15.68
M4,0.89,0.79,3.9,68.1,18.42
M5,0.71,0.5,5.5,34.4,10.28
M6,0.72,0.52,3.5,48.7,13.36
M7,0.8,0.64,3.7,69.4,18.64
M8,0.95,0.9,3,39.8,11.16
```

### Output CSV File Format:

The output CSV file will contain all the columns of the input file, along with two additional columns:
- **Topsis Score**: The calculated TOPSIS score for each object.
- **Rank**: The rank of each object based on the TOPSIS score.

#### Example Output File (`102217223-result.csv`):
```csv
Fund Name,P1,P2,P3,P4,P5,Topsis Score,Rank
M1,0.75,0.56,6.3,47,13.65,0.57,4
M2,0.81,0.66,3.7,34.8,9.99,0.43,7
M3,0.86,0.74,5.6,55.5,15.68,0.63,3
M4,0.89,0.79,3.9,68.1,18.42,0.76,1
M5,0.71,0.5,5.5,34.4,10.28,0.41,8
M6,0.72,0.52,3.5,48.7,13.36,0.46,6
M7,0.8,0.64,3.7,69.4,18.64,0.74,2
M8,0.95,0.9,3,39.8,11.16,0.44,5
```

## Notes

- Ensure the number of weights and impacts matches the number of criteria columns in the input file.
- The impacts must be either `+` (beneficial) or `-` (non-beneficial).
- The program will validate the input file for correctness and handle errors gracefully.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
