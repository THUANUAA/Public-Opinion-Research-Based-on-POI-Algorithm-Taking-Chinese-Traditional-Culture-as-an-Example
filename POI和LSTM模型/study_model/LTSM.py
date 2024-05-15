'''
Author: Interest 1368534721@qq.com
Date: 2024-05-10 15:14:42
LastEditors: Interest 1368534721@qq.com
LastEditTime: 2024-05-13 13:57:16
FilePath: \Hello Python\study_model\LTSM.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

# 读取数据
# 尝试使用不同的编码格式读取文件
data = pd.read_excel("C:/Users/86176/Desktop/统计建模/POI结果/data.xlsx")


# 将时间列转换为日期时间格式
data['Time'] = pd.to_datetime(data['Time'])

# 对 EI 数据进行标准化或归一化
scaler = MinMaxScaler()
data['DI_scaled'] = scaler.fit_transform(data[['DI']])

# 准备数据


def prepare_data(data, time_steps):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data['DI_scaled'].iloc[i:i+time_steps].values)
        y.append(data['DI_scaled'].iloc[i+time_steps])
    return np.array(X), np.array(y)


time_steps = 12  # 假设使用前12个时间步长的数据进行预测
X, y = prepare_data(data, time_steps)

# 将数据划分为训练集和测试集
train_size = int(len(X) * 0.75)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]
# 构建 LSTM 模型
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(time_steps, 1)))
model.add(LSTM(units=50))
model.add(Dense(1))  # 输出维度为1
model.compile(optimizer='adam', loss='mean_squared_error')

# 训练模型
model.fit(X_train.reshape(-1, time_steps, 1), y_train, epochs=100, batch_size=32)

# 模型评估
loss = model.evaluate(X_test.reshape(-1, time_steps, 1), y_test)
print("Test Loss:", loss)

# 使用模型进行未来6个时间步长的预测
future_steps = 6
future_predictions = []

# 使用最后 time_steps 个观测值作为初始输入
current_input = X_test[-1]

for _ in range(future_steps):
    # 预测下一个时间步长的值
    next_prediction = model.predict(current_input.reshape(1, time_steps, 1))
    # 将预测值添加到预测序列中
    future_predictions.append(next_prediction)
    # 更新当前输入，将新预测值添加到末尾，并移除第一个值
    current_input = np.append(current_input[1:], next_prediction)

# 反归一化得到原始数据的预测值
predicted_values = scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1))

# 输出预测结果
print("未来6个时间步长的预测值：")
for i, pred in enumerate(predicted_values):
    print(f"时间步长 {i+1}: {pred[0]}")

# 创建包含预测结果的 DataFrame
future_dates = pd.date_range(start=data['Time'].iloc[-1], periods=future_steps+1, freq='M')[1:]
future_predictions_df = pd.DataFrame({'Time': future_dates, 'DI_predicted': predicted_values.flatten()})

# 将预测结果添加到原始数据中
predicted_data = pd.concat([data, future_predictions_df])

# 保存预测结果到 Excel 文件
predicted_data.to_excel("C:/Users/86176/Desktop/统计建模/POI结果/predicted_data.xlsx", index=False)
