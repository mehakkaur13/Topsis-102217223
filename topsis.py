import pandas as pd
import numpy as np
import os

def topsis(input_file, weights, impacts, result_file):
    if not os.path.exists(input_file):
        print("Error: Input file not found.")
        return

    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error: Unable to read the input file. {e}")
        return

    if df.shape[1] < 3:
        print("Error: Input file must have at least three columns.")
        return

    try:
        df.iloc[:, 1:] = df.iloc[:, 1:].astype(float)
    except ValueError:
        print("Error: Non-numeric values found in criteria columns.")
        return

    try:
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')
    except:
        print("Error: Weights and impacts must be comma-separated and formatted correctly.")
        return

    if len(weights) != len(impacts) or len(weights) != df.shape[1] - 1:
        print("Error: Number of weights and impacts must match the number of criteria.")
        return

    if not all(impact in ['+', '-'] for impact in impacts):
        print("Error: Impacts must be '+' or '-'.")
        return

    norm_df = df.iloc[:, 1:].div(np.sqrt((df.iloc[:, 1:] ** 2).sum()), axis=1)
    weighted_df = norm_df.mul(weights, axis=1)
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_df.iloc[:, i].max())
            ideal_worst.append(weighted_df.iloc[:, i].min())
        else:
            ideal_best.append(weighted_df.iloc[:, i].min())
            ideal_worst.append(weighted_df.iloc[:, i].max())

    dist_best = np.sqrt(((weighted_df - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_df - ideal_worst) ** 2).sum(axis=1))
    scores = dist_worst / (dist_best + dist_worst)
    df['Topsis Score'] = scores
    df['Rank'] = scores.rank(ascending=False)

    try:
        df.to_csv(result_file, index=False)
        print(f"Result saved to {result_file}")
    except Exception as e:
        print(f"Error: Unable to save the result file. {e}")