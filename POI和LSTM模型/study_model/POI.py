import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def relu(x):
    return np.maximum(0, x)


def calculate_EIt(sum_df_n, sum_df_i, n):
    if n > 1:
        sum_df_i_n_1 = sum_df_i / (n - 1)
        EIt = relu((sum_df_n - sum_df_i_n_1)) / (1 + sum_df_i_n_1)
    else:
        EIt = 0
    return EIt


def calculate_SIt(sum_df_n, sum_df_p, sum_i_df_n, sum_i_df_p):
    SIt = relu(sum_df_n / (1 + sum_i_df_n) - sum_df_p / (1 + sum_i_df_p))
    return SIt


def calculate_DI_t(sum_df_n, sum_df_i, n):
    if n > 1:
        sum_df_i_n_1 = sum_df_i / (n - 1)
        DI_temp = relu((sum_df_n - sum_df_i_n_1))
        DI_t = np.arctan(np.log(10) * (1 + DI_temp))
    else:
        DI_t = 0
    return DI_t


# Read data from Excel
data_file_path = "C:/Users/86176/Desktop/统计建模/统计/武侠.xlsx"
df = pd.read_excel(data_file_path)

# Extract data file name
data_file_name = os.path.splitext(os.path.basename(data_file_path))[0]
results = []

for i in range(len(df)):
    sum_df_n = df.iloc[i, 1]  # Accessing the 'positive' column
    sum_df_i = sum(df.iloc[:i, 2])  # Accessing the 'negative' column
    sum_df_p = df.iloc[i, 2]  # Accessing the 'negative' column
    sum_i_df_n = sum(df.iloc[1:i, 1])  # Accessing the 'positive' column
    sum_i_df_p = sum(df.iloc[1:i, 2])  # Accessing the 'negative' column

    EIt = calculate_EIt(sum_df_n, sum_df_i, i)
    SIt = calculate_SIt(sum_df_n, sum_df_p, sum_i_df_n, sum_i_df_p)
    DIt = calculate_DI_t(sum_df_n, sum_df_i, i)
    POI = EIt + SIt + DIt

    results.append([df.iloc[i, 0], EIt, SIt, DIt, POI])

# Create a DataFrame from the results
results_df = pd.DataFrame(results, columns=["Time", "EIt", "SIt", "DIt", "POI"])

# Normalize the results
scaler = MinMaxScaler()
normalized_results = scaler.fit_transform(results_df[["EIt", "SIt", "DIt", "POI"]])
results_df["EIt_normalized"] = normalized_results[:, 0]
results_df["SIt_normalized"] = normalized_results[:, 1]
results_df["DIt_normalized"] = normalized_results[:, 2]
results_df["POI_normalized"] = normalized_results[:, 3]

# Construct result file path and save the DataFrame to an Excel file
result_file_path = f"C:/Users/86176/Desktop/统计建模/POI结果/{data_file_name}_POI_results.xlsx"
results_df.to_excel(result_file_path, index=False)

print(f"Great!Results saved to {result_file_path}")
