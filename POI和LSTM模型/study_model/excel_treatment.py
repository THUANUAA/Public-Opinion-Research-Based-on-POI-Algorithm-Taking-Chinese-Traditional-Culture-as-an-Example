import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import os
# 读取数据
data_path = "C:/Users/86176/Desktop/统计建模/POI结果/最终POI结果.xlsx"
data = pd.read_excel(data_path)

# 获取文件名
data_file_name = os.path.splitext(os.path.basename(data_path))[0]

# 将负数转换为正数
data.iloc[:, 1:] = np.abs(data.iloc[:, 1:])

# 归一化处理
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data.iloc[:, 1:])

# 标准化处理
scaler = StandardScaler()
standardized_data = scaler.fit_transform(normalized_data)

# 将处理后的数据保存到文件
result_data = pd.DataFrame(standardized_data, columns=data.columns[1:])
result_data = result_data.abs()  # 将所有值取绝对值

result_file_path = f"C:/Users/86176/Desktop/统计建模/POI结果/{data_file_name}_treatment_results.xlsx"
result_data.to_excel(result_file_path, index=False)
